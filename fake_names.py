from faker import Faker
faker_ = Faker('pt_BR')
for _ in range(10):
    print(faker_.name())