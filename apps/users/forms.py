# Arquivo: apps/users/forms.py
from django.forms import ModelForm

from .models import Profile
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'first_name', 'cpf')
