# Arquivo: apps/users/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext as _


class UserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        """
        Create a basic user
        """
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
        """
        Create a superuser
        """
        user = self.create_user(**kwargs)
        user.is_admin = True
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


# Classe dos usuarios possui atendente e recepcionista

class Staff(AbstractBaseUser):

    objects = UserManager()

    name = models.CharField(
        verbose_name=_('Nome'),
        max_length=150,
        blank=False,
    )

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

    PROFILE_TYPES = (
        (1, 'Recepcionista'),
        (2, 'Atendente'),
    )

    profile = models.IntegerField(
        verbose_name=_('Perfil'),
        choices=PROFILE_TYPES,
        default=0
    )

    USERNAME_FIELD = 'email'

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their email address
        return self.name

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Patient(models.Model):

    name = models.CharField(
        verbose_name=_('Nome'),
        max_length=150,
        blank=False,
    )

    guardian = models.CharField(
        verbose_name=_('Nome do Responsável'),
        max_length=50,
        blank=False,
        help_text=_('Informe o nome do responsável'),
    )

    birth_date = models.DateTimeField(
        verbose_name=_('Data de Nascimento'),
        blank=False,
        help_text=_('Informe a data de Nascimento'),
    )

    cpf = models.CharField(
        verbose_name=_('CPF'),
        max_length=11,
        default="",
        blank=False,
        help_text=_('Informe o CPF'),
        unique=True
    )

    parents_name = models.CharField(
        verbose_name=_('Nome dos pais'),
        max_length=150,
        blank=False,
        help_text=_('Informe o nome dos pais'),
        unique=True
    )
