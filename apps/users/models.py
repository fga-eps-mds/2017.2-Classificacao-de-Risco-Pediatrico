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
            raise ValueError(_('Users must have an email address'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Person(models.Model):
    class Meta:
        abstract = True

    birth_date = models.DateField(
        verbose_name=_('Data de Nascimento'),
        blank=False,
        help_text=_('Informe a data de Nascimento'),
    )

    cpf = models.CharField(
        verbose_name=_('CPF'),
        max_length=11,
        blank=False,
        help_text=_('Informe o CPF'),
        unique=True
    )

    address = models.CharField(
        verbose_name=_('Endereço'),
        max_length=200,
        blank=False,
        help_text=_('Informe o endereço'),
    )

    name = models.CharField(
        verbose_name=_('Nome'),
        max_length=150,
        blank=False,
        help_text=_('Informe seu nome'),
    )


class Staff(AbstractBaseUser):
    username = models.CharField(
        verbose_name=_('Nome de usuário'),
        max_length=150,
        blank=False,
        help_text=_('Informe seu nome de usuário'),
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


class Patient(Person):
    guardian = models.CharField(
        verbose_name=_('Nome do Responsável'),
        max_length=50,
        blank=False,
        help_text=_('Informe o nome do responsável'),
    )
