from types import TracebackType
from typing import Dict, Optional, Self, Type, Union
import asyncio
import logging

from redis.asyncio import Redis
from redis.exceptions import ConnectionError


class DatebaseAPI:

    _host: str = "localhost"
    _port: int = 6379
    _db: Union[str, int] = 0
    _password: Optional[str] = None

    _client: Redis

    def __init__(self) -> None:
        self._client = Redis(
            host=self._host,
            port=self._port,
            db=self._db,
            password=self._password
        )

    @property
    def client_info(self) -> Dict:
        return {"HOST": self._host, "PORT": self._port, "DB": self._db}

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

#            USAGE EXAMPLE 
# async def test():
#     try:
#         async with DatebaseAPI() as database_api:
#             uuid = await database_api.get("id")
#             print(uuid)
#     except ConnectionError as err:
#         logging.error(msg=err)
#
# asyncio.run(test())