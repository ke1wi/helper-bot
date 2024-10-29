from aiogram_dialog import Window, ShowMode

from aiogram_dialog.widgets.kbd import Button, Cancel, Row
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import MessageInput
from app.utils.states.chat import Chat
from aiogram.types import ContentType
from app.bot.dialogs.chat import (
    captain_choosen,
    vice_captain_choosen,
    message_handler,
)

choose_window = Window(
    Const("Кому пишемо?"),
    Row(
        Button(Const("Старості"), id="captain_button", on_click=captain_choosen),
        Button(Const("Заму"), id="vice_button", on_click=vice_captain_choosen),
    ),
    Cancel(Const("Відміна ❌"), show_mode=ShowMode.DELETE_AND_SEND),
    state=Chat.choose,
)
message_window = Window(
    Const("Напишіть Ваше повідомлення:"),
    MessageInput(message_handler, content_types=ContentType.TEXT),
    Cancel(Const("Відміна ❌"), show_mode=ShowMode.DELETE_AND_SEND),
    state=Chat.message,
)
