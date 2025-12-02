from faker import Faker
import random

faker = Faker('pt_BR')
name = faker.name()
adress = faker.address()
email = faker.email()

print(name)
print(adress)
print(email)

number_random = random.uniform(0,10)
print(f"{number_random:0.2f}")

