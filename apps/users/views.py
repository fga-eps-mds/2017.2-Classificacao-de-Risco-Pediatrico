# Arquivo: /apps/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from apps.risk_rating.ml_classifier import MachineLearning
from apps.risk_rating.ml_classifier_range2 import MachineLearningRange2

from apps.users.forms import RegistrationStaffForm
from apps.users.forms import RegistrationPatientForm
from apps.users.forms import EditPatientForm


from .models import Patient, Staff

ml1 = MachineLearning('apps/risk_rating/class_menos_28.csv')
ml2 = MachineLearningRange2()
ml4 = MachineLearning('apps/risk_rating/class_10y+.csv')

def landing_page(request):
    return render(request, 'landing_page/landingPage.html', {})


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
    triggers the machine learning based on patient's age range
    """
    patients = Patient.objects.all()
    patient = None
    classification = None
    form = None
    if request.method == "POST":
            form = request.POST
            subject_patient_id = form.get("patient_id")
            subject_patient = Patient.objects.get(id=subject_patient_id)

            # machine learning methods are called here:
            if subject_patient.age_range == 1:
                patient = get_under_28_symptoms(form)
                probability = ml1.calc_probabilities(patient)
                classification = ml1.classify_patient(patient)
                impact_list = ml1.feature_importance()
            elif subject_patient.age_range == 2:
                patient = get_29d_2m_symptoms(form)
                probability = ml2.calc_probabilities(patient)
                classification = ml2.classify_patient(patient)
                impact_list = ml2.feature_importance()
            elif subject_patient.age_range == 4:
                patient = get_10yMore(form)
                probability = ml4.calc_probabilities(patient)
                classification = ml4.classify_patient(patient)
                impact_list = ml4.feature_importance()
            # to add another age range, use another elif
            else:
                pass

            define_patient_classification(subject_patient, classification)

            # printing the results:
            print(probability)
            print(classification)
            print(impact_list)

    return render(request, 'users/user_home/main_home.html',
                           {'patients': patients,
                            'classification': classification})


def define_patient_classification(subject_patient, classification):
    """
    edit patient's classification attribute
    """
    if classification == 'AtendimentoImediato':
        subject_patient.classification = 1
    elif classification == 'AmbulatorialGeral':
        subject_patient.classification = 2
    elif classification == 'AtendimentoHospitalar':
        subject_patient.classification = 3
    else:
        pass

    subject_patient.save()


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
    kwargs['next_page'] = reverse('users:landing_page')
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


def get_under_28_symptoms(form):
    """
    get symptoms from form to build patient's clinical condition
    """
    dispineia = check_patient_problem(form.get("dispineia"))
    ictericia = check_patient_problem(form.get("ictericia"))
    consciencia = check_patient_problem(form.get("consciência"))
    cianose = check_patient_problem(form.get("cianose"))
    febre = check_patient_problem(form.get("febre"))
    solucos = check_patient_problem(form.get("solucos"))
    prostracao = check_patient_problem(form.get("prostracao"))
    vomitos = check_patient_problem(form.get("vomitos"))
    tosse = check_patient_problem(form.get("tosse"))
    coriza = check_patient_problem(form.get("coriza"))
    obstrucaoNasal = check_patient_problem(form.get("obstrucaoNasal"))
    convulsaoMomento = check_patient_problem(form.get("convulsaoMomento"))
    diarreia = check_patient_problem(form.get("diarreia"))
    choroIncosolavel = check_patient_problem(form.get("choroIncosolavel"))
    dificuldadeEvacuar = check_patient_problem(form.get("dificuldadeEvacuar"))
    naoSugaSeio = check_patient_problem(form.get("naoSugaSeio"))
    manchaPele = check_patient_problem(form.get("manchaPele"))
    salivacao = check_patient_problem(form.get("salivacao"))
    queda = check_patient_problem(form.get("queda"))
    chiadoPeito = check_patient_problem(form.get("chiadoPeito"))
    diminuicaoDiurese = check_patient_problem(form.get("diminuicaoDiurese"))
    dorAbdominal = check_patient_problem(form.get("dorAbdominal"))
    dorOuvido = check_patient_problem(form.get("dorOuvido"))
    fontanelaAbaulada = check_patient_problem(form.get("fontanelaAbaulada"))
    secrecaoUmbigo = check_patient_problem(form.get("secrecaoUmbigo"))
    secrecaoOcular = check_patient_problem(form.get("secrecaoOcular"))
    sangueFezes = check_patient_problem(form.get("sangueFezes"))
    convulsaoHoje = check_patient_problem(form.get("convulsaoHoje"))

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

    return patient


def get_29d_2m_symptoms(form):
    """
    get symptoms from form to build patient's clinical condition
    """
    dispineia = check_patient_problem(form.get("dispineia"))
    ictericia = check_patient_problem(form.get("ictericia"))
    consciencia = check_patient_problem(form.get("consciência"))
    cianose = check_patient_problem(form.get("cianose"))
    febre = check_patient_problem(form.get("febre"))
    solucos = check_patient_problem(form.get("solucos"))
    prostracao = check_patient_problem(form.get("prostracao"))
    vomitos = check_patient_problem(form.get("vomitos"))
    tosse = check_patient_problem(form.get("tosse"))
    coriza = check_patient_problem(form.get("coriza"))
    obstrucaoNasal = check_patient_problem(form.get("obstrucaoNasal"))
    convulsaoMomento = check_patient_problem(form.get("convulsaoMomento"))
    diarreia = check_patient_problem(form.get("diarreia"))
    dificuldadeEvacuar = check_patient_problem(form.get("dificuldadeEvacuar"))
    naoSugaSeio = check_patient_problem(form.get("naoSugaSeio"))
    manchaPele = check_patient_problem(form.get("manchaPele"))
    salivacao = check_patient_problem(form.get("salivacao"))
    queda = check_patient_problem(form.get("queda"))
    chiadoPeito = check_patient_problem(form.get("chiadoPeito"))
    diminuicaoDiurese = check_patient_problem(form.get("diminuicaoDiurese"))
    dorAbdominal = check_patient_problem(form.get("dorAbdominal"))
    dorOuvido = check_patient_problem(form.get("dorOuvido"))
    fontanelaAbaulada = check_patient_problem(form.get("fontanelaAbaulada"))
    secrecaoUmbigo = check_patient_problem(form.get("secrecaoUmbigo"))
    secrecaoOcular = check_patient_problem(form.get("secrecaoOcular"))
    sangueFezes = check_patient_problem(form.get("sangueFezes"))
    convulsaoHoje = check_patient_problem(form.get("convulsaoHoje"))

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

    return patient


def get_10yMore(form):
    """
    get symptoms from form to build patient's clinical condition
    """
    mais72hFebre = check_patient_problem(form.get("mais72hrFebre"))
    menos72hrFebre = check_patient_problem(form.get("menos72hrFebre"))
    tontura = check_patient_problem(form.get("tontura"))
    corpoEstranho = check_patient_problem(form.get("corpoEstranho"))
    dorDeDente = check_patient_problem(form.get("dorDeDente"))
    disuria = check_patient_problem(form.get("disuria"))
    urinaConcentrada = check_patient_problem(form.get("urinaConcentrada"))
    dispineia = check_patient_problem(form.get("dispineia"))
    dorToracica = check_patient_problem(form.get("dorToracica"))
    choqueEletrico = check_patient_problem(form.get("choqueEletrico"))
    quaseAfogamento = check_patient_problem(form.get("quaseAfogamento"))
    artralgia = check_patient_problem(form.get("artralgia"))
    ictericia = check_patient_problem(form.get("ictericia"))
    perdaDaConsciencia = check_patient_problem(form.get("perdaDaConsciencia"))
    palidez = check_patient_problem(form.get("palidez"))
    cianose = check_patient_problem(form.get("cianose"))
    solucos = check_patient_problem(form.get("solucos"))
    prostracao = check_patient_problem(form.get("prostracao"))
    febre = check_patient_problem(form.get("febre"))
    vomitos = check_patient_problem(form.get("vomitos"))
    tosse = check_patient_problem(form.get("tosse"))
    coriza = check_patient_problem(form.get("coriza"))
    espirros = check_patient_problem(form.get("espirros"))
    hiperemiaConjuntival = check_patient_problem(form.get("hiperemiaConjuntival"))
    secrecaoOcular = check_patient_problem(form.get("secrecaoOcular"))
    obstrucaoNasal = check_patient_problem(form.get("obstrucaoNasal"))
    convulsao = check_patient_problem(form.get("convulsao"))
    diarreia = check_patient_problem(form.get("diarreia"))
    dificuldadeEvacuar = check_patient_problem(form.get("dificuldadeEvacuar"))
    cefaleia = check_patient_problem(form.get("cefaleia"))
    manchasNaPele = check_patient_problem(form.get("manchasNaPele"))
    salivacao = check_patient_problem(form.get("salivacao"))
    queda = check_patient_problem(form.get("queda"))
    hiporexia = check_patient_problem(form.get("hiporexia"))
    salivacao = check_patient_problem(form.get("salivacao"))
    hiporexia = check_patient_problem(form.get("hiporexia"))
    constipacao = check_patient_problem(form.get("constipacao"))
    chiadoNoPeito = check_patient_problem(form.get("chiadoNoPeito"))
    diminuicaoDaDiurese = check_patient_problem(form.get("diminuicaoDaDiurese"))
    dorAbdominal = check_patient_problem(form.get("dorAbdominal"))
    otalgia = check_patient_problem(form.get("otalgia"))
    epistaxe = check_patient_problem(form.get("epistaxe"))
    otorreia = check_patient_problem(form.get("otorreia"))
    edema = check_patient_problem(form.get("edema"))
    adenomegalias = check_patient_problem(form.get("adenomegalias"))
    dorArticular = check_patient_problem(form.get("dorArticular"))
    dificuldadesDeMarcha = check_patient_problem(form.get("dificuldadesDeMarcha"))
    sonolencia = check_patient_problem(form.get("sonolencia"))
    secrecaoOcular = check_patient_problem(form.get("secrecaoOcular"))
    dorMuscular = check_patient_problem(form.get("dorMuscular"))
    dorRetroobitaria = check_patient_problem(form.get("dorRetroobitaria"))

    patient = [[
        mais72hrFebre,
        menos72hrFebre,
        tontura,
        corpoEstranho,
        dorDeDente,
        disuria,
        urinaConcentrada,
        dispineia,
        dorToracica,
        choqueEletrico,
        quaseAfogamento,
        artralgia,
        ictericia,
        perdaDaConsciencia,
        palidez,
        cianose,
        solucos,
        prostracao,
        febre,
        vomitos,
        tosse,
        coriza,
        espirros,
        hiperemiaConjuntival,
        secrecaoOcular,
        obstrucaoNasal,
        convulsao,
        diarreia,
        dificuldadeEvacuar,
        cefaleia,
        manchasNaPele,
        salivacao,
        queda,
        hiporexia,
        salivacao,
        hiporexia,
        constipacao,
        chiadoNoPeito,
        diminuicaoDaDiurese,
        dorAbdominal,
        otalgia,
        epistaxe,
        otorreia,
        edema,
        adenomegalias,
        dorArticular,
        dificuldadesDeMarcha,
        sonolencia,
        secrecaoOcular,
        dorMuscular,
        dorRetroobitaria,
    ]]

    return patient