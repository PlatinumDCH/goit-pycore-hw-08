from phone import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, value:str):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
