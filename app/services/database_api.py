from types import TracebackType
from typing import Dict, Optional, Type, Union

from redis.asyncio import Redis


class DatabaseAPI:

    _host: str = "localhost"
    _port: int = 6379
    _db: Union[str, int] = 0
    _password: Optional[str] = None

    _client: Redis

    def __init__(self) -> None:
        self._client = Redis(
            host='redis-16556.c304.europe-west1-2.gce.cloud.redislabs.com',
            port=16556,
            password='22XHHR2yuwIUc4DJQyvFE2ECfWxOYTBH'
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
