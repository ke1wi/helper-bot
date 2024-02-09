from aiogram import Router
from app.bot.handlers.private.start import start
from app.bot.handlers.private.help import help
from app.bot.handlers.private.db import db
from aiogram.filters import CommandStart, Command
from app.utils.states import UserStates
from app.bot.handlers.private.db import process_name, process_date, process_username

router = Router(name=__name__)
router.message.register(start, CommandStart())
router.message.register(help, Command("help"))
router.message.register(db, Command("db"))
router.message.register(process_name, UserStates.name)
router.message.register(process_date, UserStates.birthday)
router.message.register(process_username, UserStates.username)