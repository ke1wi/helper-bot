from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="Почати спілкування"),
        BotCommand(command="help", description="Допомога в користуванні"),
        BotCommand(command="reg", description="Реєстрація"),
        BotCommand(command="view", description="Список зарєєстрованих студентів"),
    ]

    await bot.set_my_commands(commands)
