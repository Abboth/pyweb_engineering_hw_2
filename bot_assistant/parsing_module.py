from abc import ABC, abstractmethod
import re
from datetime import datetime


class Field(ABC):
    def __init__(self, value):
        self.value = self.input_data(value)

    @abstractmethod
    def input_data(self, value):
        pass

    def __str__(self):
        return str(self.value)


class Name(Field):
    def input_data(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        return value


class Phone(Field):
    def input_data(self, value):
        if re.match(r"^\+?\d{0,3}\d{9}$", value):
            return value
        else:
            raise ValueError("Invalid phone number format.")


class Birthday(Field):
    def input_data(self, value):
        pattern_birthday = r"(\d{2})\.(\d{2})\.(\d{4})"
        if re.match(pattern_birthday, value):
            try:
                datetime.strptime(value, "%d.%m.%Y")
                return value
            except ValueError:
                raise ValueError(f"Date {value} is not exist")
        else:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
