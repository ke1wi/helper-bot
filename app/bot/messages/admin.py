from app.bot.messages.enviroment import environment

CELEBRANTS_MSG = environment.from_string("""
Дні народження сьогодні у:
{% for student in celebrants %}
@{{ student.get("username")}} 
{% endfor %}
""")