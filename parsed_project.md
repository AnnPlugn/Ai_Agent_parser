# Отчет по анализу проекта

## Архитектура проекта
### .
- .gitignore
- agent_config.json
- agent_params.xlsx
- I AM AGENT.xlsx
- improved_message_handler.py
- main.py
- project_structure.txt
- README.md
- requirements.txt
- run_orchestrator_tests.py
- run_telegram_bot2.py
- run_workflow.py
- simplified_period_command.py
- test_agent.txt
- test_agent_spec.docx
- test_cross_agent_collaboration.py
- test_orchestrator.py
- test_orchestrator_integration.py
- test_orchestrator_scenarios.py
- test_proactive_collaboration.py

### agents
- agent_registry.py
- analyzer.py
- collaborative_crew.py
- context_manager.py
- critic.py
- data_collector.py
- digester.py
- orchestrator.py
- task_queue.py
- __init__.py

### config
- logging_config.py
- settings.py
- __init__.py

### config\__pycache__
- logging_config.cpython-39.pyc
- __init__.cpython-39.pyc

### database
- db_manager.py
- models.py
- __init__.py

### learning_examples
- examples.jsonl

### llm
- base_llm.py
- gemma_model.py
- qwen_model.py
- __init__.py

### logs


### scheduler
- jobs.py
- __init__.py

### telegram_bot
- bot.py
- handlers.py
- improved_message_handler.py
- improved_view_digest.py
- period_command.py
- __init__.py

### utils
- helpers.py
- learning_manager.py
- telegram_session_manager.py
- text_utils.py
- __init__.py

### __pycache__
- main.cpython-39.pyc

## Зависимости и функции
### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\improved_message_handler.py
- Библиотеки: ContextTypes, datetime, Update, timedelta, logging
- Функции: enumerate, str, len, timedelta, min

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\main.py
- Библиотеки: asyncio, JobScheduler, AnalyzerAgent, os, TELEGRAM_BOT_TOKEN, DigesterAgent, AgentRegistry, QwenLLM, logging, threading, setup_logging, TELEGRAM_API_HASH, GemmaLLM, argparse, OrchestratorAgent, TelegramSessionManager, TaskQueue, traceback, TELEGRAM_API_ID, sys, datetime, TelegramClient, TelegramBot, IntelligentOrchestratorAgent, load_dotenv, DATABASE_URL, TELEGRAM_CHANNELS, CriticAgent, timedelta, DatabaseManager
- Функции: JobScheduler, AnalyzerAgent, run_message_analysis, DigesterAgent, enable_detailed_reasoning_logs, AgentRegistry, len, run_bot_with_scheduler, QwenLLM, str, _log_execution_results, hasattr, setup_logging, GemmaLLM, OrchestratorAgent, run_intelligent_workflow, main, run_data_collection, print, TelegramSessionManager, run_full_workflow, create_digest, run_categorization_review, TelegramBot, IntelligentOrchestratorAgent, load_dotenv, parse_arguments, collect_messages, sum, run_orchestrated_workflow, CriticAgent, run_scheduler, timedelta, DatabaseManager

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\run_orchestrator_tests.py
- Библиотеки: asyncio, traceback, TELEGRAM_API_ID, TELEGRAM_API_HASH, DATABASE_URL, sys, TELEGRAM_CHANNELS, os, GemmaLLM, AgentRegistry, OrchestratorAgent, datetime, QwenLLM, DatabaseManager
- Функции: GemmaLLM, enumerate, test_func, AgentRegistry, len, connectivity_test, OrchestratorAgent, QwenLLM, main, print, DatabaseManager

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\simplified_period_command.py
- Библиотеки: asyncio, DataCollectorAgent, TextUtils, ContextTypes, AnalyzerAgent, GemmaLLM, DigesterAgent, re, datetime, InlineKeyboardMarkup, CriticAgent, QwenLLM, Update, timedelta, logging, InlineKeyboardButton
- Функции: get_digest_type_name, ValueError, AnalyzerAgent, GemmaLLM, timedelta, DigesterAgent, len, str, QwenLLM, CriticAgent, TextUtils, enumerate, DataCollectorAgent, min

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\run_workflow.py
- Библиотеки: asyncio, TELEGRAM_API_ID, TELEGRAM_API_HASH, GemmaLLM, TELEGRAM_CHANNELS, os, datetime, TelegramClient, QwenLLM, CriticAgent, timedelta, load_dotenv, DatabaseManager
- Функции: run_full_workflow, collect_messages, GemmaLLM, enumerate, str, create_digest, len, analyze_messages, QwenLLM, CriticAgent, TelegramClient, review_categorization, timedelta, print, load_dotenv, DatabaseManager

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\run_telegram_bot2.py
- Библиотеки: asyncio, events, InputPeerUser, os, TelegramClient, load_dotenv, logging, DatabaseManager
- Функции: split_text, len, TelegramClient, main, enumerate, load_dotenv, DatabaseManager

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_orchestrator.py
- Библиотеки: asyncio, traceback, DATABASE_URL, AgentRegistry, OrchestratorAgent, DatabaseManager
- Функции: enumerate, AgentRegistry, OrchestratorAgent, len, test_orchestrator, print, DatabaseManager

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_proactive_collaboration.py
- Библиотеки: asyncio, DATABASE_URL, sys, os, AgentRegistry, datetime, DatabaseManager, logging, IntelligentOrchestratorAgent
- Функции: enumerate, test_database_methods, test_proactive_collaboration_monitoring, str, AgentRegistry, test_full_orchestrator_with_proactive_collaboration, len, main, IntelligentOrchestratorAgent, print, DatabaseManager, test_proactive_collaboration_execution

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_cross_agent_collaboration.py
- Библиотеки: asyncio, DATABASE_URL, sys, os, inspect, AgentRegistry, datetime, CollaborativeCrew, DatabaseManager, Mock, IntelligentOrchestratorAgent, logging, MagicMock
- Функции: test_orchestrator_collaboration_integration, str, AgentRegistry, len, CollaborativeCrew, test_cross_agent_collaboration, main, IntelligentOrchestratorAgent, print, DatabaseManager, sum, hasattr

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_orchestrator_scenarios.py
- Библиотеки: asyncio, patch, TaskType, TaskStatus, TaskResult, AsyncMock, pytest, AgentRegistry, OrchestratorAgent, datetime, TaskRequest, DatabaseManager, Mock, timedelta, TaskPriority
- Функции: TaskResult, timedelta, AsyncMock, failing_executor, Exception, real_world_setup, len, OrchestratorAgent, next, TaskRequest, datetime, setup_orchestrator, range, Mock, decision_orchestrator

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\collaborative_crew.py
- Библиотеки: Any, Task, List, GemmaLLM, Dict, Process, re, datetime, Enum, logging, Crew
- Функции: Task, _parse_categorization_result, str, len, float, min, hasattr, GemmaLLM, Exception, max, __init__, _get_existing_crewai_agents, _log_crewai_collaboration, type, Crew, sum, all, _parse_quality_result, enumerate

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\agent_registry.py
- Библиотеки: DataCollectorAgent, Any, AnalyzerAgent, Dict, DigesterAgent, CriticAgent, Enum, logging, Optional
- Функции: get_agent, getattr, callable, ValueError, validate_agents, _initialize_agents, AnalyzerAgent, Exception, get_status, AttributeError, DigesterAgent, len, str, __init__, CriticAgent, DataCollectorAgent, isinstance, hasattr

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\analyzer.py
- Библиотеки: Task, CATEGORIES, Tool, os, as_completed, time, datetime, QwenLLM, json, re, ThreadPoolExecutor, Agent, CriticAgent, LearningExamplesManager, logging
- Функции: any, _classify_message, Task, str, len, QwenLLM, ThreadPoolExecutor, Agent, create_task, analyze_messages, min, process_batch, _log_classification_reasoning, max, as_completed, int, __init__, _format_examples_for_reasoning, sum, Tool, CriticAgent, range, enumerate, LearningExamplesManager

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\context_manager.py
- Библиотеки: dataclass, Any, CATEGORIES, List, TELEGRAM_CHANNELS, Dict, asdict, datetime, json, Enum, timedelta, logging, Optional
- Функции: get_agent, __post_init__, _get_context, str, len, get_task, set_agent, _cleanup_session_context, get_session, set_global, _update_aggregated_metrics, update_agent_status, __init__, ContextEntry, get_global, set_session, end_session, get_context_summary, _initialize_global_context, _set_context, record_task_metrics, set_task, cleanup_expired, get_agent_status, get_system_stats, timedelta, start_session

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\data_collector.py
- Библиотеки: asyncio, GetHistoryRequest, FloodWaitError, random, Task, TELEGRAM_API_ID, TELEGRAM_API_HASH, Tool, TELEGRAM_CHANNELS, DigesterAgent, time, datetime, TelegramClient, Agent, timedelta, TelegramSessionManager, logging, SlowModeWaitError
- Функции: GetHistoryRequest, Task, Tool, DigesterAgent, len, client, str, __init__, range, Agent, create_task, timedelta, enumerate, TelegramSessionManager, hasattr

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_orchestrator_integration.py
- Библиотеки: asyncio, TaskType, JobScheduler, AgentType, timedelta, os, AgentRegistry, ContextScope, tempfile, OrchestratorAgent, time, patch, TaskQueue, AsyncMock, sys, datetime, pytest, ContextManager, run_orchestrated_workflow, TaskRequest, Mock, TaskPriority, DatabaseManager
- Функции: any, test_agent_registry_initialization, JobScheduler, AgentRegistry, len, test_context_manager_functionality, Exception, test_scheduler_integration, OrchestratorAgent, patch, TaskQueue, AsyncMock, mock_workflow_components, temp_db, mock_agents, ContextManager, run_orchestrated_workflow, TaskRequest, range, Mock, timedelta, DatabaseManager, orchestrator_setup

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\task_queue.py
- Библиотеки: asyncio, TaskStatus, dataclass, uuid, Any, TaskResult, List, field, Dict, datetime, TaskRequest, heapq, Enum, timedelta, logging, TaskPriority, Optional
- Функции: _check_dependencies, QueuedTask, any, list, TaskResult, field, _calculate_priority_score, __post_init__, enumerate, int, __lt__, str, len, __init__, timedelta, min, _is_task_expired, hasattr

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\critic.py
- Библиотеки: CATEGORIES, GemmaLLM, Tool, os, re, datetime, json, ThreadPoolExecutor, Agent, LearningExamplesManager, logging, concurrent.futures
- Функции: any, _perform_context_review, _perform_consistency_review, str, len, _synthesize_multi_perspective_decision, ThreadPoolExecutor, Agent, review_categorization, min, get_message_by_id, GemmaLLM, max, int, _apply_review_decision, __init__, _save_learning_example, _parse_final_decision, _perform_legal_accuracy_review, review_recent_categorizations, _parse_review_response, sum, Tool, _log_multi_perspective_reasoning, range, LearningExamplesManager

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\digester.py
- Библиотеки: asyncio, BOT_USERNAME, DataCollectorAgent, Task, CATEGORIES, GemmaLLM, Tool, as_completed, time, datetime, re, json, ThreadPoolExecutor, Agent, timedelta, logging
- Функции: _log_content_strategy, any, Task, _extract_content_after_colon, _generate_short_annotation, _add_category_icon, str, len, save_digest_with_parameters, _generate_category_overview_with_strategy, _generate_brief_section, ThreadPoolExecutor, _generate_digest_intro, create_task, _calculate_category_importance, _generate_detailed_section, Agent, _extract_fallback_priorities, get_digest_to_update, min, hasattr, set, ValueError, _extract_fallback_emphasis, GemmaLLM, as_completed, dir, time, __init__, _clean_text_with_links, _extract_categories_from_text, _plan_digest_strategy, create_digest, type, _format_category_stats, sum, list, update_digests_for_date, round, Tool, _extract_links_and_headlines, _process_categories_parallel, _extract_title_for_url, sorted, timedelta, enumerate, _extract_fallback_style, DataCollectorAgent, isinstance, _parse_strategy_response, _create_fallback_strategy

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\orchestrator.py
- Библиотеки: asyncio, dataclass, Any, Task, List, Crew, GemmaLLM, Dict, datetime, CollaborativeCrew, Enum, Agent, timedelta, logging, Optional
- Функции: any, Task, __post_init__, _log_collaboration_impact, str, len, CollaborativeCrew, Agent, create_task, min, hasattr, llm_generate, set, getattr, _calculate_message_complexity, GemmaLLM, Exception, max, __init__, _log_collaboration_monitoring, TaskResult, sum, _generate_recommendations, all, TaskRequest, chr, timedelta, enumerate, _enhance_plan_with_collaboration, _should_use_collaboration, strategy_func, isinstance

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\config\settings.py
- Библиотеки: load_dotenv, os
- Функции: load_dotenv

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\config\logging_config.py
- Библиотеки: logging, os, RotatingFileHandler
- Функции: RotatingFileHandler, setup_logging

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\database\models.py
- Библиотеки: Text, String, UniqueConstraint, Boolean, Column, relationship, declarative_base, ForeignKey, datetime, DateTime, Index, create_engine, Integer
- Функции: String, UniqueConstraint, Column, relationship, declarative_base, ForeignKey, __repr__, init_db, Index, create_engine

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\database\db_manager.py
- Библиотеки: DigestGeneration, List, func, Column, Float, DigesterAgent, DigestSection, json, init_db, extract, DateTime, sessionmaker, logging, joinedload, Any, case, sqlalchemy, time, and_, Table, Optional, MetaData, Integer, String, or_, datetime, ForeignKey, Digest, create_engine, text, Base, Dict, scoped_session, functools, timedelta, Message
- Функции: get_low_confidence_messages, DigestGeneration, save_message, dict, bool, Column, func, save_digest_generation, DigesterAgent, len, save_digest_with_parameters, find_digests_by_parameters, DigestSection, str, create_collaboration_log_table, get_unanalyzed_messages, get_latest_digest, init_db, wrapper, sessionmaker, get_messages_with_low_confidence, joinedload, hasattr, update_message_category, get_messages_by_date_range, get_message_by_channel_and_id, get_message_by_id, update_today_flags, get_categories_distribution, get_recently_categorized_messages, getattr, max, batch_save_messages, get_recently_categorized_messages_excluding_ids, get_last_digest_generation, case, get_filtered_messages, time, and_, __init__, get_recent_messages, update_message_categorization, save_digest, Table, MetaData, _log_collaboration_change, get_confidence_statistics, callable, find_todays_digests, or_, datetime, ForeignKey, Digest, get_latest_messages, type, create_engine, get_digests_containing_date, text, batch_update_message_categories, get_digest_by_date_with_sections, list, get_collaboration_statistics, round, scoped_session, decorator, get_latest_digest_with_sections, with_retry, get_digest_by_date, get_digest_by_id_with_sections, range, timedelta, enumerate, get_recently_categorized_messages_by_category, isinstance, Message

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\llm\base_llm.py
- Библиотеки: requests, hashlib, os, time, logging
- Функции: open, _generate_response, int, len, str, __init__, _get_cached_response

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\llm\gemma_model.py
- Библиотеки: requests, hashlib, os, time, logging, BaseLLM
- Функции: open, str, super, summarize, __init__, generate

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\llm\__init__.py
- Библиотеки: BaseLLM
- Функции: Отсутствуют

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\llm\qwen_model.py
- Библиотеки: hashlib, logging, os, BaseLLM
- Функции: open, classify, str, super, __init__, _process_classification_response

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\scheduler\jobs.py
- Библиотеки: asyncio, DIGEST_TIME_MINUTE, IntervalTrigger, Task, AnalyzerAgent, DigesterAgent, AgentRegistry, logging, time, OrchestratorAgent, AsyncIOExecutor, COLLECT_INTERVAL_MINUTES, TaskQueue, DIGEST_TIME_HOUR, datetime, ANALYZE_INTERVAL_MINUTES, CronTrigger, Crew, BackgroundScheduler, DataCollectorAgent
- Функции: IntervalTrigger, analyze_messages_job, AnalyzerAgent, DigesterAgent, AgentRegistry, str, len, _setup_orchestrated_jobs, run_crew_job, coro_func, update_digests_job, hasattr, start, _log_workflow_results, _setup_legacy_jobs, OrchestratorAgent, time, __init__, run_async_job, setup_jobs, TaskQueue, update_today_flags_job, stop, toggle_orchestrator, CronTrigger, Crew, BackgroundScheduler, DataCollectorAgent

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\improved_message_handler.py
- Библиотеки: ContextTypes, GemmaLLM, datetime, Update, timedelta, logging
- Функции: enumerate, str, len, timedelta, min

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\bot.py
- Библиотеки: asyncio, start_command, period_command, CommandHandler, TELEGRAM_BOT_TOKEN, list_digests_command, logging, MessageHandler, CallbackQueryHandler, GemmaLLM, BotCommand, category_selection_command, get_category_icon, help_command, button_callback, Application, show_full_digest, improved_message_handler, filters
- Функции: start_command, improved_message_handler, category_selection_command, GemmaLLM, run, period_command, CommandHandler, help_command, button_callback, list_digests_command, __init__, MessageHandler, BotCommand, CallbackQueryHandler

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\helpers.py
- Библиотеки: datetime, timedelta
- Функции: ValueError, normalize_date, date_to_end_of_day, datetime, date_to_start_of_day, type, isinstance, parse_date_string, hasattr

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\period_command.py
- Библиотеки: asyncio, DataCollectorAgent, TextUtils, ContextTypes, AnalyzerAgent, GemmaLLM, DigesterAgent, time, datetime, re, InlineKeyboardMarkup, CriticAgent, Update, QwenLLM, timedelta, logging, InlineKeyboardButton
- Функции: get_digest_type_name, list, ValueError, AnalyzerAgent, GemmaLLM, timedelta, DigesterAgent, len, str, InlineKeyboardMarkup, QwenLLM, CriticAgent, TextUtils, enumerate, DataCollectorAgent, isinstance, min, InlineKeyboardButton

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\handlers.py
- Библиотеки: asyncio, period_command, timedelta, AnalyzerAgent, DigesterAgent, re, QwenLLM, Update, logging, InlineKeyboardButton, get_short_category_id, BOT_USERNAME, GemmaLLM, time, CATEGORIES, get_category_icon, telegram, datetime, ContextTypes, improved_message_handler, show_full_digest, page_navigation_callback, view_digest_section_callback, InlineKeyboardMarkup, TextUtils, DataCollectorAgent, view_digest_callback
- Функции: any, dict, AnalyzerAgent, timedelta, show_digest_categories, import_agent, DigesterAgent, len, str, QwenLLM, list_digests_command, min, start_digest_generation, map, InlineKeyboardButton, hasattr, getattr, ValueError, GemmaLLM, max, int, get_category_icon, __import__, datetime, handle_digest_generation, list, show_full_digest, page_navigation_callback, view_digest_section_callback, next, InlineKeyboardMarkup, CriticAgent, sorted, TextUtils, enumerate, view_digest_callback, DataCollectorAgent, isinstance, get_short_category_id

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\improved_view_digest.py
- Библиотеки: ContextTypes, hashlib, InlineKeyboardMarkup, Update, TextUtils, logging, InlineKeyboardButton
- Функции: list, get_category_icon, int, len, str, InlineKeyboardMarkup, range, get_short_category_id, InlineKeyboardButton

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\telegram_session_manager.py
- Библиотеки: asyncio, os, time, TelegramClient, logging
- Функции: list, str, len, super, TelegramClient, __init__, __new__

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\learning_manager.py
- Библиотеки: Any, threading, List, os, Dict, datetime, json, logging, Optional
- Функции: set, get_examples, list, _should_rotate_file, open, max, str, len, id, __init__, sorted, save_example, _load_examples, _rotate_examples_file, sum

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\text_utils.py
- Библиотеки: logging, re
- Функции: convert_to_html, split_text, clean_markdown_text, len

## Промпты
## Бизнес-требования
### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agent_config.json
{
  "agent_name": "TestAgent",
  "model": "gpt-4",
  "temperature": 0.1,
  "system_prompt": "Ты - банковский ассистент",
  "guardrails": [
    "Не разглашай конфиденциальную информацию",
    "Всегда проверяй данные клиента"
  ]
}

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\project_structure.txt
lawdigest_bot/
    config/__init__.py
    config/settings.py
    config/logging_config.py
    database/__init__.py
    database/models.py
    database/db_manager.py
    agents/__init__.py
    agents/data_collector.py
    agents/analyzer.py
    agents/digester.py
    telegram_bot/__init__.py
    telegram_bot/bot.py
    telegram_bot/handlers.py
    llm/__init__.py
    llm/qwen_model.py
    llm/gemma_model.py
    utils/__init__.py
    utils/helpers.py
    scheduler/__init__.py
    scheduler/jobs.py
    main.py
    requirements.txt
    README.md


### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\README.md
# LawDigest Bot v2.0 - Intelligent Orchestrator

## 🚀 Новая версия с Intelligent планированием!

Система была полностью модернизирована с добавлением **Intelligent Orchestrator** - умного планировщика, который использует CrewAI для принятия решений о том, какие агенты запускать и в каком порядке.

## 🧠 Что нового в v2.0

### Intelligent Orchestrator Agent
- **Умное планирование**: Анализирует текущую ситуацию и сам принимает решения
- **Контекстно-зависимые решения**: Учитывает состояние данных, количество неанализированных сообщений, наличие дайджестов
- **Объяснение решений**: Каждая задача имеет обоснование, почему она нужна
- **Адаптивные стратегии**: Разные подходы для разных сценариев
- **Fallback механизмы**: Если CrewAI недоступен, используется базовая логика

### Решение проблемы с нулевой уверенностью
Новый оркестратор **всегда** запускает анализатор и критик когда это необходимо, решая проблему с сообщениями с нулевой уверенностью (confidence=0).

## 🎯 Сценарии работы

### 1
. daily_workflow (ежедневный)
- Анализирует состояние системы
- Собирает новые данные если нужно
- **Всегда** запускает анализатор для сообщений без категоризации
- **Всегда** запускает критик для улучшения качества
- Создает или обновляет дайджесты

### 2. urgent_update (срочное обновление)
- Быстрый сбор только критических данных
- Ограниченный анализ для скорости
- Создание краткого дайджеста

### 3. full_analysis (полный анализ)
- Глубокий анализ за длительный период
- Акцент на качество анализа
- Расширенная проверка критиком

### 4. digest_only (только дайджест)
- Работа только с существующими данными
- Создание дайджестов без сбора новых данных

## 🔧 Установка и запуск

### Быстрый старт с Intelligent Orchestrator

```bash
# Рекомендуемый способ - с intelligent планированием
python main.py --mode workflow --orchestrator --scenario daily_workflow

# Срочное обновление
python main.py --mode workflow --orchestrator --scenario urgent_update

# Полный анализ за неделю
python main.py 
--mode workflow --orchestrator --scenario full_analysis --days 7

# Только создание дайджеста
python main.py --mode workflow --orchestrator --scenario digest_only
```

### Тестирование системы

```bash
# Тестирование intelligent оркестратора
python test_intelligent_orchestrator.py

# Примеры использования
python orchestrator_examples.py
```

### Legacy режим (для совместимости)

```bash
# Старый способ без оркестратора
python main.py --mode workflow --days 1

# Legacy режим
python main.py --mode legacy --days 1
```

## 🧠 Как работает Intelligent Planning

### 1. Анализ контекста
Оркестратор собирает информацию о:
- Количестве неанализированных сообщений
- Сообщениях с низкой уверенностью категоризации
- Наличии дайджестов за сегодня
- Времени последнего сбора данных
- Статистике по категориям

### 2. CrewAI планирование
Intelligent агент анализирует ситуацию и принимает решения:
```python
# Пример reasoning от оркестратора:
"Необходим анализ 15 неанализированных сообщений для улучшения
 качества данных"
"Запускаю критик для проверки 8 сообщений с низкой уверенностью"
"Создаю новый дайджест, так как за сегодня дайджестов еще нет"
```

### 3. Адаптивное выполнение
- Учитывает зависимости между задачами
- Обрабатывает ошибки с fallback логикой
- Предоставляет детальные метрики и рекомендации

## 📊 Мониторинг и метрики

### Детальное логирование
```
=== РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ===
Статус: success
Сценарий: daily_workflow
Успешность: 100.0%
Время выполнения: 29.4с
Intelligent планирование: True

=== КОНТЕКСТ ПЛАНИРОВАНИЯ ===
Изначально неанализированных: 15
С низкой уверенностью: 8
Дайджестов за сегодня: 0

=== ДЕТАЛИ ВЫПОЛНЕНИЯ ЗАДАЧ ===
✅ data_collection: completed (9.56с)
✅ message_analysis: completed (8.42с)
✅ categorization_review: completed (6.21с)
✅ digest_creation: completed (5.15с)
```

### Проверка здоровья системы
```bash
# В коде можно использовать
health_check = await registry.health_check()
print(f"Статус системы: {health_check['overall_status']}")
```

## 🔄 М
играция с предыдущей версии

### Что изменилось
1. **agents/orchestrator.py** → **IntelligentOrchestratorAgent**
2. **Новый** agents/agent_registry.py с улучшенной валидацией
3. **Обновленный** main.py с поддержкой новых сценариев
4. **Сохранена** обратная совместимость через legacy режим

### Обновление конфигурации
```bash
# Убедитесь, что у вас есть все зависимости
poetry install

# Или если используете pip
pip install crewai

# Запустите тесты
python test_intelligent_orchestrator.py
```

## 🛡️ Обработка ошибок

### Robust планирование
- Если CrewAI недоступен → fallback на базовую логику
- Если агент недоступен → пропуск с логированием
- Если задача failed → продолжение с рекомендациями

### Автоматическое восстановление
```python
# Система автоматически:
# 1. Проверяет здоровье агентов
# 2. Адаптирует план при проблемах
# 3. Предоставляет рекомендации для исправления
```

## 📋 Рекомендации по использованию

### Для продакшена
```bash
# Ежедневный запуск через cron
0 9 * * * cd /pa
th/to/bot && python main.py --mode workflow --orchestrator --scenario daily_workflow

# Срочные обновления
python main.py --mode workflow --orchestrator --scenario urgent_update
```

### Для разработки
```bash
# Тестирование изменений
python main.py --mode workflow --orchestrator --scenario daily_workflow --debug

# Анализ производительности
python orchestrator_examples.py
```

### Для мониторинга
```bash
# Проверка системы
python test_intelligent_orchestrator.py

# Детальная диагностика
python main.py --mode workflow --orchestrator --scenario daily_workflow --debug
```

## 🔍 Отладка проблем

### Если сообщения остаются с confidence=0
1. Проверьте, что анализатор запускается: `message_analysis` должен быть в плане
2. Включите debug режим: `--debug`
3. Проверьте логи анализатора на ошибки

### Если критик не запускается
1. Intelligent оркестратор должен детектировать сообщения с низкой уверенностью
2. Проверьте, что `categorization_review` есть в плане выполнения
3. Убедитесь, что Criti
cAgent инициализирован корректно

### Если CrewAI не работает
Система автоматически переключится на fallback режим с сообщением в логах:
```
Ошибка при intelligent планировании: ... 
Переходим на fallback планирование...
```

## 🎉 Преимущества новой версии

✅ **Умное планирование** - система сама решает, что делать  
✅ **Решена проблема с confidence=0** - анализатор и критик запускаются когда нужно  
✅ **Лучшая производительность** - оптимизированные планы выполнения  
✅ **Подробная аналитика** - детальные метрики и рекомендации  
✅ **Гибкость** - разные сценарии для разных задач  
✅ **Надежность** - fallback механизмы и обработка ошибок  
✅ **Обратная совместимость** - legacy режим сохранен  

## 📞 Поддержка

При проблемах:
1. Запустите `python test_intelligent_orchestrator.py`
2. Проверьте логи с `--debug` флагом
3. Попробуйте fallback: `python main.py --mode legacy`
4. Изучите примеры в `orchestrator_examples.py`

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\requirements.txt
# Telegram
python-telegram-bot==20.6
telethon==1.28.5

# Database
sqlalchemy==2.0.20
alembic==1.11.3

# LLM & AI
crewai==0.8.0
langchain==0.0.235
openai==0.28.0

# Utilities
python-dotenv==1.0.0
schedule==1.2.0
apscheduler==3.10.1
loguru==0.7.0


### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_agent.txt
Агент: TestAgent

Описание:
Тестовый ИИ-агент для банковских операций.

Функции:
- Обработка запросов клиентов
- Анализ рисков
- Предоставление рекомендаций

Ограничения:
- Не обрабатывает персональные данные без разрешения
- Требует подтверждения для финансовых операций



### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_agent_spec.docx
Техническая спецификация TestAgent
Общие сведения
TestAgent - это ИИ-агент для банковской сферы.
Технические характеристики
Модель: Qwen3/GEmma
Температура: 0.1
Максимальное число токенов: 4096
Ограничения безопасности
1. Не обрабатывает персональные данные без согласия
2. Требует подтверждения для операций свыше 100,000 руб.


## Анализ LLM
Ошибка анализа: Error code: 404 - {'detail': 'Not Found'}
## Пустые файлы
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\__init__.py
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\config\__init__.py
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\database\__init__.py
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\scheduler\__init__.py
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\__init__.py
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\__init__.py
