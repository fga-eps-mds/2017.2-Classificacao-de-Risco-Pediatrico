# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Admin, Attendant, Patient, Address, Receptionist


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['uf', 'city', 'neighborhood', 'street', 'block', 'number']


class RegistrationReceptionistForm(UserCreationForm):
    class Meta:
        model = Receptionist
        fields = ['email', 'id_user']


class RegistrationAttendantForm(UserCreationForm):
    class Meta:
        model = Attendant
        fields = ['name', 'email', 'id_user']


class RegistrationAdminForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['name', 'email', 'id_user']


class RegistrationPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'cpf', 'guardian', 'birth_date', 'parents_name']
