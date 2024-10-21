from address_book import AddressBook
from record import Record

def main():
    book = AddressBook()
    record1 = Record("John")
    record2 = Record("Alice")
    record3 = Record("Bob")
    record4 = Record("Eve")
    record1.add_birthday("1990.10.25")
    record2.add_birthday("1985.10.22")
    record3.add_birthday("1992.10.30")
    record4.add_birthday("1990.10.28")

    book.add_record(record1)
    book.add_record(record2)
    book.add_record(record3)
    book.add_record(record4)

    # upcom_bd = book.get_upcoming_birthdays()
    # for birthday in upcom_bd:
    #     print(f"Имя: {birthday['name']}, Дата привітання: {birthday['birthday']}")

    print(book.get_upcoming_birthdays())    

if __name__ == "__main__":
    main()
