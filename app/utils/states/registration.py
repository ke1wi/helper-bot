from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    email = State()
    name = State()
    surname = State()
    number = State()
    birthday = State()
    info = State()
    database_info = State()
