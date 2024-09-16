from aiogram.types import Message

from app.bot.messages.help import HELP_MSG


async def help(message: Message) -> None:
    await message.answer(await HELP_MSG.render_async())
