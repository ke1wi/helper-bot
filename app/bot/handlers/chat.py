from aiogram_dialog import DialogManager, StartMode
from app.utils.states.chat import Chat
from aiogram.types import Message
from app.utils.database.models.user import User


async def chat(message: Message, dialog_manager: DialogManager, user: User):
    await dialog_manager.start(
        Chat.choose,
        data={
            "first_message_id": message.message_id + 1,
            "telegram_username": user.telegram_username,
        },
        mode=StartMode.RESET_STACK,
    )
