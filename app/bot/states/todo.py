from aiogram.fsm.state import State, StatesGroup


class Todo(StatesGroup):
    text = State()
    deadline = State()