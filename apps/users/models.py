from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext as _


class UserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError(_('O endereço de email não pode ser nulo'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Address(models.Model):
    uf = models.CharField(verbose_name='UF',
                          max_length=50,
                          blank=False)
    city = models.CharField(verbose_name='Cidade',
                            max_length=50,
                            blank=False)
    neighborhood = models.CharField(verbose_name='Bairro',
                                    max_length=100,
                                    blank=False)
    street = models.CharField(verbose_name='Rua',
                              max_length=50,
                              blank=False)
    block = models.CharField(verbose_name='Conjunto',
                             max_length=50,
                             blank=False)
    number = models.CharField(verbose_name='Numero',
                              max_length=10,
                              blank=False)


class Person(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        verbose_name=_('Nome'),
        max_length=150,
        blank=False,
    )


class Staff(AbstractBaseUser):

    id_user = models.CharField(
        verbose_name=_('ID de usuário'),
        max_length=150,
        blank=False,
        unique=True
    )

    email = models.EmailField(
        verbose_name=_('Email do usuário'),
        unique=True,
        default=''
    )

    is_superuser = False
    USERNAME_FIELD = 'email'

    def get_short_name(self):
        pass

    def get_full_name(self):
        pass


class Admin(Staff, Person):
    objects = UserManager()


class Attendant(Staff, Person):
    objects = UserManager()

class Recepcionist(Staff, Person):
    objects = UserManager()
