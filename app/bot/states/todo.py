from aiogram.fsm.state import State, StatesGroup


class Todo(StatesGroup):
    description = State()
    deadline = State()
    migrate = State()
