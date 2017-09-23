# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Admin, Attendant, Patient


class RegistrationAdminForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['username', 'name', 'email', 'uf', 'city', 'neighborhood', 'street', 'block', 'number']


class RegistrationAttendantForm(UserCreationForm):
    class Meta:
        model = Attendant
        fields = ['username', 'name', 'email', 'uf', 'city', 'neighborhood', 'street', 'block', 'number']


class RegistrationPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'cpf', 'guardian', 'birth_date', 'parents_name', 'uf', 'city', 'neighborhood', 'street',
                  'block', 'number']