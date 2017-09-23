# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms


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
