# Arquivo: /apps/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate

from apps.users.forms import RegistrationStaffForm
from apps.users.forms import RegistrationPatientForm
from apps.users.forms import EditPatientForm


from .models import Patient, Staff, QueuedPatient


def login_view(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_admin:
                login(request, user)
                return redirect("/home/admin")

            if user.profile == 1:
                login(request, user)
                return redirect("/home/receptionist/")

            if user.profile == 2:
                login(request, user)
                return redirect("/home/attendant/")
        else:

            kwargs['extra_context'] = {'next': reverse('users:login'),
                                       'errors': 'Usuário e/ou senha inválido.'
                                       }

            kwargs['template_name'] = 'users/login.html'
            return login(request, *args, **kwargs)

    kwargs['extra_context'] = {'next': reverse('users:login')}
    kwargs['template_name'] = 'users/login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    """
    Define the logout page
    """
    kwargs['next_page'] = reverse('users:login')
    return logout(request, *args, **kwargs)


def sign_up_profile(request):
    if request.method == 'POST':
        form = RegistrationStaffForm(request.POST)
        form.is_valid()
        form.non_field_errors()
        # [print(field.label, field.name, field.errors) for field in form]
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            username = authenticate(username=username, password=raw_password)
            login(request, 'users:login')
            return redirect('users:login')
        else:
            status = 400
    else:
        form = RegistrationStaffForm()
        status = 200
    return render(request, 'users/registerProfile.html', {'form': form},
                  status=status)


def sign_up_patient(request):
    if request.method == 'POST':
        form = RegistrationPatientForm(request.POST)
        form.is_valid()
        form.non_field_errors()
        # [print(field.label, field.name, field.errors) for field in form]

        if form.is_valid():
            form.save()
            cpf_patient = form.cleaned_data.get('cpf')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            username = authenticate(username=username, password=raw_password)
            login(request, 'users:login')
            return redirect('users:registered_patient')
        else:
            status = 400
    else:
        form = RegistrationPatientForm()
        status = 200
    return render(request, 'users/registerPatient.html', {'form': form},
                  status=status)


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


def registered_patient_view(request):
    patients = Patient.objects.all()
    return render(request, 'users/registeredPatient.html',
                           {'patients': patients})


def queue_patient(request, cpf_patient):
    patients = Patient.objects.filter(cpf=cpf_patient)
    allPatients = Patient.objects.all()
    patient = Patient.objects.get(cpf=cpf_patient)
    patientsInQueue = QueuedPatient.objects.all()
    patientList = list()
    for patient0 in patientsInQueue:
        patientList.append(patient0.patient)
    if patient in patientList:
        return render(request, 'users/queuePatient.html',
                               {'patientList': patientList})
    else:
        queuedPatient = QueuedPatient.objects.create(patient = patient)
        queuedPatient.save()
        patientList.append(patient)
        return render(request, 'users/queuePatient.html',
                               {'patientList': patientList})
    return render(request, 'users/queuePatient.html', {'patientList': patientList})


def manage_accounts_view(request):
    staffs = Staff.objects.all()
    return render(request, 'users/manageAccounts.html', {'staffs': staffs})


def edit_accounts_view(request, id_user):
    staff = Staff.objects.filter(id_user=id_user)
    if len(staff) == 1:
        return render(request, 'users/editAccounts.html', {'staff': staff[0]})
    return render(request, 'users/editAccounts.html', status=404)


def staff_remove(request, id_user):
    staff = Staff.objects.filter(id_user=id_user)
    staff.delete()
    return HttpResponseRedirect(reverse('users:manage_accounts'))


def patient_remove(request, cpf):
    patient = Patient.objects.filter(cpf=cpf)
    patient.delete()
    return HttpResponseRedirect(reverse('users:manage_patients'))


def edit_patient(request, cpf):
    """
    edit an existing patient with post method
    """
    patient = Patient.objects.filter(cpf=cpf)[0]
    form = EditPatientForm()

    if request.method == 'POST':
        form = EditPatientForm(request.POST, instance=patient)
        form.is_valid()
        form.non_field_errors()

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            username = authenticate(username=username, password=raw_password)
            return redirect('users:manage_patients')
        else:
            status = 400
            return render(request, 'users/editPatient.html',
                          {'patient': patient, 'form': form}, status=status)
    else:
        return render(request, 'users/editPatient.html',
                      {'patient': patient, 'form': form})


def queue_patient_view(request):
    patientsInQueue = QueuedPatient.objects.all()
    patientList = list()
    for onePatient in patientsInQueue:
        patientList.append(onePatient.patient)
    return render(request, 'users/queuePatient.html',
                           {'patientList': patientList})


def classification_view(request):
    return render(request, 'users/classification.html')


def classification(request, cpf_patient):
    patient = Patient.objects.filter(cpf=cpf_patient)
    chosenPatient = QueuedPatient.objects.filter(patient = patient)
    chosenPatient.delete()
    return render(request, 'users/classification.html', {'patient': patient})


def show_pacient_view(request, cpf):
    """
    return rendered text from showPatient
    """
    patient = Patient.objects.filter(cpf=cpf)
    if len(patient) == 1:
        return render(request, 'users/showPatient.html', {'patient': patient})
    return render(request, 'users/showPatient.html', status=404)


def home_receptionist_view(request):
    """
    return rendered text from homeReceptionist
    """
    return render(request, 'users/homeReceptionist.html')


def manage_patients_view(request):
    patients = Patient.objects.all()
    search = request.GET.get('q')
    if search:
        patients = patients.filter(
            Q(name__icontains=search) |
            Q(cpf__icontains=search)
            )
    return render(request, 'users/managePatients.html', {'patients': patients})
