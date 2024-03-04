from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


def get_approve_birthday_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="Надіслати привітання в чат", callback_data="SENDCONGRATS"),
        InlineKeyboardButton(text="Ігнорувати", callback_data="IGNORE")
    )

    return builder.as_markup()
