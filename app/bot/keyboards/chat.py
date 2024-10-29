from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


async def deputy_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    return builder.as_markup()
