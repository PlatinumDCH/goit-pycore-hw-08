from phone import Field
from datetime import datetime

class ValidatedDataBirthday(Exception):
    '''castom exception for invalid birthday format'''
    ...

class Birthday(Field):
    def __init__(self, value:str):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            super().__init__(value)
        except ValueError:
            raise ValidatedDataBirthday("Invalid date format. Use DD.MM.YYYY")
