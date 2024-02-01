from aiogram.types import Message
from aiogram import Bot
from app.settings import settings


async def start(message: Message, bot: Bot) -> None:
    await bot.send_message(settings.CHAT_ID, 'Vova, ya tebe lublyu')
