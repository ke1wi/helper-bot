from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput
from aiogram.types import CallbackQuery, Message
import re
from app.utils.database.api import get_user_by_email
from app.utils.dateutils import Dateutil
from app.utils.states.registration import Registration
from app.utils.database.api import create_user, delete_user_by_telegram_id
from app.utils.database.models.user import User


async def approve(callback: CallbackQuery, button: Button, manager: DialogManager):
    if manager.start_data["editing"]:
        await delete_user_by_telegram_id(manager.start_data["telegram_id"])
    await create_user(
        User(
            **manager.dialog_data["user"],
            telegram_id=manager.start_data["telegram_id"],
            telegram_username=manager.start_data["telegram_username"],
        )
    )
    await callback.message.bot.delete_messages(
        callback.message.chat.id,
        list(
            range(
                manager.start_data["first_message_id"], callback.message.message_id + 1
            )
        ),
    )
    await callback.message.answer(
        f"Юзер {manager.dialog_data['user']['name']} успішно зарєєстрований!"
    )
    await callback.answer()
    await manager.done()


async def edit(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(Registration.email)


async def cancel(callback: CallbackQuery, button: Button, manager: DialogManager):
    await callback.message.bot.delete_messages(
        callback.message.chat.id,
        list(
            range(
                manager.start_data["first_message_id"], callback.message.message_id + 1
            )
        ),
    )
    await callback.message.answer("Відміняю ❌")
    await callback.answer()


async def email_handler(
    message: Message,
    message_input: MessageInput,
    manager: DialogManager,
):
    email = message.text
    if re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", email):
        user = await get_user_by_email(email)
        if user and not manager.start_data["editing"]:
            manager.dialog_data["user"] = {
                "email": user.email,
                "name": user.name,
                "surname": user.surname,
                "number": user.number,
                "birthday": user.birthday,
            }
            await manager.switch_to(Registration.database_info)
        else:
            manager.dialog_data["user"] = {"email": message.text}
            await manager.next()
    else:
        await message.answer(
            "Електронна пошта неправильна\nВведіть електронну пошту ще раз:"
        )


async def name_handler(
    message: Message,
    message_input: MessageInput,
    manager: DialogManager,
):
    manager.dialog_data["user"].update({"name": message.text})
    await manager.next()


async def surname_handler(
    message: Message,
    message_input: MessageInput,
    manager: DialogManager,
):
    manager.dialog_data["user"].update({"surname": message.text})
    await manager.next()


async def number_handler(
    message: Message,
    message_input: MessageInput,
    manager: DialogManager,
):
    number: str = message.text
    if "+38" not in number:
        number = "+38" + number
    if re.fullmatch(r"^\+?38\s?0\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$", number):
        manager.dialog_data["user"].update({"number": message.text})
        await manager.next()
    else:
        await message.answer(
            "Номер телефону неправильний\nВведіть телефон ще раз:",
        )


async def birthday_handler(
    message: Message,
    message_input: MessageInput,
    manager: DialogManager,
):
    input_birthdate = message.text
    if birthdate := Dateutil.parse_birthday(input_birthdate):
        manager.dialog_data["user"].update({"birthday": birthdate})
        await manager.next()
    else:
        await message.answer(
            "Дата народження неправильна\nВведіть дату народження ще раз:",
        )


async def database_approve(
    callback: CallbackQuery, button: Button, manager: DialogManager
):
    await callback.message.answer("Супер, дякую за достовірну інформацію")
    await manager.done()


async def database_edit(
    callback: CallbackQuery, button: Button, manager: DialogManager
):
    manager.start_data["editing"] = True
    await manager.switch_to(Registration.email)
