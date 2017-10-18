import factory
from apps.users.models import Patient
from faker import Faker

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
    isInQueue = factory.faker.Faker("pybool")
    queuePosition = factory.Sequence(lambda n: n)


# class PlatformFactory(factory.DjangoModelFactory):
#
#     class Meta:
#
#         model = Platform
#
#     name = factory.faker.Faker("word")
#     extensions = factory.LazyAttribute(lambda x: "deb")
#     kernel = factory.LazyAttribute(lambda x: "Linux")
#
#
# class PackageFactory(factory.DjangoModelFactory):
#
#     class Meta:
#         model = Package
#
#     package = factory.django.FileField(data=b'1' * 10,
#               filename='package.deb')
#     game = factory.SubFactory(GameFactory)
#     downloads = factory.faker.Faker('pyint')
#     architecture = factory.LazyAttribute(lambda x: "AMD64/64-bit")
