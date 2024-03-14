from aiogram.filters.callback_data import CallbackData


class BirthdaySendApprove(CallbackData, prefix="birthday"):
    done: bool


class TodoApprove(CallbackData, prefix="todo"):
    done: bool
