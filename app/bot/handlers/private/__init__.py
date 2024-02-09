from aiogram import Router
from app.bot.handlers.private.start import start
from app.bot.handlers.private.help import help
from aiogram.filters import CommandStart, Command


router = Router(name=__name__)
router.message.register(start, CommandStart())
router.message.register(help, Command("help"))
