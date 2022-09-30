from faker import Faker

faker = Faker()

def greet():
    return f'Hi, I`m {faker.first_name()}'