from datetime import datetime


class DateService:

    @classmethod
    def validate_date(cls, bd_date: str) -> datetime | None:
        try:
            date = datetime.strptime(bd_date, "%d.%m.%Y")
            return date
        except ValueError:
            return None