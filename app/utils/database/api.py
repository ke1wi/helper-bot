from typing import List, Optional
from app.utils.database.models.user import User
from app.utils.database.engine import Database_API
from sqlalchemy.future import select


async def create_user(user: User) -> None:
    async with Database_API() as session:
        session.add(user)
        await session.commit()


async def get_user_by_email(email: str) -> Optional[User]:
    async with Database_API() as session:
        result = await session.execute(select(User).filter(User.email == email))
        return result.scalar_one_or_none()


async def get_users() -> List[User]:
    async with Database_API() as session:
        return (await session.execute(select(User))).scalars().all()
