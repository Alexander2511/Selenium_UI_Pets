from faker import Faker
import random

fake = Faker()


class Generator:

    def random_name(self):
        name = fake.first_name()
        return name

    def random_email(self):
        email = fake.email()
        return email

    def random_age(self):
        age = random.randint(0, 15)
        return age

