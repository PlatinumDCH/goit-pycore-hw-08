from phone import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, value:str):
        try:
            parse_date = datetime.strptime(value, "%Y.%m.%d").date()
            super().__init__(parse_date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
