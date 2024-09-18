from app.bot.messages.enviromnent import environment


REGISTRATION_MSG = environment.from_string(
    """
Перевір чи все правильно:

Імʼя: <b>{{name}}</b>
Прізвище: <b>{{surname}}</b>
Електронна пошта: <b>{{email}}</b>
Номер телефону: <b>{{number}}</b>
Дата народження: <b>{{birthday}}</b>
"""
)
