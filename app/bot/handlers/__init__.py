from aiogram import Router
from aiogram.filters.command import CommandStart, Command
from app.bot.filters.in_database import InDatabase
from app.bot.handlers.view import view
from app.bot.handlers.start import start
from app.bot.handlers.help import help
from app.bot.handlers.chat import chat
from app.bot.handlers.registration import reg

router = Router(name=__name__)

router.message.register(start, CommandStart())
router.message.register(help, Command("help"))
router.message.register(reg, Command("reg"))
router.message.register(view, Command("view"))
router.message.register(chat, Command("chat"), InDatabase())
