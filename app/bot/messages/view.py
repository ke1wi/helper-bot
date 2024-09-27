from app.bot.messages.enviromnent import environment


VIEW_MSG = environment.from_string(
    """
Список юзерів:
{% for index, user in enumerate(users) %}
{{ index + 1 }}. {{ user.surname }} {{ user.name }}
{% endfor %}
"""
)
