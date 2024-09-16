from aiogram.types import Message

from app.bot.messages.start import START_MSG


async def start(message: Message) -> None:
    await message.answer(await START_MSG.render_async())

