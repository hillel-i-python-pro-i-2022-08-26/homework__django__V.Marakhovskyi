from faker import Faker

faker = Faker()


def default_greetings():
    return f"Hi, I`m {faker.first_name()}"
