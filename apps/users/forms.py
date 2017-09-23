# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from .models import Admin, Attendant, Address
from django import forms


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['uf', 'city', 'neighborhood', 'street', 'block', 'number']


class RegistrationAdminForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['username', 'name', 'email', 'id_user']


class RegistrationAttendantForm(UserCreationForm):
    class Meta:
        model = Attendant
        fields = ['username', 'name', 'email', 'id_user']
