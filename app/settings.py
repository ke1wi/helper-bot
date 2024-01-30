import os 

# class Settings:
    
#     TOKEN: str = os.getenv("TOKEN")
#     CHANNEL_URL: str = os.getenv("CHANNEL_URL")
#     CHAT_ID: int = int(os.getenv("CHAT_ID"))
#     ADMIN_ID: str = os.getenv("ADMIN_ID")

from pydantic import AnyUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEVELOPMENT: bool = True
    DEBUG: bool = True
    TOKEN: SecretStr
    CHAT_ID: int
    TELEGRAM_SECRET: SecretStr
    BASE_URL: AnyUrl = AnyUrl("http://localhost:8000")
    WEBHOOK_PATH: str
    ADMIN_ID: str = os.getenv("ADMIN_ID")
    @property
    def WEBHOOK_URL(self) -> str:
        return f"{self.BASE_URL}{self.WEBHOOK_PATH}"

    model_config = SettingsConfigDict(
        env_file=('.env', 'stack.env'), env_file_encoding='utf-8', extra='ignore')



settings = Settings()  # type: ignore[call-arg]