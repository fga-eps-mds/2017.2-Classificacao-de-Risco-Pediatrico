# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from .models import Admin, Attendant, Address, Staff, Recepcionist
from django import forms


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['uf', 'city', 'neighborhood', 'street', 'block', 'number']


class RegistrationRecepcionistForm(UserCreationForm):
    class Meta:
        model = Recepcionist
        fields = ['email', 'id_user']


class RegistrationAttendantForm(UserCreationForm):
    class Meta:
        model = Attendant
        fields = ['name', 'email', 'id_user']


class RegistrationAdminForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['name', 'email', 'id_user']
