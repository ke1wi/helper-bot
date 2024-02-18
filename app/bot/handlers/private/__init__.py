from aiogram import Router
from app.bot.handlers.private.start import start
from app.bot.handlers.private.help import help
from app.bot.handlers.private.add_birthday import add_birthday
from app.bot.handlers.private.add_birthday_admin import add_birthday_admin
from aiogram.filters import CommandStart, Command



router = Router(name=__name__)
router.message.register(start, CommandStart())
router.message.register(help, Command("help"))
router.message.register(add_birthday, Command("add"))
router.message.register(add_birthday_admin, Command("add_admin"))
