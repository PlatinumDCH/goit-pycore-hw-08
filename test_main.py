import unittest
from address_book import AddressBook
from birthday import Birthday
from CLI import (add_contact,
                 change_contact,
                 delete_contact,
                 show_phone,
                 show_all,
                 show_birthday,
                 birthdays,
                 add_birthday
                 )
from phone import Phone, ValidatePhone
from record import Record


class TestAddressBook(unittest.TestCase):
    def test_valid_phone(self):
        """valid number"""
        phone = Phone("1234567890")
        self.assertEqual(phone.value, "1234567890")

    def test_invalid_phone_non_digit(self):
        """Uncorect number"""
        with self.assertRaises(ValidatePhone):
            Phone("12345abc90")

    def test_invalid_phone_length(self):
        """false len"""
        with self.assertRaises(ValidatePhone):
            Phone("123456789")  # Менее 10 цифр
        with self.assertRaises(ValidatePhone):
            Phone("12345678901")  # Более 10 цифр
    def test_valid_birthday(self):
        """Valid date"""
        birthday = Birthday("2024.10.21")
        self.assertEqual(birthday.value.year, 2024)
        self.assertEqual(birthday.value.month, 10)
        self.assertEqual(birthday.value.day, 21)

    def test_invalid_birthday_format(self):
        """Not valid date"""
        with self.assertRaises(ValueError):
            Birthday("21-10-2024")  # Неверный формат
        with self.assertRaises(ValueError):
            Birthday("2024/10/21")  # Неверный формат

    def test_invalid_birthday_non_date(self):
        """not data test"""
        with self.assertRaises(ValueError):
            Birthday("Not a date")  # Не является датой
    
    def setUp(self):
        self.record = Record("John Doe")
        self.book = AddressBook()
        self.record1 = Record("John Doe")
        self.record2 = Record("Jane Doe")
        self.record1.add_birthday("2024.10.25") 
        self.record2.add_birthday("2024.10.27")
        self.book.add_record(self.record1)
        self.book.add_record(self.record2)

    def test_add_phone(self):
        self.record.add_phone("1234567890")
        self.assertEqual(len(self.record.phones), 1)
        self.assertEqual(self.record.phones[0].value, "1234567890")

    def test_remove_phone(self):
        self.record.add_phone("1234567890")
        self.record.remove_phone("1234567890")
        self.assertEqual(len(self.record.phones), 0)

    def test_remove_nonexistent_phone(self):
        self.record.add_phone("1234567890")
        result = self.record.remove_phone("0987654321")
        self.assertIsNone(result)

    def test_add_birthday(self):
        self.record.add_birthday("2024.10.21")
        self.assertIsNotNone(self.record._birthday)
        self.assertEqual(self.record._birthday.value.year, 2024)
        self.assertEqual(self.record._birthday.value.month, 10)
        self.assertEqual(self.record._birthday.value.day, 21)

    def test_edit_phone(self):
        self.record.add_phone("1234567890")
        self.record.edit_phone("1234567890", "0987654321")
        self.assertEqual(self.record.phones[0].value, "0987654321")

    def test_edit_nonexistent_phone(self):
        with self.assertRaises(ValueError):
            self.record.edit_phone("1234567890", "0987654321")

    def test_str_method(self):
        self.record.add_phone("1234567890")
        self.record.add_birthday("2024.10.21")
        expected_str = "Contact name: John Doe, Phones: 1234567890, Birthday: 2024-10-21"
        self.assertEqual(str(self.record), expected_str)

    def test_add_record(self):
        self.assertEqual(len(self.book.data), 2)

    def test_find_record(self):
        found_record = self.book.find("John Doe")
        self.assertEqual(found_record, self.record1)

    def test_delete_record(self):
        self.book.delete("Jane Doe")
        self.assertIsNone(self.book.find("Jane Doe"))
        self.assertEqual(len(self.book.data), 1)

    def test_get_upcoming_birthdays(self):

        upcoming_birthdays = self.book.get_upcoming_birthdays()
        self.assertEqual(len(upcoming_birthdays), 2)

    def test_str_method_2(self):
        expected_str = (
            "Contact name: John Doe, Phones: , Birthday: 2024-10-25\n"
            "Contact name: Jane Doe, Phones: , Birthday: 2024-10-27"
        )
        self.assertEqual(str(self.book), expected_str)
    
    def test_add_contact(self):
        response = add_contact(self.book, ["Alice", "1234567890"])
        self.assertEqual(response, "Contact added")
        self.assertIsNotNone(self.book.find("Alice"))

    def test_change_contact(self):
        self.record1.add_phone("9876543210")
        response = change_contact(self.book, ["John Doe", "9876543210", "1111111111"])
        self.assertEqual(response, "Contact changed.")
        self.assertIsNotNone(self.book.find("John Doe").find_phone("1111111111"))

    def test_delete_contact(self):
        response = delete_contact(self.book, ["Jane Doe"])
        self.assertEqual(response, "Contact deleted.")
        self.assertIsNone(self.book.find("Jane Doe"))

    def test_show_phone(self):
        self.record1.add_phone("5555555555")
        response = show_phone(self.book, ["John Doe"])
        self.assertIn("John Doe: 5555555555", response)

    def test_show_all(self):
        response = show_all(self.book, [])
        self.assertIn("Contact name: John Doe", response)
        self.assertIn("Contact name: Jane Doe", response)

    def test_add_birthday_2(self):
        response = add_birthday(self.book, ["John Doe", "2024.11.30"])
        self.assertEqual(response, "Birthday added.")
        self.assertIsNotNone(self.book.find("John Doe")._birthday)

    def test_show_birthday(self):
        response = show_birthday(self.book, ["John Doe"])
        self.assertIn("John Doe: 2024-10-25", response)

    def test_birthdays(self):
        response = birthdays(self.book)
        self.assertGreater(len(response), 0) 
if __name__ == '__main__':
    unittest.main(verbosity=2)