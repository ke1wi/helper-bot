from app.utils.database.models.base import TimedBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, BigInteger
from app.utils.enums.role import Role
from datetime import date


class User(TimedBase):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column("telegram_id", BigInteger)
    email: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    surname: Mapped[str]
    number: Mapped[str] = mapped_column(unique=True)
    birthday: Mapped[date]
    role: Mapped[Role] = mapped_column(
        Enum(Role, native_enum=False), nullable=True, default=Role.STUDENT
    )
