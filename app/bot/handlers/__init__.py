from aiogram import Router
from aiogram.filters.command import CommandStart, Command
from app.bot.handlers.start import start
from app.bot.handlers.help import help

from app.bot.handlers.registration import (
    name,
    surname,
    email,
    number,
    approve,
    reg,
    cancel,
    birthday,
    edit,
)
from app.utils.states.registration import Registration
from app.utils.callbacks.registration import (
    Cancel,
    Approve,
    Edit,
)

router = Router(name=__name__)

router.message.register(start, CommandStart())
router.message.register(help, Command("help"))

router.message.register(reg, Command("reg"))
router.callback_query.register(cancel, Cancel.filter())
router.message.register(email, Registration.email)
router.message.register(name, Registration.name)
router.message.register(surname, Registration.surname)
router.message.register(number, Registration.number)
router.message.register(birthday, Registration.birthday)
router.callback_query.register(approve, Approve.filter())
router.callback_query.register(edit, Edit.filter())
