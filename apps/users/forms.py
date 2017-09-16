# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Admin, Attendant, Pacient


class AddressForm(forms.ModelForm):
    class Meta:
        fields = ['uf', 'city', 'neighborhood', 'street', 'block', 'number']


class RegistrationRecepcionistForm(UserCreationForm):
    class Meta:
        fields = ['email', 'id_user']


class RegistrationAttendantForm(UserCreationForm):
    class Meta:
        fields = ['name', 'email', 'id_user']


class RegistrationAdminForm(UserCreationForm):
    class Meta:
        fields = ['name', 'email', 'id_user']
        model = Admin


class RegistrationPacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = ['name', 'cpf', 'guardian', 'birth_date', 'parents_name', 'uf', 'city', 'neighborhood', 'street', 'block', 'number' ]
