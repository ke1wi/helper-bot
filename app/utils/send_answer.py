from typing import Union
from aiogram.types import Message, CallbackQuery


async def send_answer(update: Union[Message, CallbackQuery], message: str) -> None:
    if isinstance(update, Message):
        await update.reply(message)
    else:
        await update.answer(message)
