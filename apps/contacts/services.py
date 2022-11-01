from collections.abc import Iterator

from faker import Faker

from apps.contacts import models

faker = Faker()
locale_list = ["uk-UA", "en_US", "da_DK", "No_NO", "pl_PL"]
fake = Faker(locale_list)


def generate_contacts(amount: int) -> Iterator[models.Contact]:
    contacts = set()

    while len(contacts) < amount:
        contact = fake.name()

        if contact in contacts:
            continue

        contacts.add(contact)
        yield models.Contact(
            full_name=contact,
            phone_number=faker.phone_number(),
            date_of_birth=faker.date_of_birth(minimum_age=18, maximum_age=90),
        )
