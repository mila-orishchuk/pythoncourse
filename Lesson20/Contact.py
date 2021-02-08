'''
Practise type annotations

Go to your implementation of the Phonebook application from module 1 or any other
comprehensive code, which you have done during the course, and annotate this code
with type hints, using knowledge from this lesson.

'''
import typing


class Contact:
    def __init__(self, name: str, lastname: str, phone: str, city: str) -> None:
        self.__name = name
        self.__lastname = lastname
        self.__phone = phone
        self.__city = city

    @property
    def __fullname(self) -> str:
        return f'{self.__name}{self.__lastname}'

    def __str__(self) -> str:
        return self.__name

    def __repr__(self) -> str:
        return f"Contact name:{self.__name} phone:{self.__phone}"

    def get_display_value(self) -> str:
        return f"{self.__name} / {self.__phone}"

    def has_phone(self) -> bool:
        return self.__phone is not None and len(self.__phone) > 0

    def to_dict(self) -> dict:
        return {
            "name": self.__name,
            "phone": self.__phone,
            'lastname': self.__lastname,
            'fullname': self.__fullname,
            'city': self.__city
        }


if __name__ == '__main__':
    pass
