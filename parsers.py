import os
import ast
import re
import astunparse
from typing import List, Dict
import PyPDF2
import logging
from docx import Document
import xml.etree.ElementTree as ET  # Для XML
import markdown  # Для MD (pip install markdown)
# Для Java: используйте javalang (pip install javalang)
from langchain_community.document_loaders import TextLoader
import javalang

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_dependencies(file_path: str) -> Dict[str, List[str]]:
    """Извлечение зависимостей библиотек и функций из файла кода"""
    dependencies = {"libraries": [], "functions": []}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            tree = ast.parse(content)

        # Извлечение импортов
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                for name in getattr(node, 'names', []):
                    dependencies["libraries"].append(name.name)

        # Извлечение определений функций и их вызовов
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                dependencies["functions"].append(node.name)
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                dependencies["functions"].append(node.func.id)

        # Удаление дубликатов
        dependencies["libraries"] = list(set(dependencies["libraries"]))
        dependencies["functions"] = list(set(dependencies["functions"]))

    except Exception as e:
        logger.error(f"Ошибка при анализе зависимостей {file_path}: {e}")
    return dependencies

def load_requirements(file_path: str, batch_size: int = 1000) -> str:
    """Загрузка бизнес-требований из текстовых файлов"""
    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == '.pdf':
            return extract_text_from_pdf(file_path, batch_size)
        elif ext == '.docx':
            return extract_text_from_docx(file_path, batch_size)
        elif ext == '.txt':
            return extract_text_from_txt(file_path, batch_size)
        else:
            loader = TextLoader(file_path, encoding='utf-8')
            docs = loader.load()
            text = "\n".join([doc.page_content for doc in docs])
            return "\n".join([text[i:i + batch_size] for i in range(0, len(text), batch_size)])
    except Exception as e:
        logger.error(f"Ошибка при загрузке требований из {file_path}: {e}")
        return f"Ошибка загрузки: {str(e)}"

def get_project_structure(directory_path: str) -> Dict[str, List[str]]:
    """Получение архитектуры проекта"""
    structure = {}
    for root, dirs, files in os.walk(directory_path):
        if '.git' in dirs:
            dirs.remove('.git')
        relative_path = os.path.relpath(root, directory_path)
        structure[relative_path] = files
    return structure

def extract_text_from_pdf(file_path: str, batch_size: int = 1000) -> str:
    """Извлечение текста из PDF файла с батчевой обработкой"""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                page_text = reader.pages[page_num].extract_text() or ""
                # Обрабатываем текст батчами
                for i in range(0, len(page_text), batch_size):
                    text += page_text[i:i + batch_size] + "\n"
            return text
    except Exception as e:
        logger.error(f"Ошибка при извлечении текста из PDF {file_path}: {e}")
        return f"Ошибка извлечения: {str(e)}"

def extract_text_from_docx(file_path: str, batch_size: int = 1000) -> str:
    """Извлечение текста из DOCX файла с батчевой обработкой"""
    try:
        doc = Document(file_path)
        text = ""
        full_text = "\n".join([para.text for para in doc.paragraphs])
        # Обрабатываем текст батчами
        for i in range(0, len(full_text), batch_size):
            text += full_text[i:i + batch_size] + "\n"
        return text
    except Exception as e:
        logger.error(f"Ошибка при извлечении текста из DOCX {file_path}: {e}")
        return f"Ошибка извлечения: {str(e)}"

def extract_text_from_txt(file_path: str, batch_size: int = 1000) -> str:
    """Извлечение текста из TXT файла с батчевой обработкой"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text = ""
            # Обрабатываем текст батчами
            for i in range(0, len(content), batch_size):
                text += content[i:i + batch_size] + "\n"
            return text
    except Exception as e:
        logger.error(f"Ошибка при извлечении текста из TXT {file_path}: {e}")
        return f"Ошибка извлечения: {str(e)}"

def extract_dependencies(file_path: str) -> Dict[str, List[str]]:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.py':
        # Текущая логика AST для Python
        ...
    elif ext == '.java':
        # Новый парсер для Java (см. ниже)
        return extract_java_dependencies(file_path)
    elif ext == '.js':
        # Для JS: используйте regex или esprima (но без интернета – regex)
        return extract_js_dependencies(file_path)
    elif ext == '.cpp':
        # Для C++: regex для #include и функций
        return extract_cpp_dependencies(file_path)
    return {"libraries": [], "functions": []}

def extract_prompts(file_path: str) -> List[str]:
    """
    Извлечение промптов из файлов кода с обработкой сложных структур и устойчивостью к синтаксическим ошибкам.

    Args:
        file_path (str): Путь к файлу с кодом.

    Returns:
        List[str]: Список найденных промптов.
    """
    prompts = set()  # Используем set для исключения дубликатов
    ext = os.path.splitext(file_path)[1].lower()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Попытка парсинга через AST только для Python файлов
        if ext == '.py':
            try:
                tree = ast.parse(content, filename=file_path)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Str):
                        prompt_text = astunparse.unparse(node).strip().strip('\'"')
                        # Фильтруем строки, которые могут быть промптами (содержат переменные или ключевые слова)
                        if '{' in prompt_text or any(keyword in prompt_text.lower() for keyword in ['задача', 'анализируй', 'ты']):
                            cleaned_prompt = ' '.join(prompt_text.strip().split())
                            if cleaned_prompt:
                                prompts.add(cleaned_prompt)
                                logger.debug(f"AST: Извлечён промпт из {file_path}: {cleaned_prompt[:50]}...")
            except SyntaxError as e:
                logger.warning(f"Синтаксическая ошибка в {file_path}: {e}. Пропускаем AST-парсинг.")
            except Exception as e:
                logger.warning(f"Ошибка AST парсинга в {file_path}: {e}")

        # 2. Регулярное выражение для поиска промптов во всех файлах
        prompt_pattern = r'''
            (?:
                # Вариант 1: ChatPromptTemplate.from_template(...)
                ChatPromptTemplate\.from_template\s*\(
                    (?:
                        # Однострочные строки
                        ["'](.*?)["']
                        |
                        # Многострочные строки
                        (?:f?["']{3}(.*?)(?<!\\)["']{3})
                    )
                \)
                |
                # Вариант 2: PromptTemplate(...)
                PromptTemplate\s*\([^)]*?template\s*=\s*
                    (?:
                        ["'](.*?)["']
                        |
                        (?:f?["']{3}(.*?)(?<!\\)["']{3})
                    )
                \)
                |
                # Вариант 3: Присваивание переменной с "prompt" в имени
                (?:
                    (?:[a-zA-Z_]*prompt[a-zA-Z_]*)\s*=\s*
                    (?:
                        # Однострочные строки
                        ["'](.*?)["']
                        |
                        # Многострочные f-строки или обычные строки
                        (?:f?["']{3}(.*?)(?<!\\)["']{3})
                    )
                )
                |
                # Вариант 4: HumanMessagePromptTemplate(...)
                HumanMessagePromptTemplate\s*\([^)]*?prompt\s*=\s*PromptTemplate\s*\([^)]*?template\s*=\s*
                    (?:
                        ["'](.*?)["']
                        |
                        (?:f?["']{3}(.*?)(?<!\\)["']{3})
                    )
                \)
                |
                # Вариант 5: Промпты в словарях (например, PROMPTS['key'])
                PROMPTS\s*\[\s*['"]([^'"]+)['"]\s*\]\s*=\s*
                    (?:
                        ["'](.*?)["']
                        |
                        (?:f?["']{3}(.*?)(?<!\\)["']{3})
                    )
            )
        '''
        matches = re.findall(prompt_pattern, content, re.VERBOSE | re.DOTALL)

        # Обработка совпадений
        for match in matches:
            for group in match:
                if group and group.strip():
                    cleaned_prompt = ' '.join(group.strip().split())
                    if cleaned_prompt:
                        prompts.add(cleaned_prompt)
                        logger.debug(f"Regex: Извлечён промпт из {file_path}: {cleaned_prompt[:50]}...")
                        break

        # 3. Дополнительные паттерны для Java и других языков
        if ext in ['.java', '.js', '.cpp']:
            # Поиск строковых литералов в других языках
            string_patterns = [
                r'["\'](.*?prompt.*?)["\']',  # строки содержащие "prompt"
                r'["\'](.*?шаблон.*?)["\']',  # строки содержащие "шаблон"
                r'["\'](.*?template.*?)["\']',  # строки содержащие "template"
                r'["\'](.*?сообщение.*?)["\']',  # строки содержащие "сообщение"
                r'["\'](.*?message.*?)["\']',  # строки содержащие "message"
            ]

            for pattern in string_patterns:
                string_matches = re.findall(pattern, content, re.IGNORECASE)
                for match in string_matches:
                    if len(match) > 20:  # Минимальная длина для промпта
                        cleaned_prompt = ' '.join(match.strip().split())
                        if cleaned_prompt:
                            prompts.add(cleaned_prompt)

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
    except UnicodeDecodeError:
        logger.error(f"Ошибка декодирования файла: {file_path}")
    except Exception as e:
        logger.error(f"Ошибка при извлечении промптов из {file_path}: {e}")

    return list(prompts)

def extract_java_dependencies(file_path: str) -> Dict[str, List[str]]:
    """Парсер для Java файлов с использованием javalang"""
    dependencies = {"libraries": [], "functions": []}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Парсим Java код
        tree = javalang.parse.parse(content)

        # Извлекаем импорты
        for import_decl in tree.imports:
            dependencies["libraries"].append(import_decl.path)

        # Извлекаем методы (функции)
        for path, node in tree:
            if isinstance(node, javalang.tree.MethodDeclaration):
                dependencies["functions"].append(node.name)
            # Также можно добавить вызовы методов, если нужно
            elif isinstance(node, javalang.tree.MethodInvocation):
                if hasattr(node, 'member') and node.member:
                    dependencies["functions"].append(node.member)

        # Удаляем дубликаты
        dependencies["libraries"] = list(set(dependencies["libraries"]))
        dependencies["functions"] = list(set(dependencies["functions"]))

    except javalang.parser.JavaSyntaxError as e:
        logger.warning(f"Синтаксическая ошибка в Java файле {file_path}: {e}")
    except Exception as e:
        logger.error(f"Ошибка при анализе Java зависимостей {file_path}: {e}")

    return dependencies

def extract_js_dependencies(file_path: str) -> Dict[str, List[str]]:
    """Regex-парсер для JS (библиотеки: import/from, функции: function/def)"""
    dependencies = {"libraries": [], "functions": []}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Импорты: import ... from 'lib';
    lib_matches = re.findall(r"import\s+.*?\s+from\s+['\"](.*?)['\"]", content)
    dependencies["libraries"] = list(set(lib_matches))
    # Функции: function name() или const name = ()
    func_matches = re.findall(r"(?:function|const|let|var)\s+([a-zA-Z_]\w*)\s*(?:=|\()", content)
    dependencies["functions"] = list(set(func_matches))
    return dependencies

def extract_cpp_dependencies(file_path: str) -> Dict[str, List[str]]:
    """Regex для C++: #include <lib>, функции"""
    dependencies = {"libraries": [], "functions": []}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    lib_matches = re.findall(r"#include\s+[<\"](.*?)[\">]", content)
    dependencies["libraries"] = list(set(lib_matches))
    func_matches = re.findall(r"(\w+)\s*\([^)]*\)\s*\{", content)  # Простой паттерн для функций
    dependencies["functions"] = list(set(func_matches))
    return dependencies

def smart_parse_txt_bpmn(file_path: str, batch_size: int = 1000) -> str:
    """Умный парсинг для TXT и BPMN (low-code). Если XML внутри – парсить как XML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if '<' in content and '>' in content and '<?xml' in content:  # Проверка на XML
            # Low-code: парсим как XML
            root = ET.fromstring(content)
            text = ET.tostring(root, encoding='unicode', method='text')  # Извлекаем текст
            # Или более умно: извлекаем атрибуты/элементы для BPMN (процессы, задачи)
            processes = [elem.attrib.get('name', '') for elem in root.findall('.//{*}process')]
            tasks = [elem.attrib.get('name', '') for elem in root.findall('.//{*}task')]
            text += f"\nBPMN Processes: {', '.join(processes)}\nTasks: {', '.join(tasks)}"
        else:
            text = content  # Обычный TXT
        # Батчевая обработка
        batched = ""
        for i in range(0, len(text), batch_size):
            batched += text[i:i + batch_size] + "\n"
        return batched
    except Exception as e:
        logging.error(f"Ошибка парсинга TXT/BPMN {file_path}: {e}")
        return f"Ошибка: {str(e)}"

def parse_md(file_path: str, batch_size: int = 1000) -> str:
    """Отдельный парсер для MD: конверт в HTML или извлекай структуру."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        # Используем markdown lib для конвертации в HTML (или извлечения)
        html = markdown.markdown(md_content)
        # Или структура: извлекаем заголовки
        headers = re.findall(r'^#{1,6}\s+(.*)', md_content, re.MULTILINE)
        text = f"MD Headers: {', '.join(headers)}\n\n{html}"
        # Батчевая
        batched = ""
        for i in range(0, len(text), batch_size):
            batched += text[i:i + batch_size] + "\n"
        return batched
    except Exception as e:
        logging.error(f"Ошибка парсинга MD {file_path}: {e}")
        return f"Ошибка: {str(e)}"