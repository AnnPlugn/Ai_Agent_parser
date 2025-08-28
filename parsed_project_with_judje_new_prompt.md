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
### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\main.py
- Библиотеки: QwenLLM, load_dotenv, logging, asyncio, TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNELS, GemmaLLM, threading, TELEGRAM_API_HASH, sys, OrchestratorAgent, traceback, TELEGRAM_API_ID, setup_logging, AnalyzerAgent, os, CriticAgent, DatabaseManager, JobScheduler, argparse, datetime, TaskQueue, TelegramBot, DigesterAgent, DATABASE_URL, TelegramClient, TelegramSessionManager, AgentRegistry, IntelligentOrchestratorAgent, timedelta
- Функции: QwenLLM, run_intelligent_workflow, load_dotenv, run_full_workflow, enable_detailed_reasoning_logs, sum, GemmaLLM, hasattr, run_categorization_review, create_digest, str, run_message_analysis, print, collect_messages, run_bot_with_scheduler, _log_execution_results, OrchestratorAgent, run_orchestrated_workflow, setup_logging, len, AnalyzerAgent, IntelligentOrchestratorAgent, CriticAgent, DatabaseManager, JobScheduler, TelegramBot, DigesterAgent, run_scheduler, run_data_collection, TelegramSessionManager, parse_arguments, AgentRegistry, main, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\improved_message_handler.py
- Библиотеки: logging, ContextTypes, datetime, Update, timedelta
- Функции: min, str, enumerate, len, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\run_orchestrator_tests.py
- Библиотеки: QwenLLM, os, DATABASE_URL, TELEGRAM_API_HASH, DatabaseManager, asyncio, sys, OrchestratorAgent, TELEGRAM_CHANNELS, traceback, GemmaLLM, AgentRegistry, TELEGRAM_API_ID, datetime
- Функции: QwenLLM, print, DatabaseManager, connectivity_test, OrchestratorAgent, GemmaLLM, AgentRegistry, test_func, enumerate, len, main

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\run_telegram_bot2.py
- Библиотеки: os, TelegramClient, load_dotenv, logging, DatabaseManager, asyncio, events, InputPeerUser
- Функции: split_text, TelegramClient, load_dotenv, DatabaseManager, enumerate, len, main

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\run_workflow.py
- Библиотеки: QwenLLM, os, CriticAgent, load_dotenv, TelegramClient, TELEGRAM_API_HASH, DatabaseManager, asyncio, TELEGRAM_CHANNELS, GemmaLLM, TELEGRAM_API_ID, datetime, timedelta
- Функции: str, QwenLLM, print, create_digest, CriticAgent, load_dotenv, TelegramClient, DatabaseManager, run_full_workflow, collect_messages, review_categorization, GemmaLLM, analyze_messages, enumerate, len, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_cross_agent_collaboration.py
- Библиотеки: os, DATABASE_URL, logging, DatabaseManager, asyncio, sys, inspect, MagicMock, AgentRegistry, datetime, IntelligentOrchestratorAgent, Mock, CollaborativeCrew
- Функции: str, print, DatabaseManager, main, test_cross_agent_collaboration, sum, AgentRegistry, hasattr, len, test_orchestrator_collaboration_integration, IntelligentOrchestratorAgent, CollaborativeCrew

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\simplified_period_command.py
- Библиотеки: AnalyzerAgent, QwenLLM, InlineKeyboardMarkup, DigesterAgent, re, CriticAgent, DataCollectorAgent, logging, ContextTypes, asyncio, TextUtils, InlineKeyboardButton, GemmaLLM, datetime, Update, timedelta
- Функции: AnalyzerAgent, min, str, QwenLLM, DigesterAgent, CriticAgent, DataCollectorAgent, ValueError, get_digest_type_name, TextUtils, GemmaLLM, enumerate, len, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_orchestrator.py
- Библиотеки: DATABASE_URL, DatabaseManager, asyncio, OrchestratorAgent, traceback, AgentRegistry
- Функции: print, DatabaseManager, test_orchestrator, OrchestratorAgent, AgentRegistry, enumerate, len

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_orchestrator_integration.py
- Библиотеки: tempfile, asyncio, AgentType, timedelta, sys, OrchestratorAgent, run_orchestrated_workflow, TaskPriority, os, DatabaseManager, TaskType, JobScheduler, ContextScope, time, AsyncMock, datetime, Mock, TaskQueue, pytest, ContextManager, AgentRegistry, TaskRequest, patch
- Функции: mock_workflow_components, timedelta, temp_db, test_agent_registry_initialization, any, OrchestratorAgent, run_orchestrated_workflow, Exception, orchestrator_setup, len, DatabaseManager, range, JobScheduler, AsyncMock, mock_agents, Mock, test_scheduler_integration, TaskQueue, test_context_manager_functionality, ContextManager, AgentRegistry, TaskRequest, patch

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_proactive_collaboration.py
- Библиотеки: os, DATABASE_URL, logging, DatabaseManager, asyncio, sys, AgentRegistry, datetime, IntelligentOrchestratorAgent
- Функции: str, print, DatabaseManager, main, test_proactive_collaboration_execution, test_full_orchestrator_with_proactive_collaboration, test_database_methods, AgentRegistry, test_proactive_collaboration_monitoring, enumerate, len, IntelligentOrchestratorAgent

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_orchestrator_scenarios.py
- Библиотеки: TaskStatus, pytest, AsyncMock, DatabaseManager, asyncio, TaskType, TaskResult, OrchestratorAgent, TaskPriority, patch, AgentRegistry, datetime, TaskRequest, Mock, timedelta
- Функции: datetime, decision_orchestrator, len, next, range, real_world_setup, setup_orchestrator, OrchestratorAgent, TaskResult, Exception, AsyncMock, TaskRequest, failing_executor, Mock, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\agent_registry.py
- Библиотеки: Dict, AnalyzerAgent, Enum, DigesterAgent, CriticAgent, DataCollectorAgent, logging, Optional, Any
- Функции: AnalyzerAgent, str, _initialize_agents, DigesterAgent, callable, CriticAgent, DataCollectorAgent, AttributeError, ValueError, getattr, hasattr, Exception, validate_agents, len, get_status, isinstance, __init__, get_agent

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\analyzer.py
- Библиотеки: Task, Agent, os, QwenLLM, re, CriticAgent, Tool, logging, as_completed, ThreadPoolExecutor, json, time, LearningExamplesManager, CATEGORIES, datetime
- Функции: QwenLLM, sum, LearningExamplesManager, analyze_messages, str, Task, any, as_completed, enumerate, len, _classify_message, min, _format_examples_for_reasoning, create_task, CriticAgent, Tool, range, ThreadPoolExecutor, process_batch, __init__, _log_classification_reasoning, Agent, max, int

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\context_manager.py
- Библиотеки: Dict, dataclass, Enum, logging, json, Optional, TELEGRAM_CHANNELS, Any, CATEGORIES, datetime, List, asdict, timedelta
- Функции: _initialize_global_context, get_agent_status, start_session, cleanup_expired, get_session, _set_context, get_task, timedelta, str, set_task, ContextEntry, _cleanup_session_context, len, update_agent_status, set_agent, record_task_metrics, get_context_summary, set_session, _get_context, __init__, get_agent, __post_init__, end_session, set_global, get_global, _update_aggregated_metrics, get_system_stats

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\collaborative_crew.py
- Библиотеки: Dict, Process, Task, Enum, Crew, re, logging, Any, GemmaLLM, datetime, List
- Функции: sum, GemmaLLM, hasattr, type, float, _get_existing_crewai_agents, str, Task, all, _parse_categorization_result, Exception, enumerate, len, min, Crew, __init__, _log_crewai_collaboration, max, _parse_quality_result

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\critic.py
- Библиотеки: Agent, os, re, Tool, logging, ThreadPoolExecutor, json, concurrent.futures, LearningExamplesManager, GemmaLLM, CATEGORIES, datetime
- Функции: get_message_by_id, _parse_review_response, review_categorization, sum, LearningExamplesManager, GemmaLLM, _save_learning_example, str, any, _perform_context_review, _apply_review_decision, review_recent_categorizations, len, min, Tool, range, ThreadPoolExecutor, _perform_consistency_review, _synthesize_multi_perspective_decision, _perform_legal_accuracy_review, _parse_final_decision, __init__, Agent, max, _log_multi_perspective_reasoning, int

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\data_collector.py
- Библиотеки: FloodWaitError, Task, Agent, DigesterAgent, TelegramClient, Tool, logging, random, asyncio, TELEGRAM_API_HASH, time, TELEGRAM_CHANNELS, TelegramSessionManager, SlowModeWaitError, TELEGRAM_API_ID, datetime, GetHistoryRequest, timedelta
- Функции: str, Task, create_task, Agent, client, DigesterAgent, Tool, range, TelegramSessionManager, GetHistoryRequest, hasattr, enumerate, len, __init__, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\task_queue.py
- Библиотеки: Dict, dataclass, TaskStatus, Enum, heapq, field, logging, TaskRequest, asyncio, uuid, Optional, TaskResult, TaskPriority, Any, datetime, List, timedelta
- Функции: min, str, QueuedTask, list, _is_task_expired, any, field, __lt__, TaskResult, __post_init__, int, hasattr, enumerate, len, _check_dependencies, _calculate_priority_score, __init__, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\digester.py
- Библиотеки: Task, Agent, BOT_USERNAME, re, as_completed, logging, Tool, DataCollectorAgent, ThreadPoolExecutor, asyncio, json, time, GemmaLLM, CATEGORIES, datetime, timedelta
- Функции: _extract_links_and_headlines, _clean_text_with_links, _extract_content_after_colon, _extract_categories_from_text, sum, set, GemmaLLM, hasattr, type, _extract_fallback_emphasis, timedelta, create_digest, str, Task, _calculate_category_importance, any, as_completed, update_digests_for_date, round, ValueError, _log_content_strategy, sorted, enumerate, len, _extract_fallback_priorities, _create_fallback_strategy, _generate_short_annotation, get_digest_to_update, min, create_task, _generate_category_overview_with_strategy, Tool, dir, ThreadPoolExecutor, time, _plan_digest_strategy, _generate_brief_section, _generate_digest_intro, _process_categories_parallel, _generate_detailed_section, __init__, isinstance, _format_category_stats, Agent, DataCollectorAgent, _extract_fallback_style, _extract_title_for_url, _add_category_icon, list, save_digest_with_parameters, _parse_strategy_response

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\config\logging_config.py
- Библиотеки: logging, RotatingFileHandler, os
- Функции: RotatingFileHandler, setup_logging

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\config\settings.py
- Библиотеки: os, load_dotenv
- Функции: load_dotenv

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\orchestrator.py
- Библиотеки: Dict, dataclass, Task, Enum, Agent, Crew, logging, asyncio, CollaborativeCrew, Optional, Any, GemmaLLM, datetime, List, timedelta
- Функции: _enhance_plan_with_collaboration, TaskResult, sum, set, GemmaLLM, hasattr, timedelta, chr, str, Task, llm_generate, any, all, Exception, enumerate, len, min, create_task, _calculate_message_complexity, _should_use_collaboration, _log_collaboration_impact, getattr, __init__, isinstance, _generate_recommendations, Agent, strategy_func, max, _log_collaboration_monitoring, __post_init__, TaskRequest, CollaborativeCrew

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\database\db_manager.py
- Библиотеки: MetaData, String, logging, ForeignKey, text, Optional, Integer, sessionmaker, List, or_, DigestGeneration, Dict, and_, case, func, DateTime, Table, create_engine, init_db, sqlalchemy, Base, joinedload, Message, DigestSection, time, Column, Any, Float, datetime, extract, DigesterAgent, scoped_session, Digest, json, functools, timedelta
- Функции: MetaData, create_collaboration_log_table, find_todays_digests, get_message_by_id, save_digest_generation, get_digest_by_date, text, get_digest_by_date_with_sections, update_message_categorization, ForeignKey, sessionmaker, get_latest_digest, get_recently_categorized_messages_by_category, hasattr, type, or_, get_messages_by_date_range, DigestGeneration, batch_save_messages, get_collaboration_statistics, with_retry, str, get_last_digest_generation, decorator, callable, and_, case, bool, func, round, get_latest_digest_with_sections, Table, create_engine, enumerate, len, init_db, save_message, get_messages_with_low_confidence, find_digests_by_parameters, get_categories_distribution, update_today_flags, get_digests_containing_date, range, Message, DigestSection, joinedload, get_unanalyzed_messages, time, get_message_by_channel_and_id, get_latest_messages, Column, get_recently_categorized_messages, datetime, get_recently_categorized_messages_excluding_ids, batch_update_message_categories, __init__, get_filtered_messages, isinstance, getattr, update_message_category, save_digest, DigesterAgent, max, scoped_session, get_low_confidence_messages, Digest, dict, _log_collaboration_change, get_digest_by_id_with_sections, get_recent_messages, get_confidence_statistics, list, wrapper, save_digest_with_parameters, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\llm\base_llm.py
- Библиотеки: os, logging, time, hashlib, requests
- Функции: __init__, str, _generate_response, _get_cached_response, len, int, open

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\llm\gemma_model.py
- Библиотеки: os, logging, time, hashlib, requests, BaseLLM
- Функции: __init__, str, generate, super, summarize, open

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\database\models.py
- Библиотеки: String, UniqueConstraint, Boolean, ForeignKey, declarative_base, Column, DateTime, Index, Integer, create_engine, datetime, relationship, Text
- Функции: String, UniqueConstraint, ForeignKey, Column, Index, __repr__, declarative_base, create_engine, relationship, init_db

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\bot.py
- Библиотеки: logging, asyncio, TELEGRAM_BOT_TOKEN, get_category_icon, GemmaLLM, BotCommand, MessageHandler, Application, improved_message_handler, button_callback, list_digests_command, CallbackQueryHandler, category_selection_command, period_command, show_full_digest, start_command, filters, CommandHandler, help_command
- Функции: category_selection_command, BotCommand, period_command, MessageHandler, CommandHandler, start_command, improved_message_handler, GemmaLLM, run, help_command, button_callback, list_digests_command, CallbackQueryHandler, __init__

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\llm\__init__.py
- Библиотеки: BaseLLM
- Функции: Отсутствуют

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\llm\qwen_model.py
- Библиотеки: logging, BaseLLM, hashlib, os
- Функции: __init__, str, _process_classification_response, super, classify, open

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\handlers.py
- Библиотеки: QwenLLM, view_digest_section_callback, logging, ContextTypes, asyncio, page_navigation_callback, get_category_icon, GemmaLLM, re, TextUtils, improved_message_handler, InlineKeyboardButton, Update, get_short_category_id, AnalyzerAgent, BOT_USERNAME, period_command, show_full_digest, time, CATEGORIES, datetime, view_digest_callback, InlineKeyboardMarkup, DigesterAgent, DataCollectorAgent, telegram, timedelta
- Функции: QwenLLM, view_digest_section_callback, page_navigation_callback, import_agent, get_category_icon, GemmaLLM, hasattr, str, any, ValueError, TextUtils, InlineKeyboardButton, sorted, enumerate, len, list_digests_command, get_short_category_id, AnalyzerAgent, min, start_digest_generation, next, CriticAgent, show_full_digest, __import__, handle_digest_generation, map, datetime, view_digest_callback, getattr, isinstance, InlineKeyboardMarkup, DigesterAgent, max, DataCollectorAgent, dict, show_digest_categories, int, list, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\scheduler\jobs.py
- Библиотеки: logging, AsyncIOExecutor, asyncio, Task, DIGEST_TIME_HOUR, OrchestratorAgent, ANALYZE_INTERVAL_MINUTES, BackgroundScheduler, AnalyzerAgent, COLLECT_INTERVAL_MINUTES, Crew, time, datetime, CronTrigger, TaskQueue, IntervalTrigger, DigesterAgent, DataCollectorAgent, DIGEST_TIME_MINUTE, AgentRegistry
- Функции: run_crew_job, toggle_orchestrator, hasattr, setup_jobs, str, OrchestratorAgent, len, BackgroundScheduler, run_async_job, AnalyzerAgent, Crew, analyze_messages_job, time, _log_workflow_results, stop, __init__, update_today_flags_job, CronTrigger, TaskQueue, IntervalTrigger, DigesterAgent, DataCollectorAgent, start, coro_func, _setup_orchestrated_jobs, _setup_legacy_jobs, update_digests_job, AgentRegistry

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\improved_message_handler.py
- Библиотеки: logging, ContextTypes, GemmaLLM, datetime, Update, timedelta
- Функции: min, str, enumerate, len, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\helpers.py
- Библиотеки: datetime, timedelta
- Функции: date_to_end_of_day, normalize_date, date_to_start_of_day, ValueError, parse_date_string, hasattr, datetime, type, isinstance

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\improved_view_digest.py
- Библиотеки: InlineKeyboardMarkup, logging, ContextTypes, hashlib, TextUtils, InlineKeyboardButton, Update
- Функции: str, InlineKeyboardMarkup, list, range, get_category_icon, InlineKeyboardButton, len, int, get_short_category_id

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\learning_manager.py
- Библиотеки: Dict, os, threading, logging, json, Optional, Any, datetime, List
- Функции: save_example, str, max, _rotate_examples_file, open, _should_rotate_file, _load_examples, set, sum, get_examples, id, sorted, len, list, __init__

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\telegram_session_manager.py
- Библиотеки: os, TelegramClient, logging, asyncio, time
- Функции: str, TelegramClient, __new__, super, len, list, __init__

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\period_command.py
- Библиотеки: AnalyzerAgent, QwenLLM, InlineKeyboardMarkup, DigesterAgent, re, CriticAgent, DataCollectorAgent, logging, ContextTypes, asyncio, time, TextUtils, InlineKeyboardButton, GemmaLLM, datetime, Update, timedelta
- Функции: AnalyzerAgent, min, str, QwenLLM, DigesterAgent, InlineKeyboardMarkup, CriticAgent, DataCollectorAgent, ValueError, get_digest_type_name, TextUtils, GemmaLLM, InlineKeyboardButton, enumerate, len, list, isinstance, timedelta

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\text_utils.py
- Библиотеки: logging, re
- Функции: clean_markdown_text, len, split_text, convert_to_html

## Промпты
### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\main.py
- === РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ===
- Начинаем процедуру завершения работы...
- Режим работы: bot - запуск бота и планировщика, workflow - запуск полного рабочего процесса, legacy - legacy workflow без оркестратора, digest - только формирование дайджеста
- Очистка ресурсов при завершении работы

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\improved_message_handler.py
- Вопрос: {user_message} Контекст (дайджест правовых новостей): {digest["text"]} {recent_data} Дай краткий и точный ответ на вопрос на основе представленного контекста. Если информации недостаточно, так и скажи. Если вопрос касается определенной категории новостей, укажи, что пользователь может получить более подробную информацию по этой категории с помощью команды /category.

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\run_orchestrator_tests.py
- Созданы дайджесты:
- 🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! Оркестратор готов к использованию.
- ⚠️ НЕ ВСЕ ТЕСТЫ ПРОЙДЕНЫ. Требуется исправление ошибок.

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\simplified_period_command.py
- Ошибка формата даты. Используйте формат YYYY-MM-DD (например, 2025-04-01) или ключевые слова 'сегодня'/'вчера'.
- Команда позволяет получить дайджест за указанный период.\n\nФорматы:\n• /period сегодня - дайджест за сегодня\n• /period вчера - дайджест за вчерашний день\n• /period YYYY-MM-DD - дайджест за указанную дату\n• /period YYYY-MM-DD YYYY-MM-DD - дайджест за период\n\nУказание типа (опционально):\n• /period сегодня brief - краткий дайджест (по умолчанию)\n• /period вчера detailed - подробный дайджест\n• /period 2025-04-01 2025-04-10 both - оба типа дайджеста
- Ошибка при разборе даты:

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\run_workflow.py
- Сформируй краткий обзор для категории '{category}' на основе следующих сообщений из правительственных Telegram-каналов: {category_messages} Обзор должен содержать краткое описание ключевых событий и быть информативным. Объем: 1-2 абзаца.
- Проанализируй следующий текст из правительственного Telegram-канала и определи, к какой из следующих категорий он относится: - законодательные инициативы - новая судебная практика - новые законы - поправки к законам Если текст не относится ни к одной из категорий, то верни "другое". Текст сообщения: {message.text} Категория:
- Напиши краткое введение для дайджеста правовых новостей за {today.strftime('%d.%m.%Y')}. Упомяни, что дайджест составлен на основе информации из официальных Telegram-каналов Госдумы, Совета Федерации и Верховного Суда РФ. Объем: 1 абзац.
- \n Проанализируй следующий текст из правительственного Telegram-канала и определи, \n к какой из следующих категорий он относится:\n - законодательные инициативы\n - новая судебная практика\n - новые законы\n - поправки к законам\n \n Если текст не относится ни к одной из категорий, то верни "другое".\n \n Текст сообщения:\n

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_orchestrator.py
- \n🎉 ВСЕ БАЗОВЫЕ ТЕСТЫ ПРОЙДЕНЫ!

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_orchestrator_scenarios.py
- Тесты реальных сценариев использования оркестратора
- \nТесты сценариев работы оркестратора\n
- Тесты различных сценариев работы оркестратора
- Тесты принятия решений оркестратором

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_orchestrator_integration.py
- Тесты интеграции оркестратора
- Тесты интеграции с основным workflow
- \nТесты интеграции оркестратора с существующей системой\n
- Тесты производительности интеграции
- Выполнена задача

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_cross_agent_collaboration.py
- 🎉 ВСЕ ТЕСТЫ CROSS-AGENT COLLABORATION ПРОЙДЕНЫ!
- Компоненты:
- ✅ Агенты успешно взаимодействуют

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\test_proactive_collaboration.py
- \n📊 РЕЗУЛЬТАТЫ ПОЛНОГО WORKFLOW:
- 📊 ИТОГОВЫЕ РЕЗУЛЬТАТЫ:
- \n⚠️ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ
- \n📊 РЕЗУЛЬТАТЫ МОНИТОРИНГА:
- \n🎉 ВСЕ ТЕСТЫ ПРОАКТИВНОЙ КОЛЛАБОРАЦИИ ПРОЙДЕНЫ!
- \n📊 РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ:

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\analyzer.py
- \n Ты - эксперт по правовому анализу. Проанализируй сообщение и определи категорию.\n\n
- \n Создание задачи для агента\n \n Returns:\n Task: Задача CrewAI\n
- \n\n ДОСТУПНЫЕ КАТЕГОРИИ:\n 1. законодательные инициативы - проекты, предложения, рассмотрение в Госдуме\n 2. новые законы - принятые и подписанные законы, вступающие в силу\n 3. поправки к законам - изменения в существующие законы\n 4. новая судебная практика - решения, постановления судов\n 5. другое - не относится к правовым вопросам\n\n АНАЛИЗ:\n Найди ключевые слова и определи стадию процесса.\n\n Если видишь "принят", "подписан", "вступает в силу" + номер закона = "новые законы"\n Если видишь "проект", "рассмотрение", "предложение", "инициатива" = "законодательные инициативы" \n Если видишь "изменения", "поправки", "внесены в" + название закона = "поправки к законам"\n Если видишь "суд", "решение", "постановление", "определение" = "новая судебная практика"\n Иначе = "другое"\n\n СТРОГО отвечай в формате:\n Категория: [одна из 5 категорий точно как написано выше]\n Уверенность: [число 1-5]
- Ты - эксперт по правовому анализу. Проанализируй сообщение и определи категорию. {examples_text if examples else ""} СООБЩЕНИЕ: {message_text} ДОСТУПНЫЕ КАТЕГОРИИ: 1. законодательные инициативы - проекты, предложения, рассмотрение в Госдуме 2. новые законы - принятые и подписанные законы, вступающие в силу 3. поправки к законам - изменения в существующие законы 4. новая судебная практика - решения, постановления судов 5. другое - не относится к правовым вопросам АНАЛИЗ: Найди ключевые слова и определи стадию процесса. Если видишь "принят", "подписан", "вступает в силу" + номер закона = "новые законы" Если видишь "проект", "рассмотрение", "предложение", "инициатива" = "законодательные инициативы" Если видишь "изменения", "поправки", "внесены в" + название закона = "поправки к законам" Если видишь "суд", "решение", "постановление", "определение" = "новая судебная практика" Иначе = "другое" СТРОГО отвечай в формате: Категория: [одна из 5 категорий точно как написано выше] Уверенность: [число 1-5]
- Результаты анализа с информацией о количестве проанализированных сообщений и их категориях

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\agent_registry.py
- \nОбновленный реестр агентов для работы с Intelligent Orchestrator\n
- Все агенты успешно инициализированы

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\collaborative_crew.py
- Получаем существующие CrewAI агенты из наших классов
- ✅ Получены существующие CrewAI агенты:
- \n Синтезируй результаты анализа и критики в итоговый отчет.\n Создай краткое резюме с ключевыми выводами.\n
- ✅ Задача
- \n \n ЗАДАЧА:
- ❌ Не все агенты доступны для коллаборации
- /5\n \n Проанализируй:\n 1. Правовой контекст и терминологию\n 2. Тип правового акта или инициативы\n 3. Стадию законодательного процесса\n 4. Ключевые правовые аспекты\n \n ДОСТУПНЫЕ КАТЕГОРИИ:\n - законодательные инициативы\n - новые законы\n - поправки к законам \n - новая судебная практика\n - другое\n \n Дай детальный анализ с обоснованием.\n
- \n Проанализируй качество дайджеста с точки зрения контентной стратегии.\n \n ТИП ДАЙДЖЕСТА:
- \n Ты
- Ты {task.agent.role}. {task.agent.backstory} ЗАДАЧА: {task.description} ЦЕЛЬ: {task.agent.goal} Выполни задачу качественно и профессионально. Будь конкретен и структурирован.
- ❌ Не все агенты доступны для проверки качества
- ❌ Не все агенты доступны для комплексного анализа
- Агенты недоступны

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\data_collector.py
- Некорректный формат даты:
- сообщений, даты:
- \n Сбор данных за указанный период (формат дат YYYY-MM-DD)\n \n Args:\n start_date_str (str): Начальная дата в формате YYYY-MM-DD\n end_date_str (str): Конечная дата в формате YYYY-MM-DD\n channels (list, optional): Список каналов для сбора (по умолчанию все каналы)\n \n Returns:\n dict: Результаты сбора\n
- \n Создание задачи для агента\n \n Returns:\n Task: Задача CrewAI\n
- Результаты сбора данных с информацией о количестве собранных сообщений
- Ошибка формата даты:
- \n Асинхронный хук, вызываемый после успешного сбора данных\n \n Args:\n collect_result (dict): Результаты сбора данных\n
- \n Интеллектуальный сбор данных с фильтрацией и оптимизацией для существующей БД\n \n Args:\n client (TelegramClient): Клиент Telegram\n channel (str): Имя канала\n start_date (datetime): Начальная дата\n end_date (datetime): Конечная дата\n \n Returns:\n dict: Результаты сбора с дополнительной информацией\n
- \n Метод для глубокого сбора исторических данных\n \n Args:\n channel (str): Имя канала\n start_date (datetime): Начальная дата\n end_date (datetime): Конечная дата\n force_update (bool): Принудительное обновление существующих сообщений\n \n Returns:\n dict: Результаты сбора\n
- \n Асинхронный метод для сбора данных из каналов с поддержкой исторических периодов\n \n Args:\n days_back (int): За сколько дней назад собирать данные\n force_update (bool): Принудительно обновлять существующие сообщения\n start_date (datetime, optional): Начальная дата для сбора\n end_date (datetime, optional): Конечная дата для сбора\n \n Returns:\n dict: Результаты сбора данных\n

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\critic.py
- \n\n КОНТЕКСТНЫЙ АНАЛИЗ:\n\n 1. АНАЛИЗ ИСТОЧНИКА:\n @dumainfo → часто законодательные инициативы и принятые законы\n @sovfedinfo → федеральное законодательство, одобрения СФ\n @vsrf_ru → судебная практика, разъяснения ВС\n @kremlininfo → подписанные президентом законы\n @governmentru → правительственные решения\n\n 2. ТИПИЧНОСТЬ ДЛЯ ИСТОЧНИКА:\n Типично ли такое сообщение для данного канала?\n Соответствует ли категория специализации источника?\n\n 3. ВРЕМЕННЫЕ МАРКЕРЫ:\n Есть ли указания на время (прошлое/настоящее/будущее)?\n Как это влияет на категорию?\n\n ОТВЕТ в формате:\n Контекст: [соответствует/не соответствует источнику]\n Типичность: [типично/нетипично для канала]\n Временной аспект: [актуальное/историческое/планируемое]\n
- \n Ты - аналитик логической последовательности и качества классификации.\n\n ЗАДАЧА: Проверить внутреннюю логику категоризации.\n\n СООБЩЕНИЕ:
- Ты - эксперт по контекстному анализу и медиа-источникам. ЗАДАЧА: Учесть контекст источника при проверке категоризации. СООБЩЕНИЕ: {message_text} ИСТОЧНИК: {channel} ТЕКУЩАЯ КАТЕГОРИЯ: {current_category} КОНТЕКСТНЫЙ АНАЛИЗ: 1. АНАЛИЗ ИСТОЧНИКА: @dumainfo → часто законодательные инициативы и принятые законы @sovfedinfo → федеральное законодательство, одобрения СФ @vsrf_ru → судебная практика, разъяснения ВС @kremlininfo → подписанные президентом законы @governmentru → правительственные решения 2. ТИПИЧНОСТЬ ДЛЯ ИСТОЧНИКА: Типично ли такое сообщение для данного канала? Соответствует ли категория специализации источника? 3. ВРЕМЕННЫЕ МАРКЕРЫ: Есть ли указания на время (прошлое/настоящее/будущее)? Как это влияет на категорию? ОТВЕТ в формате: Контекст: [соответствует/не соответствует источнику] Типичность: [типично/нетипично для канала] Временной аспект: [актуальное/историческое/планируемое]
- \n\n ПРАВОВАЯ ЭКСПЕРТИЗА:\n\n 1. ТЕРМИНОЛОГИЧЕСКИЙ АНАЛИЗ:\n - Правильно ли использованы правовые термины?\n - Соответствует ли терминология российской правовой системе?\n - Нет ли ошибок в понимании правовых процедур?\n\n 2. ПРОЦЕДУРНЫЙ АНАЛИЗ:\n - Законодательные инициативы: проекты, внесение, рассмотрение\n - Новые законы: принятие, подписание, опубликование, вступление в силу\n - Поправки к законам: изменения, дополнения существующих актов\n - Судебная практика: решения, постановления, разъяснения судов\n\n 3. ПРАВОВАЯ ОЦЕНКА:\n На какой стадии правового процесса находится описываемое событие?\n Соответствует ли категория этой стадии?\n\n ОТВЕТ в формате:\n Правовая оценка: [правильно/неправильно/спорно]\n Стадия процесса: [описание стадии]\n Рекомендация: [подтвердить категорию или предложить другую]\n
- \n Ты - эксперт по правовой терминологии и российскому законодательству.\n\n ЗАДАЧА: Проверить правовую точность категоризации сообщения.\n\n СООБЩЕНИЕ:
- Ты - аналитик логической последовательности и качества классификации. ЗАДАЧА: Проверить внутреннюю логику категоризации. СООБЩЕНИЕ: {message_text} ТЕКУЩАЯ КАТЕГОРИЯ: {current_category} АНАЛИЗ КОНСИСТЕНТНОСТИ: 1. ЛОГИЧЕСКАЯ ПРОВЕРКА: - Есть ли явные признаки указанной категории? - Нет ли признаков других категорий? - Логично ли решение о категоризации? 2. ПРИЗНАКИ КАТЕГОРИЙ: Законодательные инициативы: "проект", "предложение", "рассмотрение", "внесен" Новые законы: "принят", "подписан", "вступает в силу", "федеральный закон №" Поправки: "изменения", "внесены в", "дополнен", существующий закон Судебная практика: "суд", "решение", "постановление", "разъяснение" 3. АЛЬТЕРНАТИВНЫЕ КАТЕГОРИИ: Могло ли сообщение относиться к другой категории? Какие признаки за это говорят? ОТВЕТ в формате: Логическая оценка: [логично/нелогично/спорно] Альтернатива: [другая возможная категория или "нет"] Уверенность: [1-5]
- Я проверяю результаты классификации и исправляю ошибки, чтобы обеспечить высокое качество дайджеста.
- \n\n ПРИНЯТИЕ РЕШЕНИЯ:\n\n Проанализируй все три экспертизы и прими взвешенное решение:\n\n 1. Если 2+ экспертизы рекомендуют изменение → ИЗМЕНИТЬ\n 2. Если 2+ экспертизы подтверждают категорию → ПОДТВЕРДИТЬ\n 3. Если мнения разделились → учесть уверенность экспертиз\n\n КАТЕГОРИИ НА ВЫБОР:\n - законодательные инициативы\n - новые законы \n - поправки к законам\n - новая судебная практика\n - другое\n\n ФИНАЛЬНОЕ РЕШЕНИЕ в формате:\n Решение: [подтвердить/изменить]\n Новая категория: [если изменить - укажи какую]\n Уверенность: [1-5]\n Обоснование: [краткое объяснение решения]\n
- \n Проверяет категоризацию сообщений с низкой уверенностью\n \n Args:\n confidence_threshold (int): Проверять только сообщения с уверенностью <= этого значения\n limit (int): Максимальное количество сообщений для проверки\n batch_size (int): Размер пакета для параллельной обработки\n max_workers (int): Максимальное количество потоков\n \n Returns:\n dict: Результаты проверки\n
- Ты - старший эксперт-аналитик, принимающий финальное решение. СООБЩЕНИЕ: {message_text} ТЕКУЩАЯ КАТЕГОРИЯ: {original_category} РЕЗУЛЬТАТЫ ЭКСПЕРТИЗ: 1. Правовая экспертиза: {legal_analysis} 2. Логическая консистентность: {consistency_analysis} 3. Контекстный анализ: {context_analysis} ПРИНЯТИЕ РЕШЕНИЯ: Проанализируй все три экспертизы и прими взвешенное решение: 1. Если 2+ экспертизы рекомендуют изменение → ИЗМЕНИТЬ 2. Если 2+ экспертизы подтверждают категорию → ПОДТВЕРДИТЬ 3. Если мнения разделились → учесть уверенность экспертиз КАТЕГОРИИ НА ВЫБОР: - законодательные инициативы - новые законы - поправки к законам - новая судебная практика - другое ФИНАЛЬНОЕ РЕШЕНИЕ в формате: Решение: [подтвердить/изменить] Новая категория: [если изменить - укажи какую] Уверенность: [1-5] Обоснование: [краткое объяснение решения]
- \n Ты - эксперт по контекстному анализу и медиа-источникам.\n\n ЗАДАЧА: Учесть контекст источника при проверке категоризации.\n\n СООБЩЕНИЕ:
- Ты - эксперт по правовой терминологии и российскому законодательству. ЗАДАЧА: Проверить правовую точность категоризации сообщения. СООБЩЕНИЕ: {message_text} ТЕКУЩАЯ КАТЕГОРИЯ: {current_category} ПРАВОВАЯ ЭКСПЕРТИЗА: 1. ТЕРМИНОЛОГИЧЕСКИЙ АНАЛИЗ: - Правильно ли использованы правовые термины? - Соответствует ли терминология российской правовой системе? - Нет ли ошибок в понимании правовых процедур? 2. ПРОЦЕДУРНЫЙ АНАЛИЗ: - Законодательные инициативы: проекты, внесение, рассмотрение - Новые законы: принятие, подписание, опубликование, вступление в силу - Поправки к законам: изменения, дополнения существующих актов - Судебная практика: решения, постановления, разъяснения судов 3. ПРАВОВАЯ ОЦЕНКА: На какой стадии правового процесса находится описываемое событие? Соответствует ли категория этой стадии? ОТВЕТ в формате: Правовая оценка: [правильно/неправильно/спорно] Стадия процесса: [описание стадии] Рекомендация: [подтвердить категорию или предложить другую]
- \n Ты - старший эксперт-аналитик, принимающий финальное решение.\n\n СООБЩЕНИЕ:
- \n\n РЕЗУЛЬТАТЫ ЭКСПЕРТИЗ:\n 1. Правовая экспертиза:

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\task_queue.py
- Запущена задача
- \n Выполнение отдельной задачи\n \n Args:\n task: Задача для выполнения\n
- \n Отмена задачи\n \n Args:\n task_id: ID задачи для отмены\n \n Returns:\n True если задача была отменена\n
- Задача в очереди с дополнительной информацией
- \n Проверка выполнения зависимостей задачи\n \n Args:\n task: Задача для проверки\n \n Returns:\n True если все зависимости выполнены\n
- Задача

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\orchestrator.py
- Создаем новые дайджесты на основе собранных и проанализированных данных
- Усиление плана задачами коллаборации
- Я — продвинутый ИИ-планировщик, который понимает архитектуру системы \n обработки новостных сообщений и принимает intelligent решения.
- \n Выполнение проактивной коллаборации на основе рекомендаций\n \n Args:\n recommendations: Рекомендации по коллаборации\n context: Контекст системы\n \n Returns:\n Результаты коллаборации\n
- .\n Для каждой задачи объясни WHY она нужна и в каком ПОРЯДКЕ должна выполняться.\n \n ОСОБЕННОСТИ СЦЕНАРИЕВ:\n - daily_workflow: полный цикл (сбор → анализ → проверка → дайджест)\n - urgent_update: быстрое обновление критически важной информации\n - full_analysis: глубокий анализ с акцентом на качество\n - digest_only: только создание дайджеста из существующих данных\n \n ВАЖНЫЕ ПРАВИЛА:\n 1. Если есть неанализированные сообщения → нужен MESSAGE_ANALYSIS\n 2. Если много сообщений с низкой уверенностью → нужен CATEGORIZATION_REVIEW\n 3. Если рекомендована коллаборация → усиль план коллаборативными задачами\n 4. Всегда объясняй свои решения\n 5. Учитывай зависимости между задачами\n 6. Оптимизируй для конкретного сценария\n \n Ответь в формате: ЗАДАЧА_1: reasoning, ЗАДАЧА_2: reasoning, и т.д.\n
- \n Анализ результатов выполнения с учетом коллаборации\n \n Args:\n results: Список результатов выполнения задач\n scenario: Сценарий выполнения\n context: Контекст системы\n collaboration_results: Результаты коллаборации\n \n Returns:\n Финальный результат с метриками и рекомендациями\n
- Результаты intelligent планирования и выполнения с метриками и рекомендациями
- Приоритеты задач
- Результаты планирования и выполнения с метриками и рекомендациями
- Обновляем существующие дайджесты новыми проанализированными данными
- Логирование влияния коллаборации на результаты
- JSON план выполнения с задачами и обоснованием
- задачах
- Задача
- \n \n ДОСТУПНЫЕ ТИПЫ ЗАДАЧ:\n 1. DATA_COLLECTION - сбор новых сообщений из Telegram каналов\n 2. MESSAGE_ANALYSIS - анализ и категоризация сообщений\n 3. CATEGORIZATION_REVIEW - проверка и улучшение категоризации критиком\n 4. DIGEST_CREATION - создание новых дайджестов\n 5. DIGEST_UPDATE - обновление существующих дайджестов\n \n ТВОЯ ЗАДАЧА:\n Проанализируй ситуацию и создай optimal план выполнения для сценария
- \n Генерация рекомендаций на основе результатов выполнения\n \n Args:\n results: Результаты выполнения задач\n context: Контекст системы\n collaboration_results: Результаты коллаборации\n \n Returns:\n Список рекомендаций\n

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\digester.py
- \n Создание задачи для агента\n \n Returns:\n Task: Задача CrewAI\n
- \n \n ЗАДАЧА: Создай
- 🎯 ПРИОРИТЕТЫ КОНТЕНТА:
- СОЗДАНИЕ {'КРАТКОГО' if digest_type == 'brief' else 'ПОДРОБНОГО'} ОБЗОРА КАТЕГОРИИ С УЧЕТОМ СТРАТЕГИИ: СТРАТЕГИЧЕСКИЕ УКАЗАНИЯ: - Приоритет категории: {category_priority} из {len(strategy['category_order'])} - Стиль: {', '.join(strategy['style_guidelines'][:3])} - Акценты: {', '.join(relevant_emphasis) if relevant_emphasis else 'стандартная подача'} - Подход: {strategy['approach']} КАТЕГОРИЯ: {category} КОЛИЧЕСТВО СООБЩЕНИЙ: {len(messages)} СООБЩЕНИЯ ДЛЯ АНАЛИЗА: {self._format_messages_for_llm(messages, max_messages=10 if digest_type == 'detailed' else 5)} ЗАДАЧА: Создай {digest_type} обзор категории с учетом стратегических указаний ТРЕБОВАНИЯ: {"- Краткость: 1-2 предложения на новость" if digest_type == "brief" else "- Подробность: анализ, контекст, последствия"} - Следуй стратегическим акцентам - Используй рекомендованный стиль - Учитывай приоритет категории РЕЗУЛЬТАТ: профессиональный текст обзора категории
- Рассчитывает важность категории для дайджеста
- акценты:
- \n - Юридическая точность + доступность\n - Структурированная подача\n \n 3. ЧИТАТЕЛЬСКАЯ ЦЕННОСТЬ:\n - Что практически важно для аудитории?\n - Какие выводы и связи стоит подчеркнуть?\n - Как сделать информацию действенной?\n \n ДАЙ РЕКОМЕНДАЦИИ в формате:\n Структура: [порядок категорий по важности]\n Акценты: [на чем сделать упор в каждой категории]\n Стиль: [тон и подход к изложению]\n Приоритеты: [что выделить особо]\n
- Составь краткий обзор новостей категории '{category}' на основе следующих сообщений: {messages_text} Обзор должен: 1. Объединить связанные сообщения 2. Упомянуть источники (каналы) 3. Сохранить важные детали 4. Использовать **полужирное выделение** для ключевых терминов 5. Быть 2-3 абзаца длиной
- Напиши краткое вступление к {"краткому" if is_brief else "подробному"} дайджесту правовых новостей за {period_text}. Информация для вступления: - Период: {period_text} - Всего сообщений: {total_messages} - Распределение по категориям: {categories_info} Вступление должно быть лаконичным (1-2 абзаца) и содержать общую характеристику новостей за этот период. {"Упомяни, что это краткая версия, и полный текст доступен по ссылкам." if is_brief else "Упомяни, что это подробная версия дайджеста."}
- Извлекает акценты через поиск ключевых слов
- Недавно принятые и вступившие в силу законодательные акты
- , атрибуты=
- \n \n ЗАДАЧА: Создать стратегию для оптимального дайджеста\n \n УЧИТЫВАЙ:\n 1. ПРИОРИТИЗАЦИЯ КОНТЕНТА:\n - Какие категории наиболее важны для читателей?\n - Что должно быть в начале дайджеста?\n - Как сбалансировать объем разных категорий?\n \n 2. СТИЛЬ И ПОДАЧА:\n
- Используются fallback акценты
- Извлекает приоритеты через поиск ключевых слов
- Результаты создания дайджеста с полным текстом
- дайджестов для даты
- Используются fallback приоритеты
- - Краткий формат: основные факты, минимум деталей
- Найдены приоритеты:
- приоритеты:
- \n - Акценты:
- Найдены акценты:
- ПЛАНИРОВАНИЕ КОНТЕНТНОЙ СТРАТЕГИИ ДАЙДЖЕСТА: Ты - стратег контент-планирования для правового дайджеста. ИСХОДНЫЕ ДАННЫЕ: - Дата: {date.strftime('%d.%m.%Y')} - Период: {days_back} {'день' if days_back == 1 else 'дней'} - Тип дайджеста: {'краткий' if digest_type == 'brief' else 'подробный'} - Целевая аудитория: {target_audience} - Фокус на категории: {focus_category or 'нет'} - Всего сообщений: {total_messages} РАСПРЕДЕЛЕНИЕ ПО КАТЕГОРИЯМ: {self._format_category_stats(category_analysis)} ЗАДАЧА: Создать стратегию для оптимального дайджеста УЧИТЫВАЙ: 1. ПРИОРИТИЗАЦИЯ КОНТЕНТА: - Какие категории наиболее важны для читателей? - Что должно быть в начале дайджеста? - Как сбалансировать объем разных категорий? 2. СТИЛЬ И ПОДАЧА: {"- Краткий формат: основные факты, минимум деталей" if digest_type == "brief" else "- Подробный формат: анализ, контекст, последствия"} - Юридическая точность + доступность - Структурированная подача 3. ЧИТАТЕЛЬСКАЯ ЦЕННОСТЬ: - Что практически важно для аудитории? - Какие выводы и связи стоит подчеркнуть? - Как сделать информацию действенной? ДАЙ РЕКОМЕНДАЦИИ в формате: Структура: [порядок категорий по важности] Акценты: [на чем сделать упор в каждой категории] Стиль: [тон и подход к изложению] Приоритеты: [что выделить особо]
- Финальная стратегия: приоритеты=
- \n ПЛАНИРОВАНИЕ КОНТЕНТНОЙ СТРАТЕГИИ ДАЙДЖЕСТА:\n \n Ты - стратег контент-планирования для правового дайджеста.\n \n ИСХОДНЫЕ ДАННЫЕ:\n - Дата:
- \n Обновляет все дайджесты, содержащие указанную дату\n \n Args:\n date (datetime): Дата для обновления дайджестов\n \n Returns:\n dict: Результаты обновления\n
- , акценты=
- Найдены существующие дайджесты за сегодня: brief_id=
- ⭐ АКЦЕНТЫ:
- Дайджесты, содержащие дату
- \n Инструмент для создания дайджеста с расширенными параметрами\n \n Args:\n date (datetime, optional): Дата дайджеста (по умолчанию сегодня)\n days_back (int): Количество дней для сбора сообщений\n digest_type (str): Тип дайджеста: "brief", "detailed", "both"\n update_existing (bool): Обновлять существующий дайджест или создать новый\n focus_category (str, optional): Фокус на определенную категорию\n channels (list, optional): Список каналов для фильтрации\n keywords (list, optional): Ключевые слова для фильтрации\n digest_id (int, optional): ID существующего дайджеста для обновления\n \n Returns:\n dict: Результаты создания дайджеста\n
- \n - Следуй стратегическим акцентам\n - Используй рекомендованный стиль\n - Учитывай приоритет категории\n \n РЕЗУЛЬТАТ: профессиональный текст обзора категории\n
- Решения и разъяснения судов, создающие прецеденты
- Доступные атрибуты:

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\llm\qwen_model.py
- Класс для работы с моделью Qwen2.5
- Классифицируй следующий текст по одной из категорий: {', '.join(categories)}. Текст: {text} Категория:
- \nИнтерфейс для работы с моделью Qwen2.5 через LLM Studio\n

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\database\db_manager.py
- \n Находит все дайджесты за сегодня\n \n Args:\n digest_type (str, optional): Тип дайджеста для фильтрации\n \n Returns:\n list: Список дайджестов\n
- \n Поиск дайджестов по параметрам с улучшенной обработкой типов даты\n
- \n Сохранение дайджеста с секциями\n \n Args:\n date (datetime): Дата дайджеста\n text (str): Полный текст дайджеста\n sections (dict): Словарь секций {категория: текст}\n digest_type (str): Тип дайджеста: "brief" (краткий) или "detailed" (подробный)\n \n Returns:\n dict: Информация о созданном дайджесте\n
- \n Получение распределения сообщений по категориям\n \n Args:\n days_back: За сколько дней анализировать\n \n Returns:\n Словарь {категория: количество}\n
- \n Дополнительные методы для оптимизированной работы с БД\n
- Менеджер для работы с базой данных
- \n Находит все дайджесты, которые включают указанную дату\n

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\llm\gemma_model.py
- Класс для работы с моделью Gemma 3
- Создай краткое резюме следующего текста: {text} Резюме должно быть информативным, структурированным и не превышать 3-4 абзаца.
- \nИнтерфейс для работы с моделью Gemma 3 через LLM Studio\n

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\scheduler\jobs.py
- Задача анализа сообщений завершена
- Агенты не поддерживают CrewAI интерфейс, Crew не инициализирована
- Задача сбора данных
- Задача обновления флагов is_today завершилась с ошибкой:
- Задача сбора данных завершена:
- Задача создания дайджеста
- Задача обновления дайджестов завершена:
- === РЕЗУЛЬТАТЫ ЕЖЕДНЕВНОГО ПРОЦЕССА ===
- \nНастройка и управление задачами по расписанию\n
- Обновлены дайджесты:
- Ежедневная задача полного рабочего процесса через оркестратор
- Задача обновления дайджестов при получении новых сообщений
- Оркестрированная задача сбора данных завершена:
- Задача обновления флагов is_today
- Задача сбора данных через оркестратор
- Задача создания дайджеста завершена:
- Задача анализа сообщений
- Задача обновления флагов is_today успешно выполнена. Обновлено:
- Созданы дайджесты:

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\improved_message_handler.py
- Вопрос: {user_message} Контекст (дайджест правовых новостей): {digest["text"]} {recent_data} Дай краткий и точный ответ на вопрос на основе представленного контекста. Если информации недостаточно, так и скажи. Если вопрос касается определенной категории новостей, укажи, что пользователь может получить более подробную информацию по этой категории с помощью команды /category.

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\period_command.py
- Ошибка формата даты. Используйте формат YYYY-MM-DD (например, 2025-04-01) или ключевые слова 'сегодня'/'вчера'.
- Команда позволяет получить дайджест за указанный период.\n\nФорматы:\n• /period сегодня - дайджест за сегодня\n• /period вчера - дайджест за вчерашний день\n• /period YYYY-MM-DD - дайджест за указанную дату\n• /period YYYY-MM-DD YYYY-MM-DD - дайджест за период\n\nУказание типа (опционально):\n• /period сегодня brief - краткий дайджест (по умолчанию)\n• /period вчера detailed - подробный дайджест\n• /period 2025-04-01 both - оба типа дайджеста\n• /period 2025-04-01 2025-04-10 both - оба типа дайджеста
- Ошибка при разборе даты:
- Даты не были правильно преобразованы

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\helpers.py
- \n Преобразует дату в начало дня (00:00:00)\n \n Args:\n date_obj (datetime|date): Объект даты или datetime\n \n Returns:\n datetime: datetime с временем 00:00:00\n
- \n Преобразует дату в конец дня (23:59:59)\n \n Args:\n date_obj (datetime|date): Объект даты или datetime\n \n Returns:\n datetime: datetime с временем 23:59:59\n
- \n Парсит строку с датой в объект datetime\n \n Args:\n date_str (str): Строка с датой\n format (str): Формат даты\n \n Returns:\n datetime: Объект datetime\n
- \n Приводит дату к нормализованному виду (без часового пояса)\n \n Args:\n date_obj (datetime|date): Объект даты или datetime для нормализации\n \n Returns:\n datetime: Нормализованный объект datetime без часового пояса\n

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\telegram_session_manager.py
- \n Закрывает все активные клиенты Telegram, которые были получены через этот менеджер.\n
- Все активные клиенты Telegram закрыты.

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\handlers.py
- Ошибка в формате даты:
- 📊 Доступные дайджесты:\n\nВыберите дайджест для просмотра:
- Дайджесты еще не сформированы.
- Обрабатываем категорию
- Неверный формат конечной даты
- \nОбновленный обработчик колбэков для работы с интерактивными кнопками\n
- Неверный формат начальной даты
- Дайджесты за
- Неверный формат даты

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\learning_manager.py
- \nМенеджер обучающих примеров для работы с примерами категоризации\n
- Менеджер для работы с обучающими примерами категоризации новостей

### C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\text_utils.py
- \nУтилиты для обработки текста\n
- \\\\([.()[\\]{}])

## Бизнес-требования
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
Ошибка вызова LLM: Error code: 404 - {'detail': 'Not Found'}
## Пустые файлы
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\agents\__init__.py
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\config\__init__.py
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\database\__init__.py
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\scheduler\__init__.py
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\telegram_bot\__init__.py
C:\Users\aplyg\PycharmProjects\AI_Risk_Assessment_backup_ver12.15_WORK_Ann_fixes (2)\Lawdigest_bot\utils\__init__.py
