from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

from app.utils.callbacks.registration import (
    Approve,
    Edit,
    Cancel,
)


async def registration_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Підтвердити ✅", callback_data=Approve())
    builder.button(text="Переробити ✏️", callback_data=Edit())
    builder.button(text="Відміна ❌", callback_data=Cancel())

    builder.adjust(2, 1)
    return builder.as_markup()


async def registration_cancel_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Відміна ❌", callback_data=Cancel())

    return builder.as_markup()
