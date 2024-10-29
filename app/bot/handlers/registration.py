from aiogram.types import Message
from app.utils.states.registration import Registration
from aiogram_dialog import DialogManager, StartMode


async def reg(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        Registration.email,
        data={
            "first_message_id": message.message_id + 1,
            "telegram_id": message.from_user.id,
            "telegram_username": message.from_user.username,
            "editing": False,
        },
        mode=StartMode.RESET_STACK,
    )
