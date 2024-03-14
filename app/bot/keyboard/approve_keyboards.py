from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from app.bot.keyboard.types.approves import BirthdaySendApprove, TodoApprove


def get_approve_birthday_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Надіслати привітання в чат", callback_data=BirthdaySendApprove(done=True),
    )
    builder.button(
        text="Ігнорувати", callback_data=BirthdaySendApprove(done=False),
    )

    return builder.as_markup()


def get_approve_todo_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Все правильно", callback_data=TodoApprove(done=True),
    )
    builder.button(
        text="Упс, треба виправити", callback_data=TodoApprove(done=False),
    )

    return builder.as_markup()
