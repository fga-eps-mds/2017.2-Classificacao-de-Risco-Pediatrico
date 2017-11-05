import factory
from apps.users.models import Patient, Staff
from faker import Faker
from factory.fuzzy import FuzzyInteger

faker = Faker()


class PatientFactory(factory.DjangoModelFactory):

    class Meta:
        model = Patient

    name = factory.faker.Faker("word")
    guardian = factory.faker.Faker("word")
    birth_date = factory.faker.Faker("date")
    cpf = factory.faker.Faker('pyint')
    parents_name = factory.faker.Faker("word")
    uf = factory.faker.Faker("word")
    city = factory.faker.Faker("word")
    neighborhood = factory.faker.Faker("word")
    street = factory.faker.Faker("word")
    block = factory.faker.Faker("word")
    number = factory.faker.Faker("pyint")
    age_range = factory.faker.Faker("pyint")
    '''isInQueue = factory.faker.Faker("pybool")
    queuePosition = factory.Sequence(lambda n: n)'''


class StaffFactory(factory.DjangoModelFactory):

    class Meta:
        model = Staff

    name = factory.faker.Faker("word")
    id_user = factory.faker.Faker("pyint")
    email = factory.faker.Faker("date")
    profile = FuzzyInteger(0, 2)
    password = factory.faker.Faker("word")
    uf = factory.faker.Faker("word")
    city = factory.faker.Faker("word")
    neighborhood = factory.faker.Faker("word")
    street = factory.faker.Faker("word")
    block = factory.faker.Faker("word")
    number = factory.faker.Faker("pyint")
