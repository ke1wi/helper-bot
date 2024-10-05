from types import TracebackType
from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker
from app.settings import settings
from typing import Optional, Type


class Database_API:
    def __init__(self) -> None:
        self.async_engine: AsyncEngine = create_async_engine(settings.POSTGRES_URI)
        self.async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
            self.async_engine, expire_on_commit=False
        )

    async def __aenter__(self) -> AsyncSession:
        async with self.async_session() as session:
            self.session: AsyncSession = session
            return self.session

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.close()

    async def close(self) -> None:
        await self.session.aclose()
