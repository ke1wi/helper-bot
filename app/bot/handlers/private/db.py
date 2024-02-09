from aiogram.types import Message
from app.services.datebase_api import DatebaseAPI
from redis.exceptions import ConnectionError



async def add_birthday(message: Message, state) -> None:
    data = {
        "name": "Ничик Олександр Олегович",
        "birthday": "22.07.2006",
        "tag": "@cybuni"
    }
    async with DatebaseAPI() as client:
        await client.json().set("2", "$", data)
    await message.answer("Db migrated")