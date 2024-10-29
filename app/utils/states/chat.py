from aiogram.fsm.state import State, StatesGroup


class Chat(StatesGroup):
    choose = State()
    message = State()
