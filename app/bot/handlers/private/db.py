from aiogram.types import Message
from app.services.datebase_api import DatebaseAPI
from redis.exceptions import ConnectionError
from app.utils.states import UserStates
from aiogram.fsm.context import FSMContext
from datetime import datetime


async def add_birthday(message: Message, state: FSMContext) -> None:
    async with DatebaseAPI() as client:
        await client.json().set("3", "$", await state.get_data())
    await message.answer("Db migrated")


async def db(message: Message, state: FSMContext):
    await message.answer(
        "Enter name:"
    )
    await state.set_state(UserStates.name)


async def process_name(message: Message, state: FSMContext):
    if isinstance(message.text, str):
        await state.update_data(name=message.text)
        await message.answer(
            f"name succ",
        )
        await state.set_state(UserStates.birthday)
    elif len(message.text) < 3:
        await message.answer(
            f"len message error"
        )
    else:
        await message.answer(
            f"name error not a text"
        )


async def process_date(message: Message, state: FSMContext):
    def validate_date(date_string, date_format='%d.%m.%Y'):
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False
    if validate_date(message.text):
        await state.update_data(birthday=message.text)
        await message.answer(
            f"birthday succ"
        )
        await state.set_state(UserStates.username)
    else:
        await message.answer(
            f"birthday value error"
        )


async def process_username(message: Message, state: FSMContext):
    if message.forward_from.username:
        state.update_data(username=message.forward_from.username)
        await message.answer(f"username: {message.forward_from.username}")
        await add_birthday(message=message, state=state)
    else:
        await message.answer("username error")
