from datetime import datetime
from typing import Optional

DATE_FORMAT = "%d.%m.%Y"


class Dateutil:
    @staticmethod
    def parse_birthday(input_date: str) -> Optional[datetime]:
        try:
            birthday = datetime.strptime(input_date, DATE_FORMAT).date()
            return birthday
        except ValueError:
            return None
