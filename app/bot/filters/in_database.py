from typing import Union

from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message
from app.utils.database.api import get_user_by_telegram_id
from app.utils.database.models.user import User
from app.utils.send_answer import send_answer


class InDatabase(Filter):
    async def __call__(self, update: Union[Message, CallbackQuery]) -> User | None:
        if user := await get_user_by_telegram_id(update.from_user.id):
            return user
        else:
            await send_answer(update, "Спочатку зареєтруйтесь! [/reg]")
