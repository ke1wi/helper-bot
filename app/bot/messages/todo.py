from app.bot.messages.enviroment import environment

FORMAT_MSG = environment.from_string("""
{{ emoji(':warning:') }} You should use this command in following format: \n<code>/todo &lt;what todo&gt(text); &lt;day.month.year&gt;(deadline)</code>
""")

ALREADY_IN_DB_MSG = environment.from_string("""
{{ emoji(':warning:') }} This task is already in todo!
""")