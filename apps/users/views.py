# Arquivo: /apps/users/views.py
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy, reverse
from multi_form_view import MultiModelFormView

from .forms import RegistrationAdminForm
from .forms import RegistrationAttendantForm

from .forms import RegistrationRecepcionistForm
from .forms import RegistrationPacientForm
from .forms import AddressForm

from .models import Admin


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


class RegistrationAdminView(MultiModelFormView):
    form_classes = {
        'registration_admin_form': RegistrationAdminForm,
        'address_form': AddressForm,
    }
    record_id = None
    template_name = 'users/registerAdmin.html'

    def get_form_kwargs(self):
        kwargs = super(RegistrationAdminView, self).get_form_kwargs()
        # kwargs = super(RegistrationAttendantView, self).get_form_kwargs()
        kwargs['address_form']['prefix'] = 'address'
        return kwargs

    def get_objects(self):
        self.admin_id = self.kwargs.get('admin_id', None)
        # self.attendant_id = self.kwargs.get('attendant_id', None)
        try:
            admin = Admin.objects.get(id=self.admin_id)
            # attendant = Attendant.objects.get(id=self.attendant_id)
        except Admin.DoesNotExist:
            admin = None
        return {
            'registration_admin_form': admin,
            # 'registration_attendant_form': staff,
            'address_form': admin.address if admin else None,
            # 'address_form': attendant.address if attendant else None,
        }

    def get_success_url(self):
        return reverse('users:login')

    def forms_valid(self, forms):
        admin = forms['registration_admin_form'].save(commit=False)
        # attendant = forms['registration_attendant_form'].save(commit=False)
        admin.address = forms['address_form'].save()
        # attendant.address = forms['address_form'].save()
        admin.save()
        # attendant.save()
        return super(RegistrationAdminView, self).forms_valid(forms)


class RegistrationAttendantView(CreateView):

    form_class = RegistrationAttendantForm
    template_name = "users/registerAttendant.html"
    success_url = reverse_lazy('users:login')

    '''
    form_classes = {
        'registration_attendant_form' : RegistrationAttendantForm,
        'address_form' : AddressForm,
    }
    record_id = None
    template_name = 'users/registerStaff.html'

    def get_form_kwargs(self):
        kwargs = super(RegistrationAttendantView, self).get_form_kwargs()
        kwargs['address_form']['prefix'] = 'address'
        return kwargs

    def get_objects(self):
        self.attendant_id = self.kwargs.get('attendant_id', None)
        try:
            attendant = Staff.objects.get(id=self.attendant_id)
        except Attendant.DoesNotExist:
            staff = None
        return {
            'registration_attendant_form': attendant,
            'address_form': attendant.address if attendant else None,
        }

    def get_success_url(self):
        return reverse('users:login')

    def forms_valid(self, forms):
        attendant = forms['registration_attendant_form'].save(commit=False)
        attendant.address = forms['address_form'].save()
        attendant.save()
        return super(RegistrationAttendantView, self).forms_valid(forms)
    '''


class RegistrationRecepcionistView(CreateView):
    form_class = RegistrationRecepcionistForm
    template_name = "users/registerRecepcionist.html"
    success_url = reverse_lazy('users:login')


class RegistrationPacientView(CreateView):
    form_class = RegistrationPacientForm
    template_name = "users/registerPacient.html"
    success_url = reverse_lazy('users:teste')
