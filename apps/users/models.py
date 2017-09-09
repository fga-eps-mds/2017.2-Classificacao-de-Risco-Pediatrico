from django.db import models

# Create your models here.
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
    )

    guardian =  models.CharField(
        verbose_name=_('Nome do Responsável'),
        max_length=50,
        blank=False,
        help_text=_('Informe o nome do responsável'),
    )
    birth_date = models.DateField(
        verbose_name=_('Data de Nascimento'),
        blank=False,
        help_text=_('Informe a data de Nascimento'),
    )

    first_name = models.CharField(
        verbose_name=_('Nome'),
        max_length=50,
        blank=False,
        help_text=_('Informe o primeiro nome'),
    )
    address = models.CharField(
        verbose_name=('Endereço'),
        max_length=50,
        blank=False,
        help_text=_('Informe o endereço'),
    )
    cpf = models.CharField(
        verbose_name=('CPF'),
        max_length=11,
        blank=False,
        help_text=_('Informe o CPF'),
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
