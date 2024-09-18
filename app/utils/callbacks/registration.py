from aiogram.filters.callback_data import CallbackData


class Approve(CallbackData, prefix="approve_reg"):
    pass


class Edit(CallbackData, prefix="edit_reg"):
    pass


class Cancel(CallbackData, prefix="cancel_reg"):
    pass
