from aiogram_dialog import Window

from aiogram_dialog.widgets.kbd import Button, Cancel, Row
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import MessageInput
from app.utils.states.registration import Registration
from app.bot.dialogs.registration import (
    email_handler,
    name_handler,
    surname_handler,
    number_handler,
    birthday_handler,
    approve,
    edit,
    cancel,
    database_approve,
    database_edit,
)


email_window = Window(
    Const("Введіть електронну пошту:"),
    Cancel(Const("Відміна ❌"), on_click=cancel),
    MessageInput(email_handler),
    state=Registration.email,
)

name_window = Window(
    Const("Введіть імʼя:"),
    Cancel(Const("Відміна ❌"), on_click=cancel),
    MessageInput(name_handler),
    state=Registration.name,
)
surname_window = Window(
    Const("Введіть прізвище:"),
    Cancel(Const("Відміна ❌"), on_click=cancel),
    MessageInput(surname_handler),
    state=Registration.surname,
)
number_window = Window(
    Const("Введіть телефон:\nПриклад: <b>0501234567</b>"),
    Cancel(Const("Відміна ❌"), on_click=cancel),
    MessageInput(number_handler),
    state=Registration.number,
)
birthday_window = Window(
    Const("Введіть дату народження:"),
    Cancel(Const("Відміна ❌"), on_click=cancel),
    MessageInput(birthday_handler),
    state=Registration.birthday,
)
info_window = Window(
    Const("Перевір чи все правильно:\n"),
    Format("Імʼя: <b>{dialog_data[user][name]}</b>"),
    Format("Прізвище: <b>{dialog_data[user][surname]}</b>"),
    Format("Електронна пошта: <b>{dialog_data[user][email]}</b>"),
    Format("Номер телефону: <b>{dialog_data[user][number]}</b>"),
    Format("Дата народження: <b>{dialog_data[user][birthday]}</b>"),
    Row(
        Button(Const("Підтвердити ✅"), id="approve", on_click=approve),
        Button(Const("Переробити ✏️"), id="edit", on_click=edit),
    ),
    Cancel(Const("Відміна ❌")),
    state=Registration.info,
    parse_mode="HTML",
)
database_info_window = Window(
    Const("Ти вже є в базі"),
    Const("Перевір чи все правильно:\n"),
    Format("Імʼя: <b>{dialog_data[user][name]}</b>"),
    Format("Прізвище: <b>{dialog_data[user][surname]}</b>"),
    Format("Електронна пошта: <b>{dialog_data[user][email]}</b>"),
    Format("Номер телефону: <b>{dialog_data[user][number]}</b>"),
    Format("Дата народження: <b>{dialog_data[user][birthday]}</b>"),
    Row(
        Button(Const("Підтвердити ✅"), id="approve", on_click=database_approve),
        Button(Const("Переробити ✏️"), id="edit", on_click=database_edit),
    ),
    state=Registration.database_info,
)
