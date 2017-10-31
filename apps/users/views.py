# Arquivo: /apps/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from apps.risk_rating.ml_classifier import MachineLearning

from apps.users.forms import RegistrationStaffForm
from apps.users.forms import RegistrationPatientForm
from apps.users.forms import EditPatientForm


from .models import Patient, Staff

ml = MachineLearning()

def login_view(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/home")
        else:

            kwargs['extra_context'] = {'next': reverse('users:login'),
                                       'errors': 'Usuário e/ou senha inválido.'
                                       }

            kwargs['template_name'] = 'users/user_login/login.html'
            return login(request, *args, **kwargs)

    kwargs['extra_context'] = {'next': reverse('users:login')}
    kwargs['template_name'] = 'users/user_login/login.html'
    return login(request, *args, **kwargs)


@login_required(redirect_field_name='', login_url='users:login')
def home(request):
    """
    return rendered text from homeReceptionist
    """
    patients = Patient.objects.all()

    if request.method == "POST":
        if request.POST.get("classification"):
            patient_classification = request.POST.get("classification")
            patient_id = request.POST.get("patient")

            patient = Patient.objects.get(id=patient_id)
            patient.classification = patient_classification

            patient.save()
        else:
            dispineia = check_patient_problem(request.POST.get("dispineia"))
            ictericia = check_patient_problem(request.POST.get("ictericia"))
            consciencia = check_patient_problem(request.POST.get("consciência"))
            cianose = check_patient_problem(request.POST.get("cianose"))
            febre = check_patient_problem(request.POST.get("febre"))
            solucos = check_patient_problem(request.POST.get("solucos"))
            prostracao = check_patient_problem(request.POST.get("prostracao"))
            vomitos = check_patient_problem(request.POST.get("vomitos"))
            tosse = check_patient_problem(request.POST.get("tosse"))
            coriza = check_patient_problem(request.POST.get("coriza"))
            obstrucaoNasal = check_patient_problem(request.POST.get("obstrucaoNasal"))
            convulsaoMomento = check_patient_problem(request.POST.get("convulsaoMomento"))
            diarreia = check_patient_problem(request.POST.get("diarreia"))
            choroIncosolavel = check_patient_problem(request.POST.get("choroIncosolavel"))
            dificuldadeEvacuar = check_patient_problem(request.POST.get("dificuldadeEvacuar"))
            naoSugaSeio = check_patient_problem(request.POST.get("naoSugaSeio"))
            manchaPele = check_patient_problem(request.POST.get("manchaPele"))
            salivacao = check_patient_problem(request.POST.get("salivacao"))
            queda = check_patient_problem(request.POST.get("queda"))
            chiadoPeito = check_patient_problem(request.POST.get("chiadoPeito"))
            diminuicaoDiurese = check_patient_problem(request.POST.get("diminuicaoDiurese"))
            dorAbdominal = check_patient_problem(request.POST.get("dorAbdominal"))
            dorOuvido = check_patient_problem(request.POST.get("dorOuvido"))
            fontanelaAbaulada = check_patient_problem(request.POST.get("fontanelaAbaulada"))
            secrecaoUmbigo = check_patient_problem(request.POST.get("secrecaoUmbigo"))
            secrecaoOcular = check_patient_problem(request.POST.get("secrecaoOcular"))
            sangueFezes = check_patient_problem(request.POST.get("sangueFezes"))
            convulsaoHoje = check_patient_problem(request.POST.get("convulsaoHoje"))

            patient = [[
                dispineia,
                ictericia,
                consciencia,
                cianose,
                febre,
                solucos,
                prostracao,
                vomitos,
                tosse,
                coriza,
                obstrucaoNasal,
                convulsaoMomento,
                diarreia,
                choroIncosolavel,
                dificuldadeEvacuar,
                naoSugaSeio,
                manchaPele,
                salivacao,
                queda,
                chiadoPeito,
                diminuicaoDiurese,
                dorAbdominal,
                dorOuvido,
                fontanelaAbaulada,
                secrecaoUmbigo,
                secrecaoOcular,
                sangueFezes,
                convulsaoHoje,
            ]]

            probability = ml.calc_probabilities(patient)
            classification = ml.classify_patient(patient)
            impact_list = ml.feature_importance()

            print(probability)
            print(classification)
            print(impact_list)

    return render(request, 'users/user_home/main_home.html',
                           {'patients': patients})

def check_patient_problem(problem):
    if problem is not None:
        problem = 1
    else:
        problem = 0

    return problem


def logout_view(request, *args, **kwargs):
    """
    Define the logout page
    """
    kwargs['next_page'] = reverse('users:login')
    return logout(request, *args, **kwargs)


def sign_up_profile(request):
    form = RegistrationStaffForm()
    if request.method == 'POST':
        form = RegistrationStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:home')

    return render(request, 'users/user_login/registerUser.html',
                  {'form': form})


@login_required(redirect_field_name='', login_url='users:login')
def register_patient(request):
    form = RegistrationPatientForm()
    if request.method == 'POST':
        form = RegistrationPatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users:home')

    return render(request, 'users/user_home/registerPatient.html',
                  {'form': form})


@login_required(redirect_field_name='', login_url='users:login')
def queue_patient(request, cpf_patient):
    patients = Patient.objects.filter(cpf=cpf_patient)
    patient = Patient.objects.get(cpf=cpf_patient)
    patientsInQueue = Patient.objects.all()
    patientList = list()
    for patient0 in patientsInQueue:
        patientList.append(patient0.patient)
    if patient in patientList:
        return render(request, 'users/queuePatient.html',
                               {'patientList': patientList})
    else:
        queuedPatient = Patient.objects.create(patient=patient)
        queuedPatient.save()
        patientList.append(patient)
        return render(request, 'users/queuePatient.html',
                               {'patients': patients})
    return render(request, 'users/queuePatient.html', {'patients': patients})


@login_required(redirect_field_name='', login_url='users:login')
def manage_accounts_view(request):
    staffs = Staff.objects.all()
    return render(request, 'users/manageAccounts.html', {'staffs': staffs})


@login_required(redirect_field_name='', login_url='users:login')
def edit_accounts_view(request, id_user):
    staff = Staff.objects.filter(id_user=id_user)
    if len(staff) == 1:
        return render(request, 'users/editAccounts.html', {'staff': staff[0]})
    return render(request, 'users/editAccounts.html', status=404)


@login_required(redirect_field_name='', login_url='users:login')
def staff_remove(request, id_user):
    staff = Staff.objects.filter(id_user=id_user)
    staff.delete()
    return HttpResponseRedirect(reverse('users:manage_accounts'))


@login_required(redirect_field_name='', login_url='users:login')
def patient_remove(request, cpf):
    patient = Patient.objects.filter(cpf=cpf)
    patient.delete()
    return HttpResponseRedirect(reverse('users:home'))


@login_required(redirect_field_name='', login_url='users:login')
def edit_patient(request, cpf):
    """
    edit an existing patient with post method
    """
    patient = Patient.objects.filter(cpf=cpf)[0]
    form = EditPatientForm()

    status = 200

    if request.method == 'POST':
        form = EditPatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('users:home')
        else:
            status = 400
    return render(request, 'users/editPatient.html',
                  {'patient': patient, 'form': form}, status=status)


@login_required(redirect_field_name='', login_url='users:login')
def show_patient_view(request, cpf):
    """
    return rendered text from showPatient
    """
    patient = Patient.objects.filter(cpf=cpf)
    if len(patient) == 1:
        return render(request, 'users/showPatient.html', {'patient': patient})
    return render(request, 'users/showPatient.html', status=404)
