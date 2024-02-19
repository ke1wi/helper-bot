from datetime import datetime


class DateService:

    @classmethod
    def validate_date(cls, date):
        try:
            datetime.strptime(date, "%d.%M.%Y")
            return True
        except ValueError:
            return False