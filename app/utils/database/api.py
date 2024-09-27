from typing import List, Tuple
from app.utils.database.models.user import User
from app.utils.database.engine import Database_API
from sqlalchemy.future import select
from sqlalchemy import Row, Sequence


async def create_user(user: User) -> None:
    async with Database_API() as session:
        session.add(user)
        await session.commit()


async def get_user_by_email(email: str) -> Row[Tuple[User]] | None:
    async with Database_API() as session:
        return (
            await session.execute(select(User).filter(User.email == email))
        ).first()


async def get_users() -> Sequence[User]:
    async with Database_API() as session:
        return (await session.execute(select(User))).scalars().all()
