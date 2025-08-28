"""
Дополнительные утилиты для обработки файлов различных форматов
"""

import os
import re
import json
import logging
from typing import Dict, List, Tuple, Optional, Any
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)

class FileAnalyzer:
    """Класс для анализа файлов и извлечения метаданных"""
    
    def __init__(self):
        self.supported_formats = {
            'text': ['.txt', '.md', '.rst'],
            'document': ['.docx', '.pdf', '.rtf'],
            'data': ['.csv', '.xlsx', '.xls', '.json', '.yaml', '.yml'],
            'code': ['.py', '.js', '.ts', '.java', '.cpp', '.c', '.h'],
            'config': ['.ini', '.conf', '.config', '.env', '.toml'],
            'markup': ['.xml', '.html', '.htm', '.bpmn']
        }
    
    def analyze_file_content(self, file_path: str) -> Dict[str, Any]:
        """Анализ содержимого файла и извлечение метаданных"""
        try:
            file_info = {
                'path': file_path,
                'name': os.path.basename(file_path),
                'extension': os.path.splitext(file_path)[1].lower(),
                'size': os.path.getsize(file_path),
                'type': self._determine_file_type(file_path),
                'encoding': self._detect_encoding(file_path),
                'content_indicators': self._analyze_content_indicators(file_path),
                'potential_ai_content': self._detect_ai_content(file_path),
                'business_relevance': self._assess_business_relevance(file_path),
                'technical_complexity': self._assess_technical_complexity(file_path)
            }
            return file_info
        except Exception as e:
            logger.error(f"Ошибка анализа файла {file_path}: {e}")
            return {'path': file_path, 'error': str(e)}
    
    def _determine_file_type(self, file_path: str) -> str:
        """Определение типа файла"""
        ext = os.path.splitext(file_path)[1].lower()
        for file_type, extensions in self.supported_formats.items():
            if ext in extensions:
                return file_type
        return 'unknown'
    
    def _detect_encoding(self, file_path: str) -> str:
        """Определение кодировки файла"""
        try:
            import chardet
            with open(file_path, 'rb') as f:
                raw_data = f.read(10000)  # Читаем первые 10KB
                result = chardet.detect(raw_data)
                return result.get('encoding', 'unknown')
        except ImportError:
            return 'utf-8'  # Предполагаем UTF-8 по умолчанию
        except Exception:
            return 'unknown'
    
    def _analyze_content_indicators(self, file_path: str) -> Dict[str, bool]:
        """Анализ индикаторов содержимого"""
        indicators = {
            'contains_prompts': False,
            'contains_business_logic': False,
            'contains_api_keys': False,
            'contains_configurations': False,
            'contains_data_structures': False,
            'contains_documentation': False
        }
        
        try:
            # Для текстовых файлов анализируем содержимое
            if self._is_text_file(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(5000).lower()  # Читаем первые 5KB
                    
                    # Ищем промпты
                    prompt_keywords = ['prompt', 'промпт', 'template', 'шаблон', 'system', 'user', 'assistant']
                    indicators['contains_prompts'] = any(keyword in content for keyword in prompt_keywords)
                    
                    # Ищем бизнес-логику
                    business_keywords = ['требования', 'business', 'process', 'workflow', 'пользователь']
                    indicators['contains_business_logic'] = any(keyword in content for keyword in business_keywords)
                    
                    # Ищем API ключи
                    api_patterns = ['api_key', 'secret', 'token', 'password', 'credential']
                    indicators['contains_api_keys'] = any(pattern in content for pattern in api_patterns)
                    
                    # Ищем конфигурации
                    config_keywords = ['config', 'setting', 'parameter', 'environment']
                    indicators['contains_configurations'] = any(keyword in content for keyword in config_keywords)
                    
                    # Ищем документацию
                    doc_keywords = ['readme', 'documentation', 'описание', 'manual', 'guide']
                    indicators['contains_documentation'] = any(keyword in content for keyword in doc_keywords)
                    
        except Exception as e:
            logger.warning(f"Не удалось проанализировать содержимое {file_path}: {e}")
        
        return indicators
    
    def _detect_ai_content(self, file_path: str) -> Dict[str, Any]:
        """Обнаружение ИИ-специфичного контента"""
        ai_indicators = {
            'has_llm_interactions': False,
            'has_prompt_templates': False,
            'has_ai_workflows': False,
            'confidence_level': 0.0,
            'detected_ai_frameworks': []
        }
        
        try:
            if self._is_text_file(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(10000).lower()
                    
                    # Паттерны для поиска ИИ-контента
                    llm_patterns = [
                        r'openai', r'chatgpt', r'gpt-[0-9]', r'claude', r'anthropic',
                        r'langchain', r'llama', r'gemini', r'palm', r'бард'
                    ]
                    
                    prompt_patterns = [
                        r'chatprompttemplate', r'prompttemplate', r'system.*prompt',
                        r'user.*prompt', r'assistant.*prompt', r'промпт.*шаблон'
                    ]
                    
                    workflow_patterns = [
                        r'chain\.invoke', r'agent\.run', r'crew\.kickoff',
                        r'workflow', r'pipeline', r'orchestrat'
                    ]
                    
                    # Подсчитываем совпадения
                    llm_matches = sum(1 for pattern in llm_patterns if re.search(pattern, content))
                    prompt_matches = sum(1 for pattern in prompt_patterns if re.search(pattern, content))
                    workflow_matches = sum(1 for pattern in workflow_patterns if re.search(pattern, content))
                    
                    ai_indicators['has_llm_interactions'] = llm_matches > 0
                    ai_indicators['has_prompt_templates'] = prompt_matches > 0
                    ai_indicators['has_ai_workflows'] = workflow_matches > 0
                    
                    # Определяем уровень уверенности
                    total_matches = llm_matches + prompt_matches + workflow_matches
                    ai_indicators['confidence_level'] = min(total_matches / 10.0, 1.0)
                    
                    # Определяем используемые фреймворки
                    frameworks = []
                    if 'langchain' in content:
                        frameworks.append('LangChain')
                    if 'crewai' in content or 'crew' in content:
                        frameworks.append('CrewAI')
                    if 'openai' in content:
                        frameworks.append('OpenAI')
                    if 'anthropic' in content or 'claude' in content:
                        frameworks.append('Anthropic')
                    
                    ai_indicators['detected_ai_frameworks'] = frameworks
                    
        except Exception as e:
            logger.warning(f"Ошибка анализа ИИ-контента в {file_path}: {e}")
        
        return ai_indicators
    
    def _assess_business_relevance(self, file_path: str) -> float:
        """Оценка бизнес-релевантности файла"""
        filename = os.path.basename(file_path).lower()
        
        # Высокая релевантность
        high_relevance_indicators = [
            'requirements', 'требования', 'business', 'бизнес',
            'process', 'процесс', 'workflow', 'specification',
            'спецификация', 'use_case', 'пользовательские_истории'
        ]
        
        # Средняя релевантность
        medium_relevance_indicators = [
            'config', 'settings', 'readme', 'documentation',
            'описание', 'manual', 'guide', 'api'
        ]
        
        # Низкая релевантность
        low_relevance_indicators = [
            'test', 'тест', 'debug', 'temp', 'tmp', 'cache',
            'log', 'backup', '__pycache__'
        ]
        
        for indicator in high_relevance_indicators:
            if indicator in filename:
                return 0.9
        
        for indicator in medium_relevance_indicators:
            if indicator in filename:
                return 0.6
        
        for indicator in low_relevance_indicators:
            if indicator in filename:
                return 0.2
        
        # Анализируем содержимое для более точной оценки
        try:
            if self._is_text_file(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(2000).lower()
                    
                    business_keywords_count = sum(1 for keyword in [
                        'бизнес', 'business', 'требования', 'requirements',
                        'процесс', 'process', 'пользователь', 'user',
                        'клиент', 'client', 'заказчик', 'customer'
                    ] if keyword in content)
                    
                    if business_keywords_count >= 3:
                        return 0.8
                    elif business_keywords_count >= 1:
                        return 0.5
        except Exception:
            pass
        
        return 0.3  # Средняя релевантность по умолчанию
    
    def _assess_technical_complexity(self, file_path: str) -> float:
        """Оценка технической сложности файла"""
        ext = os.path.splitext(file_path)[1].lower()
        
        # Высокая сложность
        if ext in ['.py', '.java', '.cpp', '.c', '.js', '.ts']:
            complexity = 0.8
        # Средняя сложность
        elif ext in ['.json', '.yaml', '.yml', '.xml', '.sql']:
            complexity = 0.6
        # Низкая сложность
        elif ext in ['.txt', '.md', '.csv']:
            complexity = 0.3
        else:
            complexity = 0.5
        
        # Дополнительный анализ для кодовых файлов
        try:
            if ext in ['.py', '.js', '.java'] and self._is_text_file(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()[:100]  # Первые 100 строк
                    
                    complexity_indicators = 0
                    for line in lines:
                        line_lower = line.lower().strip()
                        # Ищем индикаторы сложности
                        if any(keyword in line_lower for keyword in [
                            'class ', 'async ', 'await ', 'lambda',
                            'decorator', 'inheritance', 'polymorphism',
                            'threading', 'multiprocessing', 'asyncio'
                        ]):
                            complexity_indicators += 1
                    
                    # Корректируем сложность на основе найденных индикаторов
                    complexity = min(complexity + (complexity_indicators * 0.05), 1.0)
                    
        except Exception:
            pass
        
        return complexity
    
    def _is_text_file(self, file_path: str) -> bool:
        """Проверка, является ли файл текстовым"""
        text_extensions = [
            '.txt', '.md', '.py', '.js', '.ts', '.java', '.cpp', '.c', '.h',
            '.json', '.yaml', '.yml', '.xml', '.html', '.css', '.sql',
            '.ini', '.conf', '.config', '.env', '.toml', '.rst'
        ]
        ext = os.path.splitext(file_path)[1].lower()
        return ext in text_extensions

class ContentExtractor:
    """Класс для извлечения специфического контента из файлов"""
    
    @staticmethod
    def extract_ai_prompts_advanced(file_path: str) -> List[Dict[str, Any]]:
        """Расширенное извлечение промптов с метаданными"""
        prompts = []
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Различные паттерны для поиска промптов
            patterns = [
                # ChatPromptTemplate паттерны
                {
                    'pattern': r'ChatPromptTemplate\.from_template\s*\(\s*["\']([^"\']+)["\']',
                    'type': 'ChatPromptTemplate',
                    'framework': 'LangChain'
                },
                # PromptTemplate паттерны  
                {
                    'pattern': r'PromptTemplate\s*\([^)]*?template\s*=\s*["\']([^"\']+)["\']',
                    'type': 'PromptTemplate', 
                    'framework': 'LangChain'
                },
                # Системные промпты
                {
                    'pattern': r'system.*prompt.*["\']([^"\']{50,})["\']',
                    'type': 'SystemPrompt',
                    'framework': 'Generic'
                },
                # Пользовательские промпты
                {
                    'pattern': r'user.*prompt.*["\']([^"\']{30,})["\']',
                    'type': 'UserPrompt',
                    'framework': 'Generic'
                },
                # Многострочные промпты
                {
                    'pattern': r'["\'{3}](.*?(?:analyze|анализ|задача|instruction).*?)["\'{3}]',
                    'type': 'MultilinePrompt',
                    'framework': 'Generic'
                }
            ]
            
            for pattern_info in patterns:
                matches = re.findall(pattern_info['pattern'], content, re.IGNORECASE | re.DOTALL)
                for match in matches:
                    prompt_data = {
                        'text': match.strip(),
                        'type': pattern_info['type'],
                        'framework': pattern_info['framework'],
                        'file_path': file_path,
                        'length': len(match.strip()),
                        'language': 'ru' if any(ru_word in match.lower() for ru_word in ['ты', 'анализ', 'задача', 'создай']) else 'en',
                        'complexity': ContentExtractor._assess_prompt_complexity(match)
                    }
                    prompts.append(prompt_data)
            
        except Exception as e:
            logger.error(f"Ошибка извлечения промптов из {file_path}: {e}")
        
        return prompts
    
    @staticmethod
    def _assess_prompt_complexity(prompt_text: str) -> str:
        """Оценка сложности промпта"""
        length = len(prompt_text)
        
        # Подсчитываем индикаторы сложности
        complexity_indicators = 0
        
        # Структурные элементы
        if '{' in prompt_text and '}' in prompt_text:
            complexity_indicators += 1  # Переменные
        
        if any(word in prompt_text.lower() for word in ['step by step', 'пошагово', 'analyze', 'анализируй']):
            complexity_indicators += 1  # Инструкции
        
        if any(word in prompt_text.lower() for word in ['format:', 'формат:', 'example:', 'пример:']):
            complexity_indicators += 1  # Форматирование
        
        if prompt_text.count('\n') > 5:
            complexity_indicators += 1  # Многострочность
        
        # Определяем сложность
        if length < 100:
            return 'simple'
        elif length < 500 and complexity_indicators <= 1:
            return 'medium'
        elif length < 1000 and complexity_indicators <= 2:
            return 'complex'
        else:
            return 'advanced'
    
    @staticmethod
    def extract_business_entities(file_path: str) -> Dict[str, List[str]]:
        """Извлечение бизнес-сущностей из документов"""
        entities = {
            'roles': [],
            'processes': [],
            'requirements': [],
            'constraints': [],
            'stakeholders': [],
            'systems': [],
            'goals': []
        }
        
        try:
            # Определяем тип файла и соответствующий метод извлечения
            ext = os.path.splitext(file_path)[1].lower()
            
            if ext == '.csv':
                entities.update(ContentExtractor._extract_from_csv(file_path))
            elif ext in ['.xlsx', '.xls']:
                entities.update(ContentExtractor._extract_from_excel(file_path))
            elif ext in ['.txt', '.md']:
                entities.update(ContentExtractor._extract_from_text(file_path))
            
        except Exception as e:
            logger.error(f"Ошибка извлечения бизнес-сущностей из {file_path}: {e}")
        
        return entities
    
    @staticmethod
    def _extract_from_csv(file_path: str) -> Dict[str, List[str]]:
        """Извлечение сущностей из CSV"""
        entities = {'roles': [], 'processes': [], 'requirements': []}
        
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
            
            # Ищем колонки с ролями
            role_columns = [col for col in df.columns if any(keyword in col.lower() 
                          for keyword in ['роль', 'role', 'должность', 'position'])]
            
            for col in role_columns:
                entities['roles'].extend(df[col].dropna().astype(str).tolist())
            
            # Ищем процессы
            process_columns = [col for col in df.columns if any(keyword in col.lower()
                             for keyword in ['процесс', 'process', 'workflow', 'задача', 'task'])]
            
            for col in process_columns:
                entities['processes'].extend(df[col].dropna().astype(str).tolist())
            
            # Ищем требования
            req_columns = [col for col in df.columns if any(keyword in col.lower()
                          for keyword in ['требование', 'requirement', 'spec', 'спецификация'])]
            
            for col in req_columns:
                entities['requirements'].extend(df[col].dropna().astype(str).tolist())
                
        except Exception as e:
            logger.warning(f"Ошибка обработки CSV {file_path}: {e}")
        
        return entities
    
    @staticmethod
    def _extract_from_excel(file_path: str) -> Dict[str, List[str]]:
        """Извлечение сущностей из Excel"""
        entities = {'roles': [], 'processes': [], 'requirements': []}
        
        try:
            xl_file = pd.ExcelFile(file_path)
            
            for sheet_name in xl_file.sheet_names:
                df = pd.read_excel(file_path, sheet_name=sheet_name)
                
                # Применяем ту же логику, что и для CSV
                sheet_entities = ContentExtractor._extract_from_csv_dataframe(df)
                
                for key in entities:
                    entities[key].extend(sheet_entities.get(key, []))
                    
        except Exception as e:
            logger.warning(f"Ошибка обработки Excel {file_path}: {e}")
        
        return entities
    
    @staticmethod
    def _extract_from_csv_dataframe(df: pd.DataFrame) -> Dict[str, List[str]]:
        """Вспомогательный метод для извлечения из DataFrame"""
        entities = {'roles': [], 'processes': [], 'requirements': []}
        
        # Роли
        role_columns = [col for col in df.columns if any(keyword in str(col).lower() 
                      for keyword in ['роль', 'role', 'должность', 'position'])]
        
        for col in role_columns:
            entities['roles'].extend(df[col].dropna().astype(str).tolist())
        
        # Процессы
        process_columns = [col for col in df.columns if any(keyword in str(col).lower()
                         for keyword in ['процесс', 'process', 'workflow', 'задача', 'task'])]
        
        for col in process_columns:
            entities['processes'].extend(df[col].dropna().astype(str).tolist())
        
        # Требования
        req_columns = [col for col in df.columns if any(keyword in str(col).lower()
                      for keyword in ['требование', 'requirement', 'spec', 'спецификация'])]
        
        for col in req_columns:
            entities['requirements'].extend(df[col].dropna().astype(str).tolist())
        
        return entities
    
    @staticmethod
    def _extract_from_text(file_path: str) -> Dict[str, List[str]]:
        """Извлечение сущностей из текстовых файлов"""
        entities = {'roles': [], 'processes': [], 'requirements': [], 'goals': [], 'constraints': []}
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                line_lower = line.lower()
                
                # Ищем роли
                if any(keyword in line_lower for keyword in ['роль:', 'role:', 'должность:', 'агент', 'пользователь']):
                    entities['roles'].append(line)
                
                # Ищем процессы
                elif any(keyword in line_lower for keyword in ['процесс:', 'process:', 'workflow:', 'алгоритм']):
                    entities['processes'].append(line)
                
                # Ищем требования
                elif any(keyword in line_lower for keyword in ['требование:', 'requirement:', 'должен', 'необходимо']):
                    entities['requirements'].append(line)
                
                # Ищем цели
                elif any(keyword in line_lower for keyword in ['цель:', 'goal:', 'задача:', 'objective:']):
                    entities['goals'].append(line)
                
                # Ищем ограничения
                elif any(keyword in line_lower for keyword in ['ограничение:', 'constraint:', 'нельзя', 'запрещено']):
                    entities['constraints'].append(line)
                    
        except Exception as e:
            logger.warning(f"Ошибка обработки текста {file_path}: {e}")
        
        return entities

class ReportGenerator:
    """Класс для генерации отчетов на основе анализа файлов"""
    
    @staticmethod
    def generate_file_analysis_report(file_analyses: List[Dict]) -> str:
        """Генерация отчета по анализу файлов"""
        report = "# 📊 Отчет по анализу файлов проекта\n\n"
        
        # Общая статистика
        total_files = len(file_analyses)
        ai_files = sum(1 for fa in file_analyses 
                      if fa.get('potential_ai_content', {}).get('confidence_level', 0) > 0.3)
        business_files = sum(1 for fa in file_analyses 
                           if fa.get('business_relevance', 0) > 0.7)
        
        report += f"## 📈 Общая статистика\n\n"
        report += f"- **Всего файлов проанализировано:** {total_files}\n"
        report += f"- **Файлов с ИИ-контентом:** {ai_files}\n"  
        report += f"- **Файлов с высокой бизнес-релевантностью:** {business_files}\n\n"
        
        # Детализация по типам файлов
        file_types = {}
        for fa in file_analyses:
            file_type = fa.get('type', 'unknown')
            file_types[file_type] = file_types.get(file_type, 0) + 1
        
        report += f"## 📁 Распределение по типам файлов\n\n"
        for file_type, count in sorted(file_types.items(), key=lambda x: x[1], reverse=True):
            report += f"- **{file_type}:** {count} файлов\n"
        
        report += "\n"
        
        # ИИ-контент анализ
        if ai_files > 0:
            report += f"## 🤖 Анализ ИИ-контента\n\n"
            
            ai_frameworks = {}
            for fa in file_analyses:
                frameworks = fa.get('potential_ai_content', {}).get('detected_ai_frameworks', [])
                for framework in frameworks:
                    ai_frameworks[framework] = ai_frameworks.get(framework, 0) + 1
            
            if ai_frameworks:
                report += f"**Обнаруженные ИИ-фреймворки:**\n"
                for framework, count in sorted(ai_frameworks.items(), key=lambda x: x[1], reverse=True):
                    report += f"- {framework}: {count} файлов\n"
            
            report += "\n"
        
        # Топ файлы по категориям
        report += f"## 🏆 Топ файлы по категориям\n\n"
        
        # Топ по ИИ-контенту
        ai_sorted = sorted([fa for fa in file_analyses 
                           if fa.get('potential_ai_content', {}).get('confidence_level', 0) > 0],
                          key=lambda x: x.get('potential_ai_content', {}).get('confidence_level', 0),
                          reverse=True)[:5]
        
        if ai_sorted:
            report += f"### 🎯 Топ файлы с ИИ-контентом\n\n"
            for i, fa in enumerate(ai_sorted, 1):
                confidence = fa.get('potential_ai_content', {}).get('confidence_level', 0)
                report += f"{i}. **{fa['name']}** (уверенность: {confidence:.2f})\n"
            report += "\n"
        
        # Топ по бизнес-релевантности
        business_sorted = sorted(file_analyses,
                               key=lambda x: x.get('business_relevance', 0),
                               reverse=True)[:5]
        
        report += f"### 💼 Топ файлы по бизнес-релевантности\n\n"
        for i, fa in enumerate(business_sorted, 1):
            relevance = fa.get('business_relevance', 0)
            report += f"{i}. **{fa['name']}** (релевантность: {relevance:.2f})\n"
        
        return report
    
    @staticmethod
    def generate_prompt_analysis_report(prompts_data: List[Dict]) -> str:
        """Генерация отчета по анализу промптов"""
        if not prompts_data:
            return "# 🎯 Промпты не найдены\n\nВ проекте не обнаружено промптов ИИ.\n"
        
        report = "# 🎯 Детальный анализ промптов ИИ\n\n"
        
        # Статистика промптов
        total_prompts = len(prompts_data)
        avg_length = sum(p['length'] for p in prompts_data) / total_prompts
        
        # Группировка по типам
        types_stats = {}
        complexity_stats = {}
        framework_stats = {}
        language_stats = {}
        
        for prompt in prompts_data:
            # По типам
            ptype = prompt.get('type', 'Unknown')
            types_stats[ptype] = types_stats.get(ptype, 0) + 1
            
            # По сложности
            complexity = prompt.get('complexity', 'unknown')
            complexity_stats[complexity] = complexity_stats.get(complexity, 0) + 1
            
            # По фреймворкам
            framework = prompt.get('framework', 'Unknown')
            framework_stats[framework] = framework_stats.get(framework, 0) + 1
            
            # По языкам
            language = prompt.get('language', 'unknown')
            language_stats[language] = language_stats.get(language, 0) + 1
        
        report += f"## 📊 Общая статистика промптов\n\n"
        report += f"- **Всего промптов:** {total_prompts}\n"
        report += f"- **Средняя длина:** {avg_length:.0f} символов\n"
        report += f"- **Уникальных файлов с промптами:** {len(set(p['file_path'] for p in prompts_data))}\n\n"
        
        # Статистика по типам
        report += f"### 🏷️ Распределение по типам\n\n"
        for ptype, count in sorted(types_stats.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_prompts) * 100
            report += f"- **{ptype}:** {count} ({percentage:.1f}%)\n"
        report += "\n"
        
        # Статистика по сложности
        report += f"### 🧩 Распределение по сложности\n\n"
        for complexity, count in sorted(complexity_stats.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_prompts) * 100
            report += f"- **{complexity}:** {count} ({percentage:.1f}%)\n"
        report += "\n"
        
        # Статистика по фреймворкам
        if len(framework_stats) > 1:
            report += f"### 🛠️ Используемые фреймворки\n\n"
            for framework, count in sorted(framework_stats.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / total_prompts) * 100
                report += f"- **{framework}:** {count} ({percentage:.1f}%)\n"
            report += "\n"
        
        # Примеры промптов по категориям
        report += f"## 📝 Примеры промптов по категориям\n\n"
        
        for ptype in types_stats:
            type_prompts = [p for p in prompts_data if p.get('type') == ptype]
            if type_prompts:
                report += f"### {ptype}\n\n"
                
                # Берем самый длинный промпт этого типа как пример
                example_prompt = max(type_prompts, key=lambda x: x['length'])
                
                prompt_text = example_prompt['text']
                if len(prompt_text) > 500:
                    prompt_text = prompt_text[:500] + "..."
                
                report += f"**Файл:** `{os.path.basename(example_prompt['file_path'])}`\n"
                report += f"**Длина:** {example_prompt['length']} символов\n"
                report += f"**Сложность:** {example_prompt.get('complexity', 'unknown')}\n\n"
                report += f"```\n{prompt_text}\n```\n\n"
        
        return report