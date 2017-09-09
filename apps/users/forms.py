# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm

from .models import Mypaciente


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Mypaciente
        fields = ['first_name', 'email']
