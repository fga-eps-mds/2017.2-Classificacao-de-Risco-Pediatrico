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
    def clean(self):
        cleaned_data = super(RegistrationPatientForm, self).clean()
        name = cleaned_data.get("name")
        cpf = cleaned_data.get("cpf"),
        guardian = cleaned_data.get("guardian"),
        birth_date = cleaned_data.get("birth_date"),
        parents_name = cleaned_data.get("parents_name"),
        uf = cleaned_data.get("uf"),
        city = cleaned_data.get("city"),
        neighborhood = cleaned_data.get("neighborhood"),
        street = cleaned_data.get("street"),
        block = cleaned_data.get("block"),
        number = cleaned_data.get("number"),
        age_range = cleaned_data.get("age_range"),
        if(birth_date in cleaned_data is not None and \
           cleaned_data[age_range] is None):
           del cleaned_data[age_range]
        elif(age_range in cleaned_data is not None and \
           cleaned_data[birth_date] is None):
           del cleaned_data[birth_date]
        return cleaned_data
    class Meta:
        model = Patient
        fields = ['name', 'cpf', 'guardian', 'birth_date', 'parents_name',
                  'uf', 'city', 'neighborhood', 'street', 'block', 'number',
                  'age_range']


class EditPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'cpf', 'guardian', 'birth_date', 'parents_name',
                  'uf', 'city', 'neighborhood', 'street', 'block', 'number',
                  'age_range']
