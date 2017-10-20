# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.users.models import Patient, Staff


class RegistrationStaffForm(UserCreationForm):
    class Meta:
        model = Staff
        fields = ['name', 'email', 'id_user', 'profile', 'uf', 'city',
                  'neighborhood', 'street', 'block', 'number']


class RegistrationPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'cpf', 'guardian', 'birth_date', 'parents_name',
                  'uf', 'city', 'neighborhood', 'street', 'block', 'number',
                  'isInQueue', 'queuePosition']
