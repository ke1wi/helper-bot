from types import TracebackType
from typing import Optional, Type
from app.settings import settings

from pymongo import MongoClient


class DatabaseAPI:
    _client: MongoClient

    def __init__(self) -> None:
        self._client = MongoClient(settings.MONGO_URI)

    async def __aenter__(self) -> MongoClient:
        return self._client

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        await self.close()

    async def close(self) -> None:
        self._client.close()
