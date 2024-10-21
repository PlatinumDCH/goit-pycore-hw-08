from address_book import AddressBook
from record import Record


def input_error(expected_args):
    def decorator(func):
        def wrapper(book, args):
            if expected_args == 0:
                return func(book, args)
            if len(args) == 0:
                return f'Please enter arguments for the command'
            if len(args) < expected_args:
                return f"Command expected {expected_args} arguments"
            return func(book, args)
        return wrapper
    return decorator


def parse_input(user_input: str):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error(1)
def add_contact(book: AddressBook, args):
    name = args[0]
    phone = args[1] if len(args) > 1 else None

    record = book.find(name)
    message = 'Contact updated'
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = 'Contact added'
    if phone:
        record.add_phone(phone)
    return message


@input_error(3)
def change_contact(book: AddressBook, args):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact changed."
    else:
        return "Contact not found."


@input_error(1)
def delete_contact(book, args):
    name = args[0]
    if book.find(name):
        book.delete(name)
        return "Contact deleted."
    else:
        return "Contact not found."


@input_error(1)
def show_phone(book, args):
    name = args[0]
    record = book.find(name)
    if record:
        phones = ', '.join(phone.value for phone in record.phones)
        return f'{name}: {phones}'
    else:
        return "Contact not found."


def greeting():
    return "Hello, how can I help you?"


@input_error(0)
def show_all(book: AddressBook, args):
    if book:
        return str(book)
    else:
        return "No contacts found."

@input_error(2)
def add_birthday(book: AddressBook, args):
    name = args[0]
    date = args[1]
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added."
    else:
        return "Contact not found or no birthday set."

@input_error(1)
def show_birthday(book: AddressBook, args):
    name = args[0]
    record = book.find(name)
    if record and record._birthday:
        return f'{name}: {record._birthday}'
    else:
        return "Contact not found."

def birthdays(book: AddressBook):
    if book:
        return book.get_upcoming_birthdays()
    else:
        return "No contacts found."
    

def show_command():
    help_data = (
        "Available commands:\n"
        "1. add [name] [phone] - Add a new contact.\n"
        "2. change [name] [old phone] [new_phone] - Change an existing contact's phone number.\n"
        "3. phone [name] - Show the phone number of a contact.\n"
        "4. all - Show all contacts.\n"
        "5. help - Show this help message.\n"
        "6. del [name]- Delete a contact.\n"
        "7. hello - greets the user.\n"
        "8. close / exit - Exit the program.\n"
        "9. add-birthday [name] [date] -Y|M|D format.\n"
        "10. show-birthday [name] - Show a contact's birthday.\n"
        "11. birthdays - Show birthdays for the next 7 days with the dates when they should be congratulated.\n"
    )
    print(help_data)


def main():
    book = AddressBook()
    while True:
        user_input = input("Enter a command: ").strip()
        cmd, *args = parse_input(user_input)

        match cmd:
            case "add":
                print(add_contact(book, args))
            case "change":
                print(change_contact(book, args))
            case "phone":
                print(show_phone(book, args))
            case "all":
                print(show_all(book, []))
            case "help":
                show_command()
            case "del":
                print(delete_contact(book, args))
            case "hello":
                print(greeting())
            case "add-birthday":
                print(add_birthday(book, args))
            case "show-birthday":
                print(show_birthday(book, args))
            case "birthdays":
                print(birthdays(book))
            case "close" | "exit":
                print("Goodbye!")
                break
            case _:
                print('Invalid command. Type "help" for a list of available commands.')


if __name__ == "__main__":
    print("Welcome to the CLI assistant.")
    main()
