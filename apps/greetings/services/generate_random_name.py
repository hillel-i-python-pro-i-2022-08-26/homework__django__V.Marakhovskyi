from faker import Faker

faker = Faker()


def generate_name():
    return faker.first_name()
