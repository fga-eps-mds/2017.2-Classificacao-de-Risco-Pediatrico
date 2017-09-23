# Arquivo: /apps/users/views.py
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import RegistrationAdminForm
from .forms import RegistrationAttendantForm
from .forms import RegistrationPacientForm
from .models import Pacient


def home(request):
    return render(request, 'users/home.html')

def teste(request):
    return render(request, 'users/teste.html')

def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:home'))

    kwargs['extra_context'] = {'next': reverse('users:home')}
    kwargs['template_name'] = 'users/login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('users:home')
    return logout(request, *args, **kwargs)

def register_pacient(request):
    return render(request, 'user/login', {})

class RegistrationAdminView(CreateView):
    form_class = RegistrationAdminForm
    template_name = "users/registerStaff.html"
    success_url = reverse_lazy('users:login')


class RegistrationAttendantView(CreateView):
    form_class = RegistrationAttendantForm
    template_name = "users/registerStaff.html"
    success_url = reverse_lazy('users:login')


class RegistrationPacientView(CreateView):
    form_class = RegistrationPacientForm
    template_name = "users/registerPacient.html"
    success_url = reverse_lazy('users:show_pacient')

def showPacient_view(request, cpf):
    pacient = Pacient.objects.filter(cpf=cpf)[0]
    return render(request, 'users/showPacient.html', {'pacient': pacient})

def homeRecepcionist_view(request):
    return render(request, 'users/homeRecepcionist.html')
