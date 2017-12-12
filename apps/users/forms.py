# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.users.models import Patient, Staff


class RegistrationStaffForm(UserCreationForm):
    class Meta:
        model = Staff
        fields = ['name', 'email', 'id_user', 'profile', 'cep', 'uf', 'city',
                  'neighborhood', 'street', 'block', 'number']


class RegistrationPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'comment_receptionist', 'cpf', 'guardian',
                  'birth_date', 'parents_name', 'cep', 'uf', 'city',
                  'neighborhood', 'street', 'block', 'number', 'age_range',
                  'gender']


class EditPatientForm(forms.ModelForm):
    age_range = forms.IntegerField(required=False)

    class Meta:
        model = Patient
        fields = ['name', 'cpf', 'guardian', 'birth_date', 'parents_name',
                  'cep', 'uf', 'city', 'neighborhood', 'street', 'block',
                  'number', 'age_range']
