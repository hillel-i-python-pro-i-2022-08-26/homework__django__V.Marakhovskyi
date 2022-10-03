import random
import string
from collections.abc import Iterator

from faker import Faker

from apps.userdata.models import User

faker = Faker()


def generate_userdata():
    login: str = faker.unique.first_name().lower() + faker.unique.last_name().lower() + str(random.randint(100, 999))
    email: str = login[0:-3] + str(random.randint(100, 999)) + "@" + str(faker.free_email_domain())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(random.randint(8, 16)))
    info = (login, email, password)
    return info


def generate_data_for_users() -> User:
    return User(userdata=generate_userdata())


def generate_userlist(amount: int) -> Iterator[User]:
    for _ in range(amount):
        yield generate_data_for_users()
