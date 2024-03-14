from app.bot.enums.todo_types import TodoTypes

from aiogram.filters.callback_data import CallbackData


class SelectTodoType(CallbackData, prefix="todo"):
    todo_type: str