from aiogram_dialog import Dialog
from app.bot.dialogs.windows.chat import choose_window, message_window
from app.bot.dialogs.windows.registration import (
    email_window,
    name_window,
    surname_window,
    number_window,
    birthday_window,
    info_window,
    database_info_window,
)

chat_dialog = Dialog(choose_window, message_window)
registration_dialog = Dialog(
    email_window,
    name_window,
    surname_window,
    number_window,
    birthday_window,
    info_window,
    database_info_window,
)
