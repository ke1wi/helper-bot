from typing import Optional

from pydantic import AnyUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEVELOPMENT: bool = False
    DEBUG: bool = True
    NGROK_AUTHTOKEN: Optional[SecretStr] = None

    TOKEN: SecretStr
    CAPTAIN_ID: int
    VICE_CAPTAIN_ID: int
    TELEGRAM_SECRET: SecretStr
    BASE_URL: AnyUrl = AnyUrl("http://localhost:8000")
    WEBHOOK_PATH: str = "/webhook"

    POSTGRES_URI: str

    @property
    def WEBHOOK_URL(self) -> str:
        return f"{self.BASE_URL}{self.WEBHOOK_PATH}"

    model_config = SettingsConfigDict(
        env_file=(".env", "stack.env"), env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()  # ignore: [call-arg]
