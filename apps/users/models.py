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

STATE_CHOICES = (
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
    ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
)

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
    uf = models.CharField(
        verbose_name='UF',
        max_length=2,
        choices=STATE_CHOICES,
        blank=False
    )
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

    is_superuser = False

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

    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(
        verbose_name=_('Nome'),
        max_length=150,
        default='',
        blank=True
    )

    guardian = models.CharField(
        verbose_name=_('Nome do Responsável'),
        max_length=50,
        default='',
        blank=True,
        help_text=_('Informe o nome do responsável'),
    )

    birth_date = models.DateField(
        verbose_name=_('Data de Nascimento'),
        help_text=_('Informe a data de Nascimento'),
        blank=True,
        null=True
    )

    cpf = models.CharField(
        verbose_name=_('CPF'),
        max_length=14,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Informe o CPF')
    )

    parents_name = models.CharField(
        verbose_name=_('Nome dos pais'),
        max_length=150,
        default='',
        blank=True,
        help_text=_('Informe o nome dos pais')
    )

    uf = models.CharField(
        verbose_name='UF',
        max_length=2,
        choices=STATE_CHOICES,
        default='',
        blank=True
    )

    city = models.CharField(
        verbose_name='Cidade',
        max_length=50,
        default='',
        blank=True
    )
    neighborhood = models.CharField(
        verbose_name='Bairro',
        max_length=100,
        default='',
        blank=True
    )
    street = models.CharField(
        verbose_name='Rua',
        max_length=50,
        default='',
        blank=True
    )
    block = models.CharField(
        verbose_name='Conjunto',
        max_length=50,
        default='',
        blank=True
    )
    number = models.CharField(
        verbose_name='Numero',
        max_length=10,
        default='',
        blank=True
    )
    date = models.DateField(
        verbose_name='Data',
        blank=False,
        auto_now=True
    )
    classifier = models.CharField(
        verbose_name=_('Classifier'),
        max_length=150,
        blank=False,
    )

    CLASSIFICATION_TYPES = (
        (0, 'Não classificado'),
        (1, 'Atendimento Imediato'),
        (2, 'Atendimento Ambulatorial'),
        (3, 'Atendimento Hospitalar'),
        (4, 'Atendimento Eletivo')
    )

    classification = models.IntegerField(
        verbose_name=_('Classification'),
        choices=CLASSIFICATION_TYPES,
        default=0
    )

    GENDER = (
        (0, 'Sexo indefinido'),
        (1, 'Feminino'),
        (2, 'Masculino')
    )

    gender = models.IntegerField(
        verbose_name=_('Classification'),
        choices=GENDER,
        default=0,
        blank=True
    )


    AGE_RANGE = (
        (0, 'Faixa etária indefinida'),
        (1, '0 até 28 dias'),
        (2, '29 dias à 3 meses'),
        (3, '3 meses à 2 anos'),
        (4, '2 anos à 10 anos'),
        (5, 'Acima de 10 anos')
    )

    age_range = models.IntegerField(
        verbose_name=_('Classification'),
        choices=AGE_RANGE,
        default=0,
        blank=True
    )
