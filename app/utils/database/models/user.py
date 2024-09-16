from app.utils.database.models.base import TimedBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum
from app.utils.enums.role import Role



class User(TimedBase):
    __tablename__ = "users"

    telegram_id: Mapped[int]
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    number: Mapped[str] = mapped_column(unique=True)
    role: Mapped[Role] = mapped_column(Enum(Role, native_enum=False), nullable=True)
