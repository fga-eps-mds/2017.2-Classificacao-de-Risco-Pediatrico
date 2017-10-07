# Arquivo: /apps/users/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from multi_form_view import MultiModelFormView

from django.contrib.auth import authenticate

from .forms import RegistrationStaffForm
from .forms import AddressForm
from .forms import RegistrationPatientForm

from .models import Patient, Staff


def home(request):
    return render(request, 'users/home.html')


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:home'))

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_admin:
                login(request, user)
                return redirect("/user/login/admin")

            if user.profile == 1:
                login(request, user)
                return redirect("/user/home/receptionist/")

            if user.profile == 2:
                login(request, user)
                return redirect("/user/home/attendant")
        else:
            kwargs['extra_context'] = \
                {'next': reverse('users:home'),
                 'errors': 'Usuário e/ou senha inválido.'}
            kwargs['template_name'] = 'users/login.html'
            return login(request, *args, **kwargs)

    kwargs['extra_context'] = {'next': reverse('users:home')}
    kwargs['template_name'] = 'users/login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    """
    Define the logout page
    """
    kwargs['next_page'] = reverse('users:login')
    return logout(request, *args, **kwargs)


class RegistrationStaffView(MultiModelFormView):
    form_classes = {
        'registration_staff_form': RegistrationStaffForm,
        'address_form': AddressForm,
    }
    record_id = None
    template_name = 'users/registerProfile.html'

    def get_form_kwargs(self):
        """
        Get staff form
        """
        kwargs = super(RegistrationStaffView, self).get_form_kwargs()
        kwargs['address_form']['prefix'] = 'address'
        return kwargs

    def get_objects(self):
        """
        Get objects from staff form
        """
        self.staff_id = self.kwargs.get('staff_id', None)
        try:
            staff = Staff.objects.get(id=self.staff_id)
        except Staff.DoesNotExist:
            staff = None
        return {
            'registration_staff_form': staff,
            'address_form': staff.address if staff else None,
        }

    def get_success_url(self):
        """
        Get succesurl of staff class
        """
        return reverse('users:login')

    def forms_valid(self, forms):
        """
        Return staff form with fields from address form
        """
        staff = forms['registration_staff_form'].save(commit=False)
        staff.address = forms['address_form'].save()
        staff.save()
        return super(RegistrationStaffView, self).forms_valid(forms)


def register_patient(request):
    """
    Register a patient
    """
    return render(request, 'user/login', {})


class RegistrationPatientView(MultiModelFormView):
    form_classes = {
        'registration_profile_form': RegistrationPatientForm,
        'address_form': AddressForm,
    }
    record_id = None
    template_name = 'users/registerPatient.html'

    def get_form_kwargs(self):
        """
        Get patient form
        """
        kwargs = super(RegistrationPatientView, self).get_form_kwargs()
        kwargs['address_form']['prefix'] = 'address'
        return kwargs

    def get_objects(self):
        """
        Get objects from patient form
        """
        self.patient_id = self.kwargs.get('patient_id', None)
        try:
            patient = Patient.objects.get(id=self.patient_id)
        except Patient.DoesNotExist:
            patient = None
        return {
            'registration_patient_form': patient,
            'address_form': patient.address if patient else None
        }

    def get_success_url(self):
        """
        Get succesurl of patient class
        """
        return reverse('users:login')

    def forms_valid(self, forms):
        """
        Return patient form with fields from address form
        """
        patient = forms['registration_patient_form'].save(commit=False)
        patient.address = forms['address_form'].save()
        patient.save()
        return super(RegistrationPatientView, self).forms_valid(forms)


def show_pacient_view(request, cpf):
    """
    return rendered text from showPatient
    """
    patient = Patient.objects.filter(cpf=cpf)[0]
    return render(request, 'users/showPatient.html', {'patient': patient})


def home_receptionist_view(request):
    """
    return rendered text from homeReceptionist
    """
    return render(request, 'users/homeReceptionist.html')


def admin_view(request):
    """
    return rendered text from homeReceptionist
    """
    return render(request, 'users/admin.html')


def home_attendant_view(request):
    """
    return rendered text from homeAttendant
    """
    return render(request, 'users/homeAttendant.html')
