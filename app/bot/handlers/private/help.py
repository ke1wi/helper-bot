from aiogram.types import Message
from app.bot.messages.general import HELP_MSG


async def help(message: Message) -> None:
    await message.answer(
        await HELP_MSG.render_async()
    )