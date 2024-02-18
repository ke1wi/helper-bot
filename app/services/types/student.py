from typing import Dict, Union
from uuid import UUID

Student = Dict[str, str]
Students = Dict[Union[UUID, str], Dict[str, str]]
