# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from .models import Admin, Attendant


class RegistrationAdminForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['username', 'name', 'birth_date', 'cpf', 'address', 'email']


class RegistrationAttendantForm(UserCreationForm):
    class Meta:
        model = Attendant
        fields = ['username', 'name', 'birth_date', 'cpf', 'address', 'email']
