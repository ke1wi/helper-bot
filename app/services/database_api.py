from types import TracebackType
from typing import Dict, Optional, Type, Union
from app.settings import settings

from redis.asyncio import Redis


class DatabaseAPI:
    
    _client: Redis

    def __init__(self) -> None:
        self._client = Redis(
            host=settings.REDIS_HOST.get_secret_value(),
            port=settings.REDIS_PORT,
            password=settings.REDIS_PASSWORD.get_secret_value()
        )

    async def __aenter__(self) -> Redis:
        return self._client

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        await self.close()

    async def close(self) -> None:
        await self._client.aclose()
