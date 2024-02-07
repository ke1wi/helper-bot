from aiogram import Bot, Dispatcher
from app.settings import settings


class App:
    bot = Bot(settings.TOKEN.get_secret_value())
    dp = Dispatcher()

