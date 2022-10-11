from typing import NamedTuple

from faker import Faker

faker = Faker()


class User(NamedTuple):
    userdata: str

    def __str__(self):
        return f"login: {self.userdata[0]} | email: {self.userdata[1]} | password: {self.userdata[2]}"
