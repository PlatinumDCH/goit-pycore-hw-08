class ValidatePhone(Exception):
    '''Custom exception for phone validation'''
    ...

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValidatePhone("Invalid phone number")
        super().__init__(value)

