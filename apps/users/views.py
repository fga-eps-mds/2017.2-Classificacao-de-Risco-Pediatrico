# Arquivo: /apps/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from apps.risk_rating.ml_classifier import MachineLearning
from apps.users.forms import RegistrationStaffForm
from apps.users.forms import RegistrationPatientForm
from apps.users.forms import EditPatientForm

from .models import Patient, Staff

from apps.risk_rating.forms import ClinicalState_28dForm
from apps.risk_rating.forms import ClinicalState_29d_2mForm
from apps.risk_rating.forms import ClinicalState_2m_3yForm
from apps.risk_rating.forms import ClinicalState_3y_10yForm
from apps.risk_rating.forms import ClinicalState_10yMoreForm
from apps.risk_rating.forms import MachineLearning_28dForm
from apps.risk_rating.forms import MachineLearning_29d_2mForm
from apps.risk_rating.forms import MachineLearning_2m_3yForm
from apps.risk_rating.forms import MachineLearning_3y_10yForm
from apps.risk_rating.forms import MachineLearning_10yMoreForm

from apps.risk_rating.models import ClinicalState_28d
from apps.risk_rating.models import ClinicalState_29d_2m
from apps.risk_rating.models import ClinicalState_2m_3y
from apps.risk_rating.models import ClinicalState_3y_10y
from apps.risk_rating.models import ClinicalState_10yMore


ml1 = MachineLearning('apps/risk_rating/class_menos_28.csv')
ml2 = MachineLearning('apps/risk_rating/class_29d_2m.csv')
ml3 = MachineLearning('apps/risk_rating/class_2m_3y.csv')
ml4 = MachineLearning('apps/risk_rating/class_3y_10y.csv')
ml5 = MachineLearning('apps/risk_rating/class_10y+.csv')


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
@csrf_exempt
def machine_learning(request):

    if 'form1' in request.POST:
        form = ClinicalState_28dForm(request.POST)
        form.save()
        state = ClinicalState_28d
        ml = ml1
    elif "form2" in request.POST:
        form = ClinicalState_29d_2mForm(request.POST)
        form.save()
        state = ClinicalState_29d_2m
        ml = ml2
    elif "form3" in request.POST:
        form = ClinicalState_2m_3yForm(request.POST)
        form.save()
        state = ClinicalState_2m_3y
        ml = ml3
    elif "form4" in request.POST:
        form = ClinicalState_3y_10yForm(request.POST)
        form.save()
        state = ClinicalState_3y_10y
        ml = ml4
    elif "form5" in request.POST:
        form = ClinicalState_10yMoreForm(request.POST)
        form.save()
        state = ClinicalState_10yMore
        ml = ml5

    p_id = request.POST.get("patient_id")
    subject_patient = Patient.objects.filter(id=p_id)[0]

    p_c_states_l = state.objects.filter(patient_id=p_id)
    clinical_state = p_c_states_l.order_by('-id')[0]
    ml_data = trigger_ml(subject_patient, clinical_state, ml)
    ml_data["patient_id"] = p_id
    ml_data["classifier_id"] = request.user.id_user

    return JsonResponse(ml_data)


@login_required(redirect_field_name='', login_url='users:login')
def home(request):
    """
    define home page behavior
    """
    form1 = ClinicalState_28dForm()
    form2 = ClinicalState_29d_2mForm()
    form3 = ClinicalState_2m_3yForm()
    form4 = ClinicalState_3y_10yForm()
    form5 = ClinicalState_10yMoreForm()
    patients = Patient.objects.all()
    classification = None

    if request.method == 'POST' and request.POST.get("classification"):
        classification = request.POST.get("classification")
        patient_id = request.POST.get("patient")
        define_patient_classification(patient_id, classification)

        patient = Patient.objects.filter(id=patient_id)[0]
        patient.comment_receptionist = request.POST.get('comment')
        patient.classifier_id = request.user.id_user
        patient.save()

    return render(request, 'users/user_home/main_home.html',
                           {'patients': patients,
                            'classification': classification,
                            'form1': form1,
                            'form2': form2,
                            'form3': form3,
                            'form4': form4,
                            'form5': form5})


def feed_ml(request):
    """
    define feed machine learning page behaviour
    """
    form1_ml = MachineLearning_28dForm()
    form2_ml = MachineLearning_29d_2mForm()
    form3_ml = MachineLearning_2m_3yForm()
    form4_ml = MachineLearning_3y_10yForm()
    form5_ml = MachineLearning_10yMoreForm()

    if request.method == 'POST':
        if "form1_ml" in request.POST:
            form = MachineLearning_28dForm(request.POST)

        elif "form2_ml" in request.POST:
            form = MachineLearning_29d_2mForm(request.POST)

        elif "form3_ml" in request.POST:
            form = MachineLearning_2m_3yForm(request.POST)

        elif "form4_ml" in request.POST:
            form = MachineLearning_3y_10yForm(request.POST)

        elif "form5_ml" in request.POST:
            form = MachineLearning_10yMoreForm(request.POST)

        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('users:feed_ml'))

    return render(request, 'users/user_home/feed_ml.html',
                           {'form1_ml': form1_ml,
                            'form2_ml': form2_ml,
                            'form3_ml': form3_ml,
                            'form4_ml': form4_ml,
                            'form5_ml': form5_ml})


def trigger_ml(subject_patient, clinical_state, ml):
    """
    triggers the machine learning based on patient's age range
    """
    if subject_patient.age_range == 1:
        patient = get_under_28_symptoms(clinical_state)
    elif subject_patient.age_range == 2:
        patient = get_29d_2m_symptoms(clinical_state)
        # due to the lack of data, this classification is
        # always being "AmbulatorialGeral"
    elif subject_patient.age_range == 3:
        patient = get_2m_3y_symptoms(clinical_state)
    elif subject_patient.age_range == 4:
        patient = get_3y_10y_symptoms(clinical_state)
    elif subject_patient.age_range == 5:
        patient = get_10y_more_symptoms(clinical_state)
    # to add another age range, use another elif

    probability = ml.calc_probabilities(patient)
    classification = ml.classify_patient(patient)
    impact_list = ml.feature_importance()

    ml_array = {
        'probability': probability.tolist(),
        'classification': classification,
        'impact_list': impact_list
    }

    # define_patient_classification(subject_patient, classification)
    return ml_array


def define_patient_classification(patient_id, classification):
    """
    edit patient's classification attribute
    """
    patient = Patient.objects.filter(id=patient_id)[0]
    patient.classification = classification
    patient.save()


def check_patient_problem(problem):
    if problem is not None and problem is True:
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
            return redirect('users:login')

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
    """Remove an existing staff."""
    return remove_register(id_user, Staff, 'manage_accounts')


@login_required(redirect_field_name='', login_url='users:login')
def patient_remove(request, id):
    """Remove an existing patient."""
    return remove_register(id, Patient, 'home')


def remove_register(id, data_type, url):
    """Remove register data based on parameter."""
    if data_type == Staff:
        data = data_type.objects.filter(id_user=id)
    else:
        data = data_type.objects.filter(id=id)

    data.delete()
    return HttpResponseRedirect(reverse('users:' + url))


@login_required(redirect_field_name='', login_url='users:login')
def edit_patient(request, id):
    """
    edit an existing patient with post method
    """
    patient = Patient.objects.filter(id=id)[0]
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


def classifications_chart(request):
    """
    exhibit a pie chart of the classifications
    """
    imediato = Patient.objects.filter(classification=1).count()
    hospitalar = Patient.objects.filter(classification=2).count()
    ambulatorial = Patient.objects.filter(classification=3).count()
    eletivo = Patient.objects.filter(classification=4).count()

    data = [{'value':imediato, 'name':'Atendimento Imediato'},
            { 'value':hospitalar, 'name':'Atendimento Hospitalar'},
            { 'value':ambulatorial, 'name':'Atendimento Ambulatorial'},
            { 'value':eletivo, 'name':'Atendimento Eletivo'}]


    # data2 = [imediato, hospitalar, ambulatorial, eletivo]

    data3 = {'AtendimentoImediato':imediato,'AtendimentoHospitalar':hospitalar,
             'AtendimentoAmbulatorial':ambulatorial, 'AtendimentoEletivo':eletivo}

    print (data3['AtendimentoAmbulatorial'])

    return render(request, 'users/classifications_chart.html', {'data': data3})


@login_required(redirect_field_name='', login_url='users:login')
def my_history(request):
    """
    define history page behavior
    """
    patients = Patient.objects.filter(classifier_id=request.user.id_user)
    classifier = Staff.objects.filter(id_user=request.user.id_user)[0]
    return render(request, 'users/myHistory.html',
                  {'patients': patients, "classifier": classifier})

@login_required(redirect_field_name='', login_url='users:login')
def graphic_symptoms_view_28d(request):
    """
    Read all symptoms of database after classification
     someone and check which symptoms was marked
    """
    graphic_symptoms = {}

    for column in ClinicalState_28d._meta.get_fields():
        graphic_symptoms[column.name] = 0

    for state in ClinicalState_28d.objects.all():

        if request.method == 'POST':
            if int(request.POST.get('month')) != 0:
                if state.date.month != int(request.POST.get('month')):
                    break
        for column in ClinicalState_28d._meta.get_fields():
            if getattr(state, column.name):
                graphic_symptoms[column.name] += 1

    return render(request, 'users/user_home/graphic_symptoms_28d.html',
                  {'graphic_symptoms': graphic_symptoms})


@login_required(redirect_field_name='', login_url='users:login')
def graphic_symptoms_view_29d_2m(request):
    """
    Read all symptoms of database after classification
     someone and check which symptoms was marked
    """
    graphic_symptoms = {}

    for column in ClinicalState_29d_2m._meta.get_fields():
        graphic_symptoms[column.name] = 0

    for state in ClinicalState_29d_2m.objects.all():

        if request.method == 'POST':
            if int(request.POST.get('month')) != 0:
                if state.date.month != int(request.POST.get('month')):
                    break
        for column in ClinicalState_29d_2m._meta.get_fields():
            if getattr(state, column.name):
                graphic_symptoms[column.name] += 1

    return render(request, 'users/user_home/graphic_symptoms_29d_2m.html',
                  {'graphic_symptoms': graphic_symptoms})


def graphic_symptoms_view_2m_3y(request):
    """
    Read all symptoms of database after classification
     someone and check which symptoms was marked
    """
    graphic_symptoms = {}

    for column in ClinicalState_2m_3y._meta.get_fields():
        graphic_symptoms[column.name] = 0

    for state in ClinicalState_2m_3y.objects.all():

        if request.method == 'POST':
            if int(request.POST.get('month')) != 0:
                if state.date.month != int(request.POST.get('month')):
                    break
        for column in ClinicalState_2m_3y._meta.get_fields():
            if getattr(state, column.name):
                graphic_symptoms[column.name] += 1

    return render(request, 'users/user_home/graphic_symptoms_2m_3y.html',
                  {'graphic_symptoms': graphic_symptoms})


def graphic_symptoms_view_3y_10y(request):
    """
    Read all symptoms of database after classification
     someone and check which symptoms was marked
    """
    graphic_symptoms = {}

    for column in ClinicalState_3y_10y._meta.get_fields():
        graphic_symptoms[column.name] = 0

    for state in ClinicalState_3y_10y.objects.all():

        if request.method == 'POST':
            if int(request.POST.get('month')) != 0:
                if state.date.month != int(request.POST.get('month')):
                    break
        for column in ClinicalState_3y_10y._meta.get_fields():
            if getattr(state, column.name):
                graphic_symptoms[column.name] += 1

    return render(request, 'users/user_home/graphic_symptoms_3y_10y.html',
                  {'graphic_symptoms': graphic_symptoms})


def graphic_symptoms_view_10y_more(request):
    """
    Read all symptoms of database after classification
     someone and check which symptoms was marked
    """
    graphic_symptoms = {}

    for column in ClinicalState_10yMore._meta.get_fields():
        graphic_symptoms[column.name] = 0

    for state in ClinicalState_10yMore.objects.all():

        if request.method == 'POST':
            if int(request.POST.get('month')) != 0:
                if state.date.month != int(request.POST.get('month')):
                    break
        for column in ClinicalState_10yMore._meta.get_fields():
            if getattr(state, column.name):
                graphic_symptoms[column.name] += 1

    return render(request, 'users/user_home/graphic_symptoms_10yMore.html',
                  {'graphic_symptoms': graphic_symptoms})


def get_under_28_symptoms(clinical_state):
    """
    building patient (28d) to use on ml based on patient's clinical condition
    """
    patient = [[
        check_patient_problem(clinical_state.dispineia),
        check_patient_problem(clinical_state.ictericia),
        check_patient_problem(clinical_state.perdada_consciencia),
        check_patient_problem(clinical_state.cianose),
        check_patient_problem(clinical_state.febre),
        check_patient_problem(clinical_state.solucos),
        check_patient_problem(clinical_state.prostracao),
        check_patient_problem(clinical_state.vomitos),
        check_patient_problem(clinical_state.tosse),
        check_patient_problem(clinical_state.coriza),
        check_patient_problem(clinical_state.obstrucao_nasal),
        check_patient_problem(clinical_state.convulcao_no_momento),
        check_patient_problem(clinical_state.diarreia),
        check_patient_problem(clinical_state.choro_inconsolavel),
        check_patient_problem(clinical_state.dificuldade_evacuar),
        check_patient_problem(clinical_state.nao_suga_seio),
        check_patient_problem(clinical_state.manchas_na_pele),
        check_patient_problem(clinical_state.salivacao),
        check_patient_problem(clinical_state.queda),
        check_patient_problem(clinical_state.chiado_no_peito),
        check_patient_problem(clinical_state.diminuicao_da_diurese),
        check_patient_problem(clinical_state.dor_abdominal),
        check_patient_problem(clinical_state.dor_de_ouvido),
        check_patient_problem(clinical_state.fontanela_abaulada),
        check_patient_problem(clinical_state.secrecao_no_umbigo),
        check_patient_problem(clinical_state.secrecao_ocular),
        check_patient_problem(clinical_state.sangue_nas_fezes),
        check_patient_problem(clinical_state.convulsao_hoje)
    ]]
    return patient


def get_29d_2m_symptoms(clinical_state):
    """
    building patient (29d-2m) to use on ml based on
    patient's clinical condition
    """
    patient = [[
        check_patient_problem(clinical_state.dispineia),
        check_patient_problem(clinical_state.ictericia),
        check_patient_problem(clinical_state.perdada_consciencia),
        check_patient_problem(clinical_state.cianose),
        check_patient_problem(clinical_state.febre),
        check_patient_problem(clinical_state.solucos),
        check_patient_problem(clinical_state.prostracao),
        check_patient_problem(clinical_state.vomitos),
        check_patient_problem(clinical_state.tosse),
        check_patient_problem(clinical_state.coriza),
        check_patient_problem(clinical_state.obstrucao_nasal),
        check_patient_problem(clinical_state.convulcao_no_momento),
        check_patient_problem(clinical_state.diarreia),
        check_patient_problem(clinical_state.dificuldade_evacuar),
        check_patient_problem(clinical_state.nao_suga_seio),
        check_patient_problem(clinical_state.manchas_na_pele),
        check_patient_problem(clinical_state.salivacao),
        check_patient_problem(clinical_state.queda),
        check_patient_problem(clinical_state.chiado_no_peito),
        check_patient_problem(clinical_state.diminuicao_da_diurese),
        check_patient_problem(clinical_state.dor_abdominal),
        check_patient_problem(clinical_state.dor_de_ouvido),
        check_patient_problem(clinical_state.fontanela_abaulada),
        check_patient_problem(clinical_state.secrecao_no_umbigo),
        check_patient_problem(clinical_state.secrecao_ocular),
        check_patient_problem(clinical_state.sangue_nas_fezes),
        check_patient_problem(clinical_state.convulsao_hoje)
    ]]
    return patient


def get_2m_3y_symptoms(clinical_state):
    """
    building patient (2m-3y) to use on ml based on
    patient's clinical condition
    """
    patient = [[
        check_patient_problem(clinical_state.dispineia),
        check_patient_problem(clinical_state.ictericia),
        check_patient_problem(clinical_state.perdada_consciencia),
        check_patient_problem(clinical_state.cianose),
        check_patient_problem(clinical_state.febre),
        check_patient_problem(clinical_state.solucos),
        check_patient_problem(clinical_state.prostracao),
        check_patient_problem(clinical_state.vomitos),
        check_patient_problem(clinical_state.tosse),
        check_patient_problem(clinical_state.coriza),
        check_patient_problem(clinical_state.obstrucao_nasal),
        check_patient_problem(clinical_state.convulcao_no_momento),
        check_patient_problem(clinical_state.diarreia),
        check_patient_problem(clinical_state.dificuldade_evacuar),
        check_patient_problem(clinical_state.nao_suga_seio),
        check_patient_problem(clinical_state.manchas_na_pele),
        check_patient_problem(clinical_state.salivacao),
        check_patient_problem(clinical_state.queda),
        check_patient_problem(clinical_state.chiado_no_peito),
        check_patient_problem(clinical_state.diminuicao_da_diurese),
        check_patient_problem(clinical_state.dor_abdominal),
        check_patient_problem(clinical_state.dor_de_ouvido),
        check_patient_problem(clinical_state.fontanela_abaulada),
        check_patient_problem(clinical_state.secrecao_no_umbigo),
        check_patient_problem(clinical_state.secrecao_ocular)
    ]]
    return patient


def get_3y_10y_symptoms(clinical_state):
    """
    building patient (3y-10y) to use on ml based on
    patient's clinical condition
    """
    patient = [[
        check_patient_problem(clinical_state.perdada_consciencia),
        check_patient_problem(clinical_state.febre_maior_72h),
        check_patient_problem(clinical_state.febre_menos_72h),
        check_patient_problem(clinical_state.odinofagia),
        check_patient_problem(clinical_state.fascies_de_dor),
        check_patient_problem(clinical_state.tontura),
        check_patient_problem(clinical_state.corpo_estranho),
        check_patient_problem(clinical_state.dor_dentes),
        check_patient_problem(clinical_state.disuria),
        check_patient_problem(clinical_state.urina_concentrada),
        check_patient_problem(clinical_state.dispineia),
        check_patient_problem(clinical_state.dor_toracica),
        check_patient_problem(clinical_state.choque_eletrico),
        check_patient_problem(clinical_state.quase_afogamento),
        check_patient_problem(clinical_state.artralgia),
        check_patient_problem(clinical_state.ictericia),
        check_patient_problem(clinical_state.perda_consciencia),
        check_patient_problem(clinical_state.palidez),
        check_patient_problem(clinical_state.cianose),
        check_patient_problem(clinical_state.solucos),
        check_patient_problem(clinical_state.prostracao),
        check_patient_problem(clinical_state.febre),
        check_patient_problem(clinical_state.vomitos),
        check_patient_problem(clinical_state.tosse),
        check_patient_problem(clinical_state.coriza),
        check_patient_problem(clinical_state.espirros),
        check_patient_problem(clinical_state.hiperemia_conjuntival),
        check_patient_problem(clinical_state.secrecao_ocular),
        check_patient_problem(clinical_state.obstrucao_nasal),
        check_patient_problem(clinical_state.convulsao),
        check_patient_problem(clinical_state.diarreia),
        check_patient_problem(clinical_state.manchas_na_pele),
        check_patient_problem(clinical_state.queda),
        check_patient_problem(clinical_state.hiporexia),
        check_patient_problem(clinical_state.salivacao),
        check_patient_problem(clinical_state.constipacao),
        check_patient_problem(clinical_state.chiado_no_peito),
        check_patient_problem(clinical_state.diminuicao_da_diurese),
        check_patient_problem(clinical_state.dor_abdominal),
        check_patient_problem(clinical_state.otalgia),
        check_patient_problem(clinical_state.epistaxe),
        check_patient_problem(clinical_state.otorreia),
        check_patient_problem(clinical_state.edema),
        check_patient_problem(clinical_state.adenomegalias),
        check_patient_problem(clinical_state.dor_articular),
        check_patient_problem(clinical_state.dificulade_de_marchar),
        check_patient_problem(clinical_state.sonolencia),
        check_patient_problem(clinical_state.dor_muscular),
        check_patient_problem(clinical_state.dor_retroorbitaria)
    ]]
    return patient


def get_10y_more_symptoms(clinical_state):
    """
    building patient (10y+) to use on ml based on
    patient's clinical condition
    """
    patient = [[
        check_patient_problem(clinical_state.mais_de_72h_febre),
        check_patient_problem(clinical_state.menos_de_72h_febre),
        check_patient_problem(clinical_state.tontura),
        check_patient_problem(clinical_state.corpo_estranho),
        check_patient_problem(clinical_state.dor_de_dente),
        check_patient_problem(clinical_state.disuria),
        check_patient_problem(clinical_state.urina_concentrada),
        check_patient_problem(clinical_state.dispineia),
        check_patient_problem(clinical_state.dor_toracica),
        check_patient_problem(clinical_state.choque_eletrico),
        check_patient_problem(clinical_state.quase_afogamento),
        check_patient_problem(clinical_state.artralgia),
        check_patient_problem(clinical_state.ictericia),
        check_patient_problem(clinical_state.perda_da_consciencia),
        check_patient_problem(clinical_state.palidez),
        check_patient_problem(clinical_state.cianose),
        check_patient_problem(clinical_state.solucos),
        check_patient_problem(clinical_state.prostracao),
        check_patient_problem(clinical_state.febre),
        check_patient_problem(clinical_state.vomitos),
        check_patient_problem(clinical_state.tosse),
        check_patient_problem(clinical_state.coriza),
        check_patient_problem(clinical_state.espirros),
        check_patient_problem(clinical_state.hiperemia_conjuntival),
        check_patient_problem(clinical_state.secrecao_ocular),
        check_patient_problem(clinical_state.obstrucao_nasal),
        check_patient_problem(clinical_state.convulsao),
        check_patient_problem(clinical_state.diarreia),
        check_patient_problem(clinical_state.dificuldade_evacuar),
        check_patient_problem(clinical_state.cefaleia),
        check_patient_problem(clinical_state.manchas_na_pele),
        check_patient_problem(clinical_state.salivacao),
        check_patient_problem(clinical_state.queda),
        check_patient_problem(clinical_state.hiporexia),
        check_patient_problem(clinical_state.salivacao),
        check_patient_problem(clinical_state.hiporexia),
        check_patient_problem(clinical_state.constipacao),
        check_patient_problem(clinical_state.chiado_no_peito),
        check_patient_problem(clinical_state.diminuicao_da_diurese),
        check_patient_problem(clinical_state.dor_abdominal),
        check_patient_problem(clinical_state.otalgia),
        check_patient_problem(clinical_state.epistaxe),
        check_patient_problem(clinical_state.otorreia),
        check_patient_problem(clinical_state.edema),
        check_patient_problem(clinical_state.adenomegalias),
        check_patient_problem(clinical_state.dor_articular),
        check_patient_problem(clinical_state.dificuldade_de_marcha),
        check_patient_problem(clinical_state.sonolencia),
        check_patient_problem(clinical_state.secrecao_ocular),
        check_patient_problem(clinical_state.dor_muscular),
        check_patient_problem(clinical_state.dor_retroorbitaria)
    ]]
    return patient
