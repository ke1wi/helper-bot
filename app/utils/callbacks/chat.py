from aiogram.filters.callback_data import CallbackData


class Deputy(CallbackData, prefix="chat"):
    deputy_id: int
