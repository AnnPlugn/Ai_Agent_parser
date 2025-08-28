
import os
from pathlib import Path
import logging
from enum import Enum
from dataclasses import dataclass
from typing import Optional

# Настройка логирования
logger = logging.getLogger(__name__)

def load_env_file():
    """Загрузка .env файла"""
    try:
        from dotenv import load_dotenv
        # Ищем .env файл в текущей директории и родительских
        env_loaded = load_dotenv(verbose=True)

        if not env_loaded:
            current_dir = Path.cwd()
            for parent in [current_dir] + list(current_dir.parents):
                env_file = parent / ".env"
                if env_file.exists():
                    load_dotenv(env_file, verbose=True)
                    logger.info(f"📁 Загружен .env файл: {env_file}")
                    break
            else:
                logger.warning("⚠️ .env файл не найден, используются системные переменные окружения")
        else:
            logger.info("📁 .env файл успешно загружен")
    except ImportError:
        logger.warning("⚠️ python-dotenv не установлен, используются системные переменные окружения")
    except Exception as e:
        logger.error(f"⚠️ Ошибка загрузки .env файла: {e}")

class LLMProvider(Enum):
    """Поддерживаемые провайдеры LLM"""
    LM_STUDIO = "lm_studio"
    GIGACHAT = "gigachat"
    DEEPSEEK = "deepseek"

@dataclass
class LLMConfig:
    """Конфигурация LLM клиента"""
    base_url: str
    model: str
    temperature: float
    max_tokens: int
    timeout: int
    max_retries: int
    retry_delay: float
    provider: LLMProvider = LLMProvider.LM_STUDIO
    api_key: Optional[str] = None
    cert_file: Optional[str] = None
    key_file: Optional[str] = None
    top_p: float = 0.2
    verify_ssl_certs: bool = False
    profanity_check: bool = False
    streaming: bool = True

    @classmethod
    def create_default(cls) -> 'LLMConfig':
        """Создание конфигурации по умолчанию (fallback для обратной совместимости)"""
        return cls(
            base_url=os.getenv("LLM_BASE_URL", "http://127.0.0.1:1234"),
            model=os.getenv("LLM_MODEL", "qwen3-4b"),
            temperature=float(os.getenv("LLM_TEMPERATURE", "0.1")),
            max_tokens=int(os.getenv("LLM_MAX_TOKENS", "8192")),
            timeout=int(os.getenv("LLM_TIMEOUT", "120")),
            max_retries=int(os.getenv("MAX_RETRY_COUNT", "3")),
            retry_delay=float(os.getenv("LLM_RETRY_DELAY", "1.0")),
            provider=LLMProvider.LM_STUDIO
        )

    @classmethod
    def from_env(cls, **overrides) -> 'LLMConfig':
        """Альтернативный метод создания конфигурации напрямую из переменных окружения"""
        provider_str = os.getenv("LLM_PROVIDER", "lm_studio").lower()
        provider_mapping = {
            "lm_studio": LLMProvider.LM_STUDIO,
            "gigachat": LLMProvider.GIGACHAT,
            "deepseek": LLMProvider.DEEPSEEK
        }
        provider = provider_mapping.get(provider_str, LLMProvider.LM_STUDIO)

        if provider == LLMProvider.GIGACHAT:
            base_url = os.getenv("GIGACHAT_BASE_URL", "https://gigachat-ift.sberdevices.delta.sbrf.ru/v1")
            model = os.getenv("GIGACHAT_MODEL", "GigaChat-Max")
            cert_path = os.getenv("GIGACHAT_CERT_PATH", "lib/llm/client_cert.pem")
            key_path = os.getenv("GIGACHAT_KEY_PATH", "lib/llm/client_key.pem")

            if not os.path.isabs(cert_path):
                cert_path = os.path.join(os.getcwd(), cert_path)
            if not os.path.isabs(key_path):
                key_path = os.path.join(os.getcwd(), key_path)

            cert_file = cert_path
            key_file = key_path
            top_p = float(os.getenv("GIGACHAT_TOP_P", "0.2"))
            verify_ssl_certs = os.getenv("GIGACHAT_VERIFY_SSL", "false").lower() == "true"
            profanity_check = os.getenv("GIGACHAT_PROFANITY_CHECK", "false").lower() == "true"
            streaming = os.getenv("GIGACHAT_STREAMING", "true").lower() == "true"
            api_key = None
        elif provider == LLMProvider.DEEPSEEK:
            base_url = os.getenv("LLM_BASE_URL", "https://api.proxyapi.ru/deepseek")
            model = os.getenv("LLM_MODEL", "deepseek-chat")
            cert_file = None
            key_file = None
            top_p = float(os.getenv("LLM_TOP_P", "0.2"))
            verify_ssl_certs = os.getenv("LLM_VERIFY_SSL", "true").lower() == "true"
            profanity_check = False
            streaming = os.getenv("LLM_STREAMING", "true").lower() == "true"
            api_key = os.getenv("DEEPSEEK_API_KEY")
        else:
            base_url = os.getenv("LLM_BASE_URL", "http://127.0.0.1:1234")
            model = os.getenv("LLM_MODEL", "qwen3-4b")
            cert_file = None
            key_file = None
            top_p = float(os.getenv("LLM_TOP_P", "0.2"))
            verify_ssl_certs = False
            profanity_check = False
            streaming = True
            api_key = None

        temperature = float(os.getenv("LLM_TEMPERATURE", "0.1"))
        max_tokens = int(os.getenv("LLM_MAX_TOKENS", "8192"))
        timeout = int(os.getenv("LLM_TIMEOUT", "120"))
        max_retries = int(os.getenv("MAX_RETRY_COUNT", "3"))
        retry_delay = float(os.getenv("LLM_RETRY_DELAY", "1.0"))

        return cls(
            base_url=overrides.get('base_url', base_url),
            model=overrides.get('model', model),
            temperature=overrides.get('temperature', temperature),
            max_tokens=overrides.get('max_tokens', max_tokens),
            timeout=overrides.get('timeout', timeout),
            max_retries=overrides.get('max_retries', max_retries),
            retry_delay=overrides.get('retry_delay', retry_delay),
            provider=overrides.get('provider', provider),
            api_key=overrides.get('api_key', api_key),
            cert_file=overrides.get('cert_file', cert_file),
            key_file=overrides.get('key_file', key_file),
            top_p=overrides.get('top_p', top_p),
            verify_ssl_certs=overrides.get('verify_ssl_certs', verify_ssl_certs),
            profanity_check=overrides.get('profanity_check', profanity_check),
            streaming=overrides.get('streaming', streaming)
        )
