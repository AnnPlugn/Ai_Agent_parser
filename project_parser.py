import json
from typing import TypedDict, List, Dict, Optional

from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import logging
import math
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import load_env_file, LLMProvider, LLMConfig
from prompts import PROMPTS

# Импорт из отдельного файла парсеров
from parsers import (
    extract_dependencies,
    extract_prompts,
    load_requirements,
    get_project_structure,
    extract_text_from_pdf,
    extract_text_from_docx,
    extract_text_from_txt,
    extract_csv_requirements,
    extract_excel_requirements,
    smart_parse_txt_bpmn,
    parse_md,
    extract_java_dependencies,
    extract_js_dependencies,
    extract_cpp_dependencies,
    extract_business_requirements,
    extract_project_description,
    should_process_file,
    get_supported_extensions
)

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка .env файла
load_env_file()


def create_llm_client(config: LLMConfig):
    """Создание LLM клиента на основе конфигурации"""
    try:
        if config.provider == LLMProvider.GIGACHAT:
            from langchain_gigachat import GigaChat
            if not (config.cert_file and config.key_file):
                raise ValueError("Для GigaChat необходимы cert_file и key_file")
            return GigaChat(
                base_url=config.base_url,
                cert_file=config.cert_file,
                key_file=config.key_file,
                model=config.model,
                temperature=config.temperature,
                top_p=config.top_p,
                verify_ssl_certs=config.verify_ssl_certs,
                profanity_check=config.profanity_check,
                streaming=config.streaming
            )
        else:
            from langchain_openai import OpenAI
            return OpenAI(
                base_url=config.base_url,
                model=config.model,
                temperature=config.temperature,
                max_tokens=config.max_tokens,
                timeout=config.timeout,
                api_key=config.api_key
            )
    except ImportError as e:
        logger.error(f"❌ Не удалось импортировать необходимые библиотеки: {e}")
        raise
    except Exception as e:
        logger.error(f"❌ Ошибка создания LLM клиента: {e}")
        raise


# Определение состояния графа
class ParserState(TypedDict):
    directory_path: str
    files_list: List[str]
    empty_files: List[str]
    dependencies: Dict[str, Dict[str, List[str]]]
    prompts: Dict[str, List[str]]
    requirements: Dict[str, str]
    business_requirements: Dict[str, str]
    project_descriptions: Dict[str, str]
    analysis: str
    final_report: str
    project_structure: Dict[str, List[str]]
    file_stats: Dict[str, int]


def chunk_text(text: str, chunk_size: int = 80000, overlap: float = 0.2) -> List[str]:
    """Разделение текста на чанки с перекрытием"""
    chunks = []
    overlap_size = int(chunk_size * overlap)
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap_size
    return chunks


def get_files_node(state: ParserState) -> ParserState:
    """Получение списка файлов с улучшенной фильтрацией"""
    files = []
    empty_files = []
    supported_extensions = get_supported_extensions()

    # Объединяем все поддерживаемые расширения
    all_supported = []
    for category in supported_extensions.values():
        all_supported.extend(category)

    project_structure = get_project_structure(state['directory_path'])
    file_stats = {}

    for root, dirs, filenames in os.walk(state['directory_path']):
        if '.git' in dirs:
            dirs.remove('.git')
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        if 'node_modules' in dirs:
            dirs.remove('node_modules')

        for filename in filenames:
            file_path = os.path.join(root, filename)
            ext = os.path.splitext(filename)[1].lower()

            # Пропускаем неподдерживаемые файлы
            if not should_process_file(file_path):
                continue

            try:
                file_size = os.path.getsize(file_path)
                if file_size == 0:
                    empty_files.append(file_path)
                    continue
                elif file_size > 10 * 1024 * 1024:  # Пропускаем файлы больше 10MB
                    logger.warning(f"Пропускаем слишком большой файл: {file_path} ({file_size} байт)")
                    continue

                files.append(file_path)

                # Статистика по расширениям
                if ext not in file_stats:
                    file_stats[ext] = 0
                file_stats[ext] += 1

            except OSError as e:
                logger.warning(f"Ошибка доступа к файлу {file_path}: {e}")
                continue

    state['files_list'] = files
    state['empty_files'] = empty_files
    state['project_structure'] = project_structure
    state['file_stats'] = file_stats

    logger.info(f"Найдено {len(files)} поддерживаемых файлов и {len(empty_files)} пустых файлов")
    logger.info(f"Статистика файлов: {file_stats}")
    return state


def analyze_files_node(state: ParserState) -> ParserState:
    """Анализ файлов с расширенной обработкой различных типов"""
    dependencies = {}
    prompts = {}
    requirements = {}
    business_requirements = {}
    project_descriptions = {}

    # Классифицируем файлы по типам для оптимизации обработки
    code_files = []
    document_files = []
    data_files = []

    supported = get_supported_extensions()

    for file in state['files_list']:
        ext = os.path.splitext(file)[1].lower()
        if ext in supported['code_files']:
            code_files.append(file)
        elif ext in supported['document_files']:
            document_files.append(file)
        elif ext in supported['data_files']:
            data_files.append(file)

    logger.info(
        f"Классификация файлов: код={len(code_files)}, документы={len(document_files)}, данные={len(data_files)}")

    with ThreadPoolExecutor(max_workers=4) as executor:
        # Анализ зависимостей для кодовых файлов
        future_to_file = {}

        for file in code_files:
            future_to_file[executor.submit(safe_extract_dependencies, file)] = file

        # Извлечение промптов из всех файлов
        for file in state['files_list']:
            future_to_file[executor.submit(safe_extract_prompts, file)] = file

        # Извлечение требований и описаний из документов
        for file in document_files + data_files:
            future_to_file[executor.submit(safe_load_requirements, file)] = file
            future_to_file[executor.submit(safe_extract_business_requirements, file)] = file
            future_to_file[executor.submit(safe_extract_project_description, file)] = file

        # Обработка результатов
        for future in as_completed(future_to_file):
            file = future_to_file[future]
            try:
                result = future.result()
                task_type = determine_task_type(future, file)

                if task_type == 'dependencies':
                    dependencies[file] = result
                elif task_type == 'prompts':
                    if result:  # Только если есть промпты
                        prompts[file] = result
                elif task_type == 'requirements':
                    if result and len(result.strip()) > 10:
                        requirements[file] = result
                elif task_type == 'business_requirements':
                    if result and len(result.strip()) > 10:
                        business_requirements[file] = result
                elif task_type == 'project_description':
                    if result and len(result.strip()) > 10:
                        project_descriptions[file] = result

            except Exception as e:
                logger.error(f"Ошибка при обработке {file}: {e}")

    state['dependencies'] = dependencies
    state['prompts'] = prompts
    state['requirements'] = requirements
    state['business_requirements'] = business_requirements
    state['project_descriptions'] = project_descriptions

    logger.info(f"Результаты анализа:")
    logger.info(f"  - Зависимости: {len(dependencies)} файлов")
    logger.info(f"  - Промпты: {len(prompts)} файлов")
    logger.info(f"  - Требования: {len(requirements)} файлов")
    logger.info(f"  - Бизнес-требования: {len(business_requirements)} файлов")
    logger.info(f"  - Описания проекта: {len(project_descriptions)} файлов")

    return state


def safe_extract_dependencies(file_path: str) -> Dict[str, List[str]]:
    """Безопасное извлечение зависимостей с обработкой ошибок"""
    try:
        return extract_dependencies(file_path)
    except Exception as e:
        logger.error(f"Ошибка извлечения зависимостей из {file_path}: {e}")
        return {"libraries": [], "functions": []}


def safe_extract_prompts(file_path: str) -> List[str]:
    """Безопасное извлечение промптов с обработкой ошибок"""
    try:
        return extract_prompts(file_path)
    except Exception as e:
        logger.error(f"Ошибка извлечения промптов из {file_path}: {e}")
        return []


def safe_load_requirements(file_path: str) -> str:
    """Безопасная загрузка требований с обработкой ошибок"""
    try:
        return load_requirements(file_path)
    except Exception as e:
        logger.error(f"Ошибка загрузки требований из {file_path}: {e}")
        return ""


def safe_extract_business_requirements(file_path: str) -> str:
    """Безопасное извлечение бизнес-требований с обработкой ошибок"""
    try:
        return extract_business_requirements(file_path)
    except Exception as e:
        logger.error(f"Ошибка извлечения бизнес-требований из {file_path}: {e}")
        return ""


def safe_extract_project_description(file_path: str) -> str:
    """Безопасное извлечение описания проекта с обработкой ошибок"""
    try:
        return extract_project_description(file_path)
    except Exception as e:
        logger.error(f"Ошибка извлечения описания проекта из {file_path}: {e}")
        return ""


def determine_task_type(future, file_path: str) -> str:
    """Определяет тип задачи на основе функции и файла"""
    # Это упрощенная версия - в реальности нужно отслеживать какая функция была вызвана
    # Здесь мы определяем по расширению файла и содержимому
    ext = os.path.splitext(file_path)[1].lower()
    filename = os.path.basename(file_path).lower()

    if 'dependencies' in str(future):
        return 'dependencies'
    elif 'prompts' in str(future):
        return 'prompts'
    elif 'business' in filename or 'requirements' in filename:
        return 'business_requirements'
    elif 'readme' in filename or 'description' in filename:
        return 'project_description'
    else:
        return 'requirements'


def llm_analysis_node(state: ParserState, llm) -> ParserState:
    """Расширенный LLM анализ с обработкой новых типов данных"""
    try:
        # Подготовка данных для LLM
        dep_content = prepare_dependencies_content(state['dependencies'])
        prompt_content = prepare_prompts_content(state['prompts'])
        req_content = prepare_requirements_content(state['requirements'])
        business_content = prepare_business_content(state['business_requirements'])
        description_content = prepare_description_content(state['project_descriptions'])
        structure_content = prepare_structure_content(state['project_structure'])
        stats_content = prepare_stats_content(state['file_stats'])

        # Формируем полный контент для анализа
        all_content = f"""
=== СТАТИСТИКА ПРОЕКТА ===
{stats_content}

=== АРХИТЕКТУРА ПРОЕКТА ===
{structure_content}

=== ОПИСАНИЯ ПРОЕКТА ===
{description_content}

=== БИЗНЕС-ТРЕБОВАНИЯ ===
{business_content}

=== ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ ===
{req_content}

=== ЗАВИСИМОСТИ И КОД ===
{dep_content}

=== ПРОМПТЫ И ШАБЛОНЫ ===
{prompt_content}
"""

        # Чанкинг для больших проектов
        max_input_size = 100000
        chunks = chunk_text(all_content, chunk_size=80000, overlap=0.2)

        system_prompt_template = ChatPromptTemplate.from_template(PROMPTS['system_prompt'])
        chain = system_prompt_template | llm | StrOutputParser()

        analysis_chunks = []
        for i, chunk in enumerate(chunks):
            logger.info(f"Обрабатываем чанк {i + 1}/{len(chunks)}")
            try:
                analysis_chunk = chain.invoke({"content": chunk})
                analysis_chunks.append(analysis_chunk)
            except Exception as e:
                logger.error(f"Ошибка обработки чанка {i + 1}: {e}")
                analysis_chunks.append(f"Ошибка обработки чанка {i + 1}: {str(e)}")

        # Суммаризация чанков
        if len(analysis_chunks) > 1:
            summary_prompt = ChatPromptTemplate.from_template(
                "Объедини и суммируй эти анализы в единый coherentный отчет: {analyses}"
            )
            summary_chain = summary_prompt | llm | StrOutputParser()
            analysis = summary_chain.invoke({"analyses": "\n\n".join(analysis_chunks)})
        else:
            analysis = analysis_chunks[0] if analysis_chunks else "Анализ не удался"

        # Проверка с помощью judge
        judge_result = run_judge_validation(llm, analysis, all_content)

        # Улучшение анализа на основе результатов judge
        final_analysis = enhance_analysis_with_judge_feedback(
            analysis, judge_result, state, dep_content, prompt_content,
            req_content, business_content, description_content, structure_content
        )

        # Сохранение результатов
        save_analysis_results(final_analysis, state)

        state['analysis'] = final_analysis
        logger.info("✅ LLM анализ завершен и сохранен")

    except Exception as e:
        logger.error(f"❌ Ошибка при LLM анализе: {e}")
        error_analysis = generate_error_analysis(e, state)
        state['analysis'] = error_analysis
        save_analysis_results(error_analysis, state)

    return state


def prepare_dependencies_content(dependencies: Dict[str, Dict[str, List[str]]]) -> str:
    """Подготовка контента зависимостей"""
    if not dependencies:
        return "Зависимости не найдены."

    content = "АНАЛИЗ ЗАВИСИМОСТЕЙ И АРХИТЕКТУРЫ:\n\n"

    # Статистика по библиотекам
    all_libs = set()
    all_functions = set()

    for file_path, deps in dependencies.items():
        all_libs.update(deps.get('libraries', []))
        all_functions.update(deps.get('functions', []))

    content += f"Общая статистика:\n"
    content += f"- Уникальных библиотек: {len(all_libs)}\n"
    content += f"- Уникальных функций: {len(all_functions)}\n\n"

    if all_libs:
        content += f"Ключевые библиотеки: {', '.join(sorted(list(all_libs))[:20])}\n\n"

    # Детализация по файлам (ограниченная)
    content += "Детали по файлам:\n"
    for file_path, deps in list(dependencies.items())[:10]:  # Ограничиваем количество
        rel_path = os.path.relpath(file_path)
        content += f"\n{rel_path}:\n"
        if deps['libraries']:
            content += f"  Библиотеки: {', '.join(deps['libraries'][:10])}\n"
        if deps['functions']:
            content += f"  Функции: {', '.join(deps['functions'][:10])}\n"

    return content


def prepare_prompts_content(prompts: Dict[str, List[str]]) -> str:
    """Подготовка контента промптов"""
    if not prompts:
        return "Промпты не найдены."

    content = "ИЗВЛЕЧЕННЫЕ ПРОМПТЫ И ШАБЛОНЫ:\n\n"
    total_prompts = sum(len(prompt_list) for prompt_list in prompts.values())
    content += f"Всего найдено промптов: {total_prompts}\n\n"

    for file_path, prompt_list in prompts.items():
        if not prompt_list:
            continue

        rel_path = os.path.relpath(file_path)
        content += f"\n=== {rel_path} ({len(prompt_list)} промптов) ===\n"

        for i, prompt in enumerate(prompt_list[:5], 1):  # Ограничиваем 5 промптами на файл
            # Обрезаем слишком длинные промпты
            truncated_prompt = prompt[:500] + "..." if len(prompt) > 500 else prompt
            content += f"\n{i}. {truncated_prompt}\n"

        if len(prompt_list) > 5:
            content += f"\n... и еще {len(prompt_list) - 5} промптов\n"

    return content


def prepare_requirements_content(requirements: Dict[str, str]) -> str:
    """Подготовка контента технических требований"""
    if not requirements:
        return "Технические требования не найдены."

    content = "ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ И ДОКУМЕНТАЦИЯ:\n\n"

    for file_path, req in requirements.items():
        rel_path = os.path.relpath(file_path)
        content += f"\n=== {rel_path} ===\n"

        # Обрезаем слишком длинные требования
        if len(req) > 2000:
            content += req[:2000] + f"\n... [обрезано, полная длина: {len(req)} символов]\n"
        else:
            content += req + "\n"

    return content


def prepare_business_content(business_requirements: Dict[str, str]) -> str:
    """Подготовка контента бизнес-требований"""
    if not business_requirements:
        return "Бизнес-требования не найдены."

    content = "БИЗНЕС-ТРЕБОВАНИЯ И ПРОЦЕССЫ:\n\n"

    for file_path, req in business_requirements.items():
        rel_path = os.path.relpath(file_path)
        content += f"\n=== {rel_path} ===\n"

        if len(req) > 3000:
            content += req[:3000] + f"\n... [обрезано, полная длина: {len(req)} символов]\n"
        else:
            content += req + "\n"

    return content


def prepare_description_content(project_descriptions: Dict[str, str]) -> str:
    """Подготовка контента описаний проекта"""
    if not project_descriptions:
        return "Описания проекта не найдены."

    content = "ОПИСАНИЯ И ОБЗОР ПРОЕКТА:\n\n"

    for file_path, desc in project_descriptions.items():
        rel_path = os.path.relpath(file_path)
        content += f"\n=== {rel_path} ===\n"
        content += desc + "\n"

    return content


def prepare_structure_content(project_structure: Dict[str, List[str]]) -> str:
    """Подготовка контента структуры проекта"""
    content = "СТРУКТУРА ПРОЕКТА:\n\n"

    for dir_path, files in project_structure.items():
        content += f"{dir_path}:\n"
        for file in files[:20]:  # Ограничиваем количество файлов
            content += f"  - {file}\n"
        if len(files) > 20:
            content += f"  ... и еще {len(files) - 20} файлов\n"
        content += "\n"

    return content


def prepare_stats_content(file_stats: Dict[str, int]) -> str:
    """Подготовка статистики по файлам"""
    if not file_stats:
        return "Статистика файлов недоступна."

    content = "СТАТИСТИКА ПО ТИПАМ ФАЙЛОВ:\n"
    total_files = sum(file_stats.values())
    content += f"Всего файлов: {total_files}\n\n"

    for ext, count in sorted(file_stats.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_files) * 100
        content += f"{ext}: {count} файлов ({percentage:.1f}%)\n"

    return content


def run_judge_validation(llm, analysis: str, content: str) -> Dict:
    """Запуск валидации judge"""
    try:
        judge_prompt_template = ChatPromptTemplate.from_template(PROMPTS['judge'])
        judge_chain = judge_prompt_template | llm | StrOutputParser()

        judge_input = {
            "system_prompt": PROMPTS['system_prompt'],
            "analysis": analysis[:5000],  # Ограничиваем для judge
            "content": content[:10000]  # Ограничиваем для judge
        }

        judge_output = judge_chain.invoke(judge_input)

        try:
            judge_result = json.loads(judge_output)
        except json.JSONDecodeError:
            logger.warning("Не удалось распарсить JSON ответ от judge")
            judge_result = {"status": "unknown", "missing": []}

        return judge_result

    except Exception as e:
        logger.error(f"Ошибка в judge валидации: {e}")
        return {"status": "error", "missing": []}


def enhance_analysis_with_judge_feedback(analysis: str, judge_result: Dict, state: ParserState,
                                         dep_content: str, prompt_content: str, req_content: str,
                                         business_content: str, description_content: str,
                                         structure_content: str) -> str:
    """Улучшение анализа на основе обратной связи от judge"""

    if judge_result.get('status') == 'good':
        return analysis

    enhanced_analysis = analysis
    missing = judge_result.get('missing', [])

    if "prompts" in missing and state['prompts']:
        enhanced_analysis += f"\n\n=== ДОПОЛНИТЕЛЬНЫЕ ПРОМПТЫ ===\n{prompt_content}"

    if "dependencies" in missing and state['dependencies']:
        enhanced_analysis += f"\n\n=== ДОПОЛНИТЕЛЬНЫЕ ЗАВИСИМОСТИ ===\n{dep_content}"

    if "structure" in missing:
        enhanced_analysis += f"\n\n=== ДОПОЛНИТЕЛЬНАЯ АРХИТЕКТУРА ===\n{structure_content}"

    if "requirements" in missing and state['requirements']:
        enhanced_analysis += f"\n\n=== ДОПОЛНИТЕЛЬНЫЕ ТРЕБОВАНИЯ ===\n{req_content}"

    if "business" in missing and state['business_requirements']:
        enhanced_analysis += f"\n\n=== ДОПОЛНИТЕЛЬНЫЕ БИЗНЕС-ТРЕБОВАНИЯ ===\n{business_content}"

    if "description" in missing and state['project_descriptions']:
        enhanced_analysis += f"\n\n=== ДОПОЛНИТЕЛЬНЫЕ ОПИСАНИЯ ПРОЕКТА ===\n{description_content}"

    return enhanced_analysis


def save_analysis_results(analysis: str, state: ParserState):
    """Сохранение результатов анализа"""
    try:
        analysis_file = "llm_analysis.txt"
        with open(analysis_file, 'w', encoding='utf-8') as f:
            f.write(analysis)
        state['analysis_file'] = analysis_file

        # Дополнительно сохраняем детальную информацию
        details_file = "analysis_details.json"
        details = {
            "file_stats": state['file_stats'],
            "prompts_count": sum(len(prompts) for prompts in state['prompts'].values()),
            "dependencies_count": len(state['dependencies']),
            "requirements_count": len(state['requirements']),
            "business_requirements_count": len(state['business_requirements']),
            "project_descriptions_count": len(state['project_descriptions']),
            "total_files": len(state['files_list']),
            "empty_files": len(state['empty_files'])
        }

        with open(details_file, 'w', encoding='utf-8') as f:
            json.dump(details, f, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(f"Ошибка сохранения результатов анализа: {e}")


def generate_error_analysis(error: Exception, state: ParserState) -> str:
    """Генерация анализа в случае ошибки"""
    error_msg = f"Ошибка LLM анализа: {str(error)}\n\n"

    if "404" in str(error):
        error_msg += "Возможные причины:\n"
        error_msg += "- Неверный URL API\n"
        error_msg += "- Неподдерживаемый провайдер LLM\n"
        error_msg += "- Проблемы с сетевым подключением\n\n"

    # Добавляем базовую информацию о проекте
    error_msg += "БАЗОВАЯ ИНФОРМАЦИЯ О ПРОЕКТЕ:\n\n"
    error_msg += f"Всего файлов: {len(state['files_list'])}\n"
    error_msg += f"Пустых файлов: {len(state['empty_files'])}\n"

    if state['file_stats']:
        error_msg += f"Статистика файлов: {state['file_stats']}\n"

    if state['dependencies']:
        error_msg += f"Файлов с зависимостями: {len(state['dependencies'])}\n"

    if state['prompts']:
        total_prompts = sum(len(prompts) for prompts in state['prompts'].values())
        error_msg += f"Всего найдено промптов: {total_prompts}\n"

    return error_msg


def compile_report_node(state: ParserState) -> ParserState:
    """Компиляция итогового отчета с расширенной информацией"""
    report = "# 🤖 Детальный отчет по анализу ИИ-агента/проекта\n\n"

    # Исполнительное резюме
    report += generate_executive_summary(state)

    # Архитектура проекта
    report += "## 📁 Архитектура проекта\n\n"
    report += generate_architecture_section(state)

    # Статистика файлов
    report += "## 📊 Статистика файлов\n\n"
    report += generate_file_statistics(state)

    # Описания проекта
    if state['project_descriptions']:
        report += "## 📋 Описания проекта\n\n"
        report += generate_project_descriptions_section(state)

    # Бизнес-требования
    if state['business_requirements']:
        report += "## 💼 Бизнес-требования\n\n"
        report += generate_business_requirements_section(state)

    # Технические требования
    if state['requirements']:
        report += "## ⚙️ Технические требования и документация\n\n"
        report += generate_technical_requirements_section(state)

    # Зависимости и функции
    report += "## 🔧 Зависимости и архитектурные компоненты\n\n"
    report += generate_dependencies_section(state)

    # Промпты и шаблоны
    if state['prompts']:
        report += "## 🎯 Промпты и шаблоны ИИ\n\n"
        report += generate_prompts_section(state)

    # LLM анализ
    report += "## 🧠 Экспертный анализ ИИ\n\n"
    report += state['analysis'] + "\n\n"

    # Пустые файлы
    if state['empty_files']:
        report += "## ⚠️ Пустые файлы\n\n"
        report += generate_empty_files_section(state)

    # Рекомендации
    report += generate_recommendations_section(state)

    state['final_report'] = report
    return state


def generate_executive_summary(state: ParserState) -> str:
    """Генерация исполнительного резюме"""
    summary = "## 📈 Исполнительное резюме\n\n"

    total_files = len(state['files_list'])
    prompts_count = sum(len(prompts) for prompts in state['prompts'].values())
    deps_count = len(state['dependencies'])

    summary += f"**Обзор проекта:**\n"
    summary += f"- 📁 Всего обработано файлов: **{total_files}**\n"
    summary += f"- 🎯 Найдено промптов ИИ: **{prompts_count}**\n"
    summary += f"- 🔧 Файлов с зависимостями: **{deps_count}**\n"
    summary += f"- 📋 Файлов с бизнес-требованиями: **{len(state['business_requirements'])}**\n"
    summary += f"- ⚙️ Файлов с техническими требованиями: **{len(state['requirements'])}**\n"
    summary += f"- 📖 Файлов с описанием проекта: **{len(state['project_descriptions'])}**\n\n"

    return summary


def generate_architecture_section(state: ParserState) -> str:
    """Генерация секции архитектуры"""
    content = ""

    for dir_path, files in state['project_structure'].items():
        content += f"### 📂 {dir_path}\n\n"

        # Группируем файлы по расширениям
        files_by_ext = {}
        for file in files:
            ext = os.path.splitext(file)[1] or 'без расширения'
            if ext not in files_by_ext:
                files_by_ext[ext] = []
            files_by_ext[ext].append(file)

        for ext, ext_files in sorted(files_by_ext.items()):
            content += f"**{ext} файлы ({len(ext_files)}):**\n"
            for file in ext_files[:10]:  # Ограничиваем вывод
                content += f"- `{file}`\n"
            if len(ext_files) > 10:
                content += f"- ... и еще {len(ext_files) - 10} файлов\n"
            content += "\n"

    return content


def generate_file_statistics(state: ParserState) -> str:
    """Генерация статистики файлов"""
    if not state['file_stats']:
        return "Статистика недоступна.\n\n"

    content = "| Тип файла | Количество | Процент |\n"
    content += "|-----------|------------|----------|\n"

    total_files = sum(state['file_stats'].values())

    for ext, count in sorted(state['file_stats'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_files) * 100
        content += f"| `{ext}` | {count} | {percentage:.1f}% |\n"

    content += f"\n**Всего файлов:** {total_files}\n\n"
    return content


def generate_project_descriptions_section(state: ParserState) -> str:
    """Генерация секции описаний проекта"""
    content = ""

    for file_path, description in state['project_descriptions'].items():
        rel_path = os.path.relpath(file_path)
        content += f"### 📄 {rel_path}\n\n"
        content += f"{description}\n\n"
        content += "---\n\n"

    return content


def generate_business_requirements_section(state: ParserState) -> str:
    """Генерация секции бизнес-требований"""
    content = ""

    for file_path, requirements in state['business_requirements'].items():
        rel_path = os.path.relpath(file_path)
        content += f"### 💼 {rel_path}\n\n"

        if len(requirements) > 5000:
            content += f"{requirements[:5000]}\n\n*[Показаны первые 5000 символов из {len(requirements)}]*\n\n"
        else:
            content += f"{requirements}\n\n"

        content += "---\n\n"

    return content


def generate_technical_requirements_section(state: ParserState) -> str:
    """Генерация секции технических требований"""
    content = ""

    for file_path, requirements in state['requirements'].items():
        rel_path = os.path.relpath(file_path)
        content += f"### ⚙️ {rel_path}\n\n"

        if len(requirements) > 3000:
            content += f"{requirements[:3000]}\n\n*[Показаны первые 3000 символов из {len(requirements)}]*\n\n"
        else:
            content += f"{requirements}\n\n"

        content += "---\n\n"

    return content


def generate_dependencies_section(state: ParserState) -> str:
    """Генерация секции зависимостей"""
    content = ""

    if not state['dependencies']:
        return "Зависимости не найдены.\n\n"

    # Общая статистика
    all_libs = set()
    all_functions = set()

    for deps in state['dependencies'].values():
        all_libs.update(deps.get('libraries', []))
        all_functions.update(deps.get('functions', []))

    content += f"**Общая статистика:**\n"
    content += f"- 📚 Уникальных библиотек: {len(all_libs)}\n"
    content += f"- ⚡ Уникальных функций: {len(all_functions)}\n\n"

    if all_libs:
        content += f"**Ключевые библиотеки:** `{', '.join(sorted(list(all_libs))[:15])}`\n\n"

    # Детализация по файлам
    for file_path, deps in state['dependencies'].items():
        rel_path = os.path.relpath(file_path)
        content += f"### 🔧 {rel_path}\n\n"

        if deps['libraries']:
            libs_str = ', '.join([f"`{lib}`" for lib in deps['libraries'][:10]])
            if len(deps['libraries']) > 10:
                libs_str += f" ... и еще {len(deps['libraries']) - 10}"
            content += f"**Библиотеки:** {libs_str}\n\n"

        if deps['functions']:
            funcs_str = ', '.join([f"`{func}`" for func in deps['functions'][:15]])
            if len(deps['functions']) > 15:
                funcs_str += f" ... и еще {len(deps['functions']) - 15}"
            content += f"**Функции:** {funcs_str}\n\n"

        content += "---\n\n"

    return content


def generate_prompts_section(state: ParserState) -> str:
    """Генерация секции промптов"""
    content = ""

    if not state['prompts']:
        return "Промпты не найдены.\n\n"

    total_prompts = sum(len(prompts) for prompts in state['prompts'].values())
    content += f"**Всего найдено промптов ИИ:** {total_prompts}\n\n"

    for file_path, prompts in state['prompts'].items():
        if not prompts:
            continue

        rel_path = os.path.relpath(file_path)
        content += f"### 🎯 {rel_path} ({len(prompts)} промптов)\n\n"

        for i, prompt in enumerate(prompts[:3], 1):  # Показываем только первые 3
            # Обрезаем слишком длинные промпты
            if len(prompt) > 500:
                truncated = prompt[:500] + "..."
            else:
                truncated = prompt

            content += f"**Промпт {i}:**\n"
            content += f"```\n{truncated}\n```\n\n"

        if len(prompts) > 3:
            content += f"*... и еще {len(prompts) - 3} промптов*\n\n"

        content += "---\n\n"

    return content


def generate_empty_files_section(state: ParserState) -> str:
    """Генерация секции пустых файлов"""
    content = "Обнаружены пустые файлы:\n\n"

    for file_path in state['empty_files']:
        rel_path = os.path.relpath(file_path)
        content += f"- `{rel_path}`\n"

    content += f"\n**Всего пустых файлов:** {len(state['empty_files'])}\n\n"
    return content


def generate_recommendations_section(state: ParserState) -> str:
    """Генерация секции рекомендаций"""
    content = "## 💡 Рекомендации\n\n"

    recommendations = []

    # Анализ промптов
    total_prompts = sum(len(prompts) for prompts in state['prompts'].values())
    if total_prompts == 0:
        recommendations.append(
            "🎯 **Промпты:** Не найдено промптов ИИ. Рекомендуется документировать шаблоны взаимодействия с ИИ.")
    elif total_prompts < 5:
        recommendations.append(
            "🎯 **Промпты:** Найдено мало промптов. Рекомендуется расширить документацию ИИ-взаимодействий.")
    else:
        recommendations.append(f"🎯 **Промпты:** Найдено {total_prompts} промптов - хороший уровень документации ИИ.")

    # Анализ документации
    if not state['project_descriptions']:
        recommendations.append(
            "📖 **Документация:** Отсутствуют файлы описания проекта. Рекомендуется создать README или аналогичную документацию.")

    if not state['business_requirements']:
        recommendations.append(
            "💼 **Бизнес-требования:** Не найдены бизнес-требования. Рекомендуется документировать бизнес-логику и требования.")

    # Анализ архитектуры
    if len(state['dependencies']) < len(state['files_list']) * 0.5:
        recommendations.append(
            "🔧 **Архитектура:** Не все файлы проанализированы на зависимости. Возможны проблемы с форматом или доступом к файлам.")

    # Анализ пустых файлов
    if state['empty_files']:
        recommendations.append(
            f"⚠️ **Пустые файлы:** Обнаружено {len(state['empty_files'])} пустых файлов. Рекомендуется их удалить или заполнить содержимым.")

    # Рекомендации по безопасности
    if any('api_key' in str(deps).lower() or 'password' in str(deps).lower() for deps in
           state['dependencies'].values()):
        recommendations.append(
            "🔒 **Безопасность:** Обнаружены потенциальные упоминания ключей API или паролей в коде. Проверьте безопасность данных.")

    for rec in recommendations:
        content += f"- {rec}\n"

    content += "\n"

    # Следующие шаги
    content += "### 🚀 Следующие шаги\n\n"
    content += "1. **Документация:** Улучшить документацию проекта и бизнес-требований\n"
    content += "2. **Промпты:** Стандартизировать и оптимизировать промпты ИИ\n"
    content += "3. **Архитектура:** Провести рефакторинг для улучшения структуры зависимостей\n"
    content += "4. **Тестирование:** Добавить тесты для критических компонентов\n"
    content += "5. **Мониторинг:** Внедрить систему мониторинга работы ИИ-агентов\n\n"

    return content


def build_graph(llm):
    """Построение графа обработки с новыми узлами"""
    graph = StateGraph(ParserState)

    graph.add_node("get_files", get_files_node)
    graph.add_node("analyze_files", analyze_files_node)
    graph.add_node("llm_analysis", lambda state: llm_analysis_node(state, llm))
    graph.add_node("compile_report", compile_report_node)

    graph.set_entry_point("get_files")
    graph.add_edge("get_files", "analyze_files")
    graph.add_edge("analyze_files", "llm_analysis")
    graph.add_edge("llm_analysis", "compile_report")
    graph.add_edge("compile_report", END)

    return graph.compile()


def generate_summary_statistics():
    """Генерация итоговой статистики для логов"""
    try:
        if os.path.exists("analysis_details.json"):
            with open("analysis_details.json", 'r', encoding='utf-8') as f:
                details = json.load(f)

            logger.info("=" * 50)
            logger.info("📊 ИТОГОВАЯ СТАТИСТИКА АНАЛИЗА")
            logger.info("=" * 50)
            logger.info(f"📁 Всего файлов обработано: {details.get('total_files', 0)}")
            logger.info(f"🎯 Найдено промптов ИИ: {details.get('prompts_count', 0)}")
            logger.info(f"🔧 Файлов с зависимостями: {details.get('dependencies_count', 0)}")
            logger.info(f"📋 Файлов с бизнес-требованиями: {details.get('business_requirements_count', 0)}")
            logger.info(f"⚙️ Файлов с техническими требованиями: {details.get('requirements_count', 0)}")
            logger.info(f"📖 Файлов с описанием проекта: {details.get('project_descriptions_count', 0)}")
            logger.info(f"⚠️ Пустых файлов: {details.get('empty_files', 0)}")
            logger.info("=" * 50)

            if details.get('file_stats'):
                logger.info("📈 Распределение файлов по типам:")
                for ext, count in sorted(details['file_stats'].items(), key=lambda x: x[1], reverse=True):
                    logger.info(f"  {ext}: {count} файлов")

            logger.info("=" * 50)
    except Exception as e:
        logger.error(f"Ошибка генерации статистики: {e}")


if __name__ == "__main__":
    try:
        config = LLMConfig.from_env()
        logger.info(f"🔧 Конфигурация LLM: {config.provider.value}, модель: {config.model}")

        llm = create_llm_client(config)
        logger.info("✅ LLM клиент успешно создан")

        app = build_graph(llm)

        # Получаем путь к директории
        directory = input("Введите путь к директории проекта: ").strip()
        if not directory:
            directory = "."

        if not os.path.exists(directory):
            logger.error(f"❌ Директория не существует: {directory}")
            exit(1)

        logger.info(f"Начинаем анализ директории: {directory}")

        # Показываем поддерживаемые типы файлов
        supported = get_supported_extensions()
        logger.info("Поддерживаемые типы файлов:")
        for category, extensions in supported.items():
            logger.info(f"  {category}: {', '.join(extensions)}")

        # Запускаем анализ
        result = app.invoke({"directory_path": directory})

        # Выводим краткую статистику
        print("\n" + "=" * 60)
        print("РЕЗУЛЬТАТЫ АНАЛИЗА")
        print("=" * 60)
        print(f"Обработано файлов: {len(result['files_list'])}")
        print(f"Найдено промптов ИИ: {sum(len(prompts) for prompts in result['prompts'].values())}")
        print(f"Файлов с зависимостями: {len(result['dependencies'])}")
        print(f"Бизнес-требований: {len(result['business_requirements'])}")
        print(f"Технических требований: {len(result['requirements'])}")
        print(f"Описаний проекта: {len(result['project_descriptions'])}")

        # Сохраняем отчет
        report_filename = "parsed_project_enhanced.md"
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(result["final_report"])

        print(f"\nДетальный отчет сохранен в: {report_filename}")
        print(f"LLM анализ сохранен в: llm_analysis.txt")
        print(f"Детали анализа сохранены в: analysis_details.json")

        # Генерируем итоговую статистику
        generate_summary_statistics()

        logger.info("✅ Анализ проекта завершен успешно")

    except KeyboardInterrupt:
        logger.info("❌ Анализ прерван пользователем")
    except ImportError as e:
        logger.error(f"❌ Не установлены необходимые зависимости: {e}")
        print(f"\n🔧 Для установки недостающих библиотек выполните:")
        print("pip install langchain-gigachat PyPDF2 python-docx javalang markdown pandas openpyxl")
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}")
        print(f"❌ Ошибка: {e}")

        # Попытка сохранить хотя бы частичные результаты
        try:
            with open("error_report.txt", "w", encoding="utf-8") as f:
                f.write(f"Ошибка анализа: {str(e)}\n")
                f.write(f"Тип ошибки: {type(e).__name__}\n")
                f.write(f"Время ошибки: {import_datetime.datetime.now()}\n")
            print("🔧 Частичная информация сохранена в error_report.txt")
        except:
            pass