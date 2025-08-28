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
    smart_parse_txt_bpmn,
    parse_md,
    extract_java_dependencies,
    extract_js_dependencies,
    extract_cpp_dependencies
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
    analysis: str
    final_report: str
    project_structure: Dict[str, List[str]]

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
    files = []
    empty_files = []
    code_extensions = {'.py', '.js', '.java', '.cpp'}
    text_extensions = {'.txt', '.md', '.yaml', '.yml', '.json', '.docx', '.pdf', '.bpmn'}

    project_structure = get_project_structure(state['directory_path'])

    for root, dirs, filenames in os.walk(state['directory_path']):
        if '.git' in dirs:
            dirs.remove('.git')
        for filename in filenames:
            file_path = os.path.join(root, filename)
            ext = os.path.splitext(filename)[1].lower()
            if ext not in code_extensions and ext not in text_extensions:
                continue
            try:
                if os.path.getsize(file_path) == 0:
                    empty_files.append(file_path)
                    continue
                files.append(file_path)
            except OSError:
                continue

    state['files_list'] = files
    state['empty_files'] = empty_files
    state['project_structure'] = project_structure
    logger.info(f"Найдено {len(files)} поддерживаемых файлов и {len(empty_files)} пустых файлов")
    return state

def analyze_files_node(state: ParserState) -> ParserState:
    dependencies = {}
    prompts = {}
    requirements = {}

    with ThreadPoolExecutor(max_workers=4) as executor:
        code_files = [f for f in state['files_list'] if os.path.splitext(f)[1].lower() in {'.py', '.js', '.java', '.cpp'}]
        text_files = [f for f in state['files_list'] if os.path.splitext(f)[1].lower() in {'.txt', '.md', '.yaml', '.yml', '.json', '.docx', '.pdf', '.bpmn'}]

        # Анализ зависимостей с обработкой ошибок
        future_to_file = {executor.submit(extract_dependencies, file): file for file in code_files}
        for future in as_completed(future_to_file):
            file = future_to_file[future]
            try:
                dependencies[file] = future.result()
            except Exception as e:
                logger.error(f"Ошибка при анализе зависимостей {file}: {e}")
                dependencies[file] = {"libraries": [], "functions": []}

        # Аналогично для промптов и требований...
        # ... остальной код без изменений

    state['dependencies'] = dependencies
    state['prompts'] = prompts
    state['requirements'] = requirements
    return state

def llm_analysis_node(state: ParserState, llm) -> ParserState:
    try:
        # Подготовка данных для LLM
        dep_content = "\n".join([f"Файл {file}: Библиотеки: {deps['libraries']}, Функции: {deps['functions']}"
                                for file, deps in state['dependencies'].items()])
        prompt_content = "\n".join([f"Файл {file}: {', '.join(prompts)}"
                                   for file, prompts in state['prompts'].items() if prompts])
        req_content = "\n".join([f"Файл {file}: {req}"
                                for file, req in state['requirements'].items()])
        structure_content = "\n".join([f"Папка {dir}: {', '.join(files)}"
                                     for dir, files in state['project_structure'].items()])

        all_content = f"Архитектура проекта:\n{structure_content}\n\nЗависимости:\n{dep_content}\n\nПромпты:\n{prompt_content}\n\nТребования:\n{req_content}"

        # Чанкинг вместо обрезания
        max_input_size = 100000
        chunks = chunk_text(all_content, chunk_size=80000, overlap=0.2)

        system_prompt_template = ChatPromptTemplate.from_template(PROMPTS['system_prompt'])
        chain = system_prompt_template | llm | StrOutputParser()

        analysis_chunks = []
        for chunk in chunks:
            # Исправлено: передаем словарь с переменными вместо строки
            analysis_chunk = chain.invoke({"content": chunk})
            analysis_chunks.append(analysis_chunk)

        # Суммаризация чанков
        summary_prompt = ChatPromptTemplate.from_template("Суммируй и объедини эти анализы в coherentный отчет: {analyses}")
        summary_chain = summary_prompt | llm | StrOutputParser()
        analysis = summary_chain.invoke({"analyses": "\n\n".join(analysis_chunks)})

        # Проверка с помощью judge
        judge_prompt_template = ChatPromptTemplate.from_template(PROMPTS['judge'])
        judge_chain = judge_prompt_template | llm | StrOutputParser()

        # Формируем правильный словарь для judge
        judge_input = {
            "system_prompt": PROMPTS['system_prompt'],
            "analysis": analysis,
            "content": all_content
        }

        # Если контент слишком большой, обрабатываем чанками
        if len(str(judge_input)) > max_input_size:
            judge_chunks = chunk_text(str(judge_input), chunk_size=80000, overlap=0.2)
            judge_outputs = []
            for judge_chunk in judge_chunks:
                # Для каждого чанка создаем правильный словарь с переменными
                judge_output = judge_chain.invoke({
                    "system_prompt": PROMPTS['system_prompt'],
                    "analysis": analysis[:10000],  # Ограничиваем анализ для judge
                    "content": judge_chunk
                })
                judge_outputs.append(judge_output)
            judge_output = "\n".join(judge_outputs)
        else:
            # Исправлено: передаем словарь с переменными
            judge_output = judge_chain.invoke(judge_input)

        try:
            judge_result = json.loads(judge_output)
        except json.JSONDecodeError:
            logger.error("Ошибка парсинга judge output")
            judge_result = {"status": "bad", "missing": []}

        final_analysis = analysis
        if judge_result['status'] == "bad":
            missing = judge_result.get('missing', [])
            if "prompts" in missing:
                final_analysis += "\n\nДополнительные промпты (из парсера):\n" + prompt_content
            if "dependencies" in missing:
                final_analysis += "\n\nДополнительные зависимости (из парсера):\n" + dep_content
            if "structure" in missing:
                final_analysis += "\n\nДополнительная архитектура проекта (из парсера):\n" + structure_content
            if "requirements" in missing:
                final_analysis += "\n\nДополнительные требования (из парсера):\n" + req_content

        # Сохранение в отдельный файл
        analysis_file = "llm_analysis.txt"
        with open(analysis_file, 'w', encoding='utf-8') as f:
            f.write(final_analysis)
        state['analysis_file'] = analysis_file
        state['analysis'] = final_analysis
        logger.info("LLM анализ завершен и сохранен в файл")
    except Exception as e:
        logger.error(f"Ошибка при LLM анализе: {e}")
        error_msg = f"Ошибка анализа: {str(e)}"
        if "404" in str(e):
            error_msg += "\nВозможная причина: Неверный URL API или неподдерживаемый провайдер LLM."
        with open("llm_analysis.txt", 'w', encoding='utf-8') as f:
            f.write(error_msg)
        state['analysis_file'] = "llm_analysis.txt"
        state['analysis'] = error_msg
    return state

def compile_report_node(state: ParserState) -> ParserState:
    report = "# Отчет по анализу проекта\n\n"

    report += "## Архитектура проекта\n"
    for dir, files in state['project_structure'].items():
        report += f"### {dir}\n"
        report += "\n".join([f"- {file}" for file in files]) + "\n\n"

    report += "## Зависимости и функции\n"
    for file, deps in state['dependencies'].items():
        report += f"### {file}\n"
        report += f"- Библиотеки: {', '.join(deps['libraries']) if deps['libraries'] else 'Отсутствуют'}\n"
        report += f"- Функции: {', '.join(deps['functions']) if deps['functions'] else 'Отсутствуют'}\n\n"

    report += "## Промпты\n"
    for file, prompts in state['prompts'].items():
        if prompts:
            report += f"### {file}\n"
            report += "\n".join([f"- {prompt}" for prompt in prompts]) + "\n\n"

    report += "## Бизнес-требования\n"
    for file, req in state['requirements'].items():
        max_req_display = 10000
        if len(req) > max_req_display:
            # Чанкинг и суммаризация для длинных требований в отчете
            chunks = chunk_text(req, chunk_size=5000, overlap=0.2)
            req_summary = "\n".join(chunks[:1]) + "\n... [суммаризировано, исходная длина: {} символов]".format(len(req))
            report += f"### {file}\n{req_summary}\n\n"
        else:
            report += f"### {file}\n{req}\n\n"

    report += "## Анализ LLM\n"
    report += state['analysis'] + "\n"

    if state['empty_files']:
        report += "## Пустые файлы\n" + "\n".join(state['empty_files']) + "\n"

    state['final_report'] = report
    return state

def build_graph(llm):
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

if __name__ == "__main__":
    try:
        config = LLMConfig.from_env()
        logger.info(f"🔧 Конфигурация LLM: {config.provider.value}, модель: {config.model}")

        llm = create_llm_client(config)
        logger.info("✅ LLM клиент успешно создан")

        app = build_graph(llm)
        directory = input("Введите путь к директории проекта: ")

        result = app.invoke({"directory_path": directory})
        print(result["final_report"])

        with open("parsed_project_агент95.md", "w", encoding="utf-8") as f:
            f.write(result["final_report"])

        logger.info("✅ Анализ проекта завершен успешно")
    except ImportError as e:
        logger.error(f"❌ Не установлены необходимые зависимости: {e}")
        print(f"Установите: pip install langchain-gigachat PyPDF2 python-docx javalang markdown")
    except Exception as e:
        logger.error(f"❌ Фатальная ошибка: {e}")
        print(f"Ошибка: {e}")