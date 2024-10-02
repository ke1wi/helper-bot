from aiogram.types import Message
from app.utils.database.api import get_users
from app.bot.messages.view import VIEW_MSG


async def view(message: Message) -> None:
    users = await get_users()
    await message.answer(await VIEW_MSG.render_async({"users": users}))
