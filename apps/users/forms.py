# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from .models import Admin, Attendant


class RegistrationAdminForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['username', 'name', 'email', 'uf', 'city', 'neighborhood', 'street', 'block', 'number']


class RegistrationAttendantForm(UserCreationForm):
    class Meta:
        model = Attendant
        fields = ['username', 'name', 'email', 'uf', 'city', 'neighborhood', 'street', 'block', 'number']
