from aiogram import Router
from aiogram.filters.command import CommandStart
from app.bot.handlers.start import start

router = Router(name=__name__)

router.message.register(start, CommandStart())