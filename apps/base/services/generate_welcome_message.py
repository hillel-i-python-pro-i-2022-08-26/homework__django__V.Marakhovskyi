from faker import Faker

faker = Faker()


def generate_welcome_message():
    return f"Hi {faker.first_name()}. How are you?"
