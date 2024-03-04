from app.bot.messages.enviroment import environment

START_MSG = environment.from_string("""
Hello! I am a helper bot. Write from plz.
""")

HELP_MSG = environment.from_string("""
For this moment i can:

/start - Simple hello message
/help - List of commands
""")