from enum import Enum


class TodoTypes(str, Enum):
    DEADLINE = 'DEADLINE'
    REMIND = 'REMIND'
