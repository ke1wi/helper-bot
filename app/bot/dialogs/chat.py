from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput
from app.settings import settings
from aiogram.types import CallbackQuery, Message


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


async def captain_choosen(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager,
) -> None:
    manager.dialog_data["deputy_id"] = settings.CAPTAIN_ID
    await manager.next()


async def vice_captain_choosen(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager,
) -> None:
    manager.dialog_data.update({"deputy_id": settings.VICE_CAPTAIN_ID})
    await manager.next()


async def message_handler(
    message: Message,
    message_input: MessageInput,
    manager: DialogManager,
):
    header = f"Повідомлення від @{manager.start_data['telegram_username']}\n\n"
    await message.answer("Повідомлення надіслано")
    notification = header + f"<i>{message.text}</i>"
    await message.bot.send_message(manager.dialog_data.get("deputy_id"), notification)
    await manager.done()
