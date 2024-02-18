from app.bot.messages.enviroment import environment

FORMAT_MSG = environment.from_string("""
{{ emoji(':warning:') }} You should use this command in following format: \n<code>/add &lt;day.month.year&gt; &lt;alias&gt;</code>
""")

ALREADY_IN_DB_MSG = environment.from_string("""
{{ emoji(':warning:') }} You are already in database!
""")
