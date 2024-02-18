from jinja2 import Environment
from emoji import emojize

environment = Environment(enable_async=True, trim_blocks=True, autoescape=True)

environment.globals.update(
    emoji=emojize
)
