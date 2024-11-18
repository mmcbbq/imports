from faker import Faker

fake = Faker('de_DE')
Faker.seed(100)
for x in range(100):
    print(fake.name())
    print(fake.address())
    print(fake.email())
    print()

