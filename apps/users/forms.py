# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Patient, Address, Staff


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['uf', 'city', 'neighborhood', 'street', 'block', 'number']


class RegistrationStaffForm(UserCreationForm):
    class Meta:
        model = Staff
        fields = ['name', 'email', 'id_user', 'profile']


class RegistrationPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'cpf', 'guardian', 'birth_date', 'parents_name']
