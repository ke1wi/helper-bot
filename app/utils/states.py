from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    name = State()
    birthday = State()
    username = State()
    