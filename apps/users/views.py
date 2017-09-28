# Arquivo: /apps/users/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from multi_form_view import MultiModelFormView

from .forms import RegistrationAdminForm
from .forms import RegistrationAttendantForm
from .forms import RegistrationReceptionistForm
from .forms import AddressForm
from .forms import RegistrationPatientForm

from .models import Admin, Attendant, Receptionist, Patient, Staff


def home(request):
    return render(request, 'users/home.html')


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:home'))

    kwargs['extra_context'] = {'next': reverse('users:home')}
    kwargs['template_name'] = 'users/login.html'
    return login(request, *args, **kwargs)


def find_user_type(email):
    staff = Staff.objects.filter(email=email)[0]

    ad = Admin.objects.filter(staff_ptr_id=staff.id)
    attendant = Attendant.objects.filter(staff_ptr_id=staff.id)
    receptionist = Receptionist.objects.filter(staff_ptr_id=staff.id)

    tp = ''
    if ad.exists():
        tp = 'admin'
    elif attendant.exists():
        tp = 'attendant'
    elif receptionist.exists():
        tp = 'receptionist'

    return tp


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('users:home')
    return logout(request, *args, **kwargs)


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


def register_patient(request):
    return render(request, 'user/login', {})


class RegistrationAttendantView(MultiModelFormView):
    '''
    form_class = RegistrationAttendantForm
    template_name = "users/registerAttendant.html"
    success_url = reverse_lazy('users:login')
    '''
    form_classes = {
        'registration_attendant_form': RegistrationAttendantForm,
        'address_form': AddressForm,
    }
    record_id = None
    template_name = 'users/registerAttendant.html'

    def get_form_kwargs(self):
        kwargs = super(RegistrationAttendantView, self).get_form_kwargs()
        kwargs['address_form']['prefix'] = 'address'
        return kwargs

    def get_objects(self):
        self.attendant_id = self.kwargs.get('attendant_id', None)
        try:
            attendant = Attendant.objects.get(id=self.attendant_id)
        except Attendant.DoesNotExist:
            attendant = None
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


class RegistrationReceptionistView(MultiModelFormView):
    '''
    form_class = RegistrationReceptionistForm
    template_name = "users/registerReceptionist.html"
    success_url = reverse_lazy('users:login')
    '''
    form_classes = {
        'registration_receptionist_form': RegistrationReceptionistForm,
        'address_form': AddressForm,
    }
    record_id = None
    template_name = 'users/registerReceptionist.html'

    def get_form_kwargs(self):
        kwargs = super(RegistrationReceptionistView, self).get_form_kwargs()
        kwargs['address_form']['prefix'] = 'address'
        return kwargs

    def get_objects(self):
        self.receptionist_id = self.kwargs.get('receptionist_id', None)
        try:
            receptionist = Receptionist.objects.get(id=self.receptionist_id)
        except Receptionist.DoesNotExist:
            receptionist = None
        return {
            'registration_receptionist_form': receptionist,
            'address_form': receptionist.address if receptionist else None,
        }

    def get_success_url(self):
        return reverse('users:login')

    def forms_valid(self, forms):
        receptionist = forms['registration_receptionist_form']\
                        .save(commit=False)
        receptionist.address = forms['address_form'].save()
        receptionist.save()
        return super(RegistrationReceptionistView, self).forms_valid(forms)


class RegistrationPatientView(MultiModelFormView):
    '''
    form_class = RegistrationPatientForm
    template_name = "users/registerPatient.html"
    success_url = reverse_lazy('users:home_receptionist')
    '''
    form_classes = {
        'registration_patient_form': RegistrationPatientForm,
        'address_form': AddressForm,
    }
    record_id = None
    template_name = 'users/registerPatient.html'

    def get_form_kwargs(self):
        kwargs = super(RegistrationPatientView, self).get_form_kwargs()
        kwargs['address_form']['prefix'] = 'address'
        return kwargs

    def get_objects(self):
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
        return reverse('users:login')

    def forms_valid(self, forms):
        patient = forms['registration_patient_form'].save(commit=False)
        patient.address = forms['address_form'].save()
        patient.save()
        return super(RegistrationPatientView, self).forms_valid(forms)


def show_pacient_view(request, cpf):
    patient = Patient.objects.filter(cpf=cpf)[0]
    return render(request, 'users/showPatient.html', {'patient': patient})


def home_receptionist_view(request):
    return render(request, 'users/homeReceptionist.html')
