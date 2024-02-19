from app.bot.messages.enviroment import environment

START_MSG = environment.from_string("""
Hello! I am a helper bot for IA-33. I will try to make our life easier)
""")

HELP_MSG = environment.from_string("""
For this moment i can:

/start - Simple hello message
/help - List of commands
""")