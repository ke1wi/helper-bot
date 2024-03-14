from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from app.bot.keyboard.types.todo import SelectTodoType
from app.bot.enums.todo_types import TodoTypes


def get_todo_type_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Дедлайн",
        callback_data=SelectTodoType(todo_type=TodoTypes.DEADLINE)
    )
    builder.button(
        text="Нагадування",
        callback_data=SelectTodoType(todo_type=TodoTypes.REMIND)
    )

    return builder.as_markup()
