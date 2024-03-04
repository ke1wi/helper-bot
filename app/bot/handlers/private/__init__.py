from aiogram import Router
from app.bot.handlers.private.start import start, ignore
from app.bot.handlers.private.help import help
from app.bot.handlers.private.add_birthday import add_birthday, send_congrats
from app.bot.handlers.private.add_birthday_manualy import add_birthday_manualy
from app.bot.handlers.private.tags import tag_all
from aiogram.filters import CommandStart, Command
from aiogram import F



router = Router(name=__name__)
router.message.register(start, CommandStart())
router.message.register(help, Command("help"))
router.message.register(add_birthday, Command("add"))
router.message.register(add_birthday_manualy, Command("add_manual"))
router.message.register(tag_all, Command("tag_all"))
router.callback_query.register(send_congrats, F.data == "SENDCONGRATS")
router.callback_query.register(ignore, F.data == "IGNORE")
