from types import TracebackType
from typing import Optional, Type
from app.settings import settings

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection




class DatabaseAPI:

    _collection: Collection

    def __init__(self) -> None:
        self._client = AsyncIOMotorClient(
            settings.MONGO_URI
        )
        self._collection = self._client.get_database("HelperBot").get_collection("TODO")

    async def __aenter__(self) -> Collection:
        return self._collection

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        await self.close()

    async def close(self) -> None:
        self._client.close()
