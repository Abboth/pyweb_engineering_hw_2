from collections import UserDict
from bot_assistant.parsing_module import *


class Birthdays:
    def __init__(self):
        self.birthday = None

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def __str__(self):
        return str(self.birthday)


class Phones:
    def __init__(self):
        self.phones = []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone: str):
        for phone_number in self.phones:
            if phone_number.value == phone:
                self.phones.remove(phone_number)
                return
        print("Incorrect number")

    def find_phone(self, phone: str) -> str:
        for phone_number in self.phones:
            if phone_number.value == phone:
                return phone_number.value
        print(f"Phone number doesn't exist")

    def __str__(self):
        return ', '.join(str(p) for p in self.phones)


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = Phones()
        self.birthday = Birthdays()

    def add_phone(self, phone: str):
        self.phones.add_phone(Phone(phone))

    def remove_phone(self, phone: str):
        self.phones.remove_phone(phone)

    def find_phone(self, phone: str) -> str:
        return self.phones.find_phone(phone)

    def add_birthday(self, birthday: str):
        self.birthday.add_birthday(Birthday(birthday))

    def __str__(self):
        if not self.birthday:
            return f"Contact name: {self.name}, phones: {self.phones}"
        return f"Contact name: {self.name}, birthday: {self.birthday}, phones: {self.phones}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            for key, record in self.data.items():
                if key == name:
                    return record

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            print("Contact does not exist")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
