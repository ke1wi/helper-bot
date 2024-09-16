from aiogram.filters.callback_data import CallbackData


class Registration(CallbackData, prefix="reg"):
    pass


class Approve(CallbackData, prefix="approve_reg"):
    pass


class Edit(CallbackData, prefix="deny_reg"):
    pass


class Cancel(CallbackData, prefix="cancel_reg"):
    pass
