import pytest
from apps.users.apps import UsersConfig
from apps.users.forms import RegistrationStaffForm, RegistrationPatientForm, \
    EditPatientForm
from apps.users.models import Staff, Patient
from apps.risk_rating.models import MachineLearning_28d, \
    MachineLearning_29d_2m, MachineLearning_2m_3y, \
    MachineLearning_3y_10y, MachineLearning_10yMore
from apps.risk_rating.models import ClinicalState_28d, \
    ClinicalState_29d_2m, ClinicalState_2m_3y, \
    ClinicalState_3y_10y, ClinicalState_10yMore


@pytest.mark.django_db
class TestUsersViews:

    def test_login_view_for_user(self, client):

        Staff.objects.create_user(**self.default_user_data())

        user_login_data = {
            'username': 'email@gmail.com',
            'password': "1234asdf"
        }
        response = client.post('/login', user_login_data)

        assert response.url == '/home'

    def test_login_view_user_do_not_exists(self, client):
        user_login_data = {
            'username': 'email@gmail.com',
            'password': "1234asdf"
        }
        response = client.post('/login', user_login_data)

        assert response.template_name[0] == 'users/user_login/login.html'

    @pytest.mark.parametrize('url', [
        '/register/user/',
        '/'
    ])
    def test_get_route(self, client, url):
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.parametrize('url',
                             ['/register/patient/',
                              '/home/'])
    def test_get_route_logged(self, client, url):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.parametrize('url, template', [
        ('/register/user/', 'users/user_login/registerUser.html'),
        ('/register/patient/', 'users/user_home/registerPatient.html')])
    def test_sign_up_template(self, client, url, template):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.get(url)
        assert response.templates[0].name == template

    profile_data = ({
        'username': 'usernameTest', 'password1': 'password1Teste',
        'id_user': 'idUserTest', 'uf': 'DF', 'city': 'cityTeste',
        'neighborhood': 'neighborhoodTest', 'street': 'streetTeste',
        'block': 'blockTeste', 'number': 'numberTest',
        'email': 'email@test.com', 'profile': '1', 'name': 'nameTest',
        'password2': 'password1Teste'})

    patient_data = ({'birth_date': '2017-11-02'})

    def test_sign_up_post_patient(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        response = client.post('/register/patient/', {'age_range': '1'})
        assert response.url == '/home/'

    @pytest.mark.parametrize('url, form', [
        ('/register/user/', RegistrationStaffForm),
        ('/register/patient/', RegistrationPatientForm)])
    def test_sign_up_has_form(self, client, url, form):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.get(url)
        assert 'form' in response.context
        assert response.context['form'] is not None
        assert isinstance(response.context['form'], form)

    @pytest.mark.parametrize('url, data, url_redirect_to', [
        ('/register/user/', profile_data, '/login')
    ])
    def test_sign_up_post_redirect(self, client, url, data, url_redirect_to):
        response = client.post(url, data, follow=True)

        assert response.status_code == 200
        assert response.redirect_chain == [(url_redirect_to, 302)]
        assert Staff.objects.count() == 1

    @pytest.mark.parametrize('url',
                             ['/graphic/symptoms/under28d',
                              '/graphic/symptoms/29d2m',
                              '/graphic/symptoms/2m3y',
                              '/graphic/symptoms/3y10y',
                              '/graphic/symptoms/10ymore'])
    def test_graphic_symptoms_view(self, client, url):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.get(url)
        assert response.status_code == 200

    def default_user_data(self):
        data = {
            'password': "1234asdf",
            'name': "testuser",
            'email': "email@gmail.com",
            'id_user': "1234",
            'profile': "1"
        }
        return data

    def test_registered_patient_view(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                                          'password': "1234asdf"})
        patient1 = Patient(birth_date='2015-11-08')
        patient2 = Patient(birth_date='2014-10-08')
        patient1.save()
        patient2.save()
        all_patients = [patient1, patient2]
        response = client.get('/home/')
        assert response.status_code == 200
        assert list(response.context['patients']) == all_patients

    def test_register_patient_valid_form(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.post('/register/patient/', {'age_range': '1'})
        assert Patient.objects.last().age_range == 1
        # 302 as a status code means redirection
        assert response.status_code == 302

    def test_edit_patient_form(self, client):
        """
        Test edit patient form with a valid cpf
        """
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                                          'password': "1234asdf"})
        name = Patient(id='001002012', birth_date='2017-02-01')
        name.save()
        response = client.get('/patients/edit/001002012/')
        assert 'form' in response.context
        assert 'patient' in response.context
        assert response.context['form'] is not None
        assert isinstance(response.context['form'], EditPatientForm)

    def test_edit_patient_invalid_cpf(self, client):
        """
        Test edit patient form with a invalid cpf
        """
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        with pytest.raises(IndexError):
            client.get('/patients/edit/007/')

    def test_edit_patient_post_valid_data(self, client):
        """
        Test edit patient post method with valid data
        """
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/', {'username': 'email@gmail.com',
                          'password': "1234asdf"})

        Patient(id='156498', birth_date='2017-02-01').save()

        response = client.post('/patients/edit/156498/', self.patient_data)
        assert response.status_code == 302
        assert Patient.objects.count() == 1

    def test_edit_patient_post_invalid_data(self, client):
        """
        Test edit patient post method with invalid data
        """
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        invalid_patient_data = ({
            'name': 'nameTest', 'guardian': 'guardianTeste',
            'birth_date': '2010-08-06', 'cpf': 'cpferror'
        })

        Patient(id='156498', birth_date='2008-09-05', age_range='0').save()
        response = client.post('/patients/edit/156498/', invalid_patient_data)
        assert response.status_code == 400

    def test_edit_patient_is_update_data(self, client):
        """
        Test if edit patient post method is actually updating
        """
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        Patient(id='1', birth_date='2017-02-01', name='Victor').save()
        client.post('/patients/edit/1/', self.patient_data)
        assert Patient.objects.filter(id='1')[0].name == 'Victor'

    def test_edit_accounts_view(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        Staff(id_user='456').save()
        response = client.get('/accounts/edit/456/')
        assert response.status_code == 200

    def test_manage_accounts_view(self, client):
        stafflogin = Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                                          'password': "1234asdf"})
        staff1 = Staff(id_user='456')
        staff1.save()
        allstaff = [stafflogin, staff1]
        response = client.get('/accounts/')
        assert response.status_code == 200
        assert list(response.context['staffs']) == allstaff

    @pytest.mark.parametrize(
        'data_type, url', [(Patient, '/home/'), (Staff, '/accounts/')])
    def test_remove_object(self, client, data_type, url):
        """Test remove object."""
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                                          'password': "1234asdf",
                                          'id_user': "1234"})
        data_type()

        if data_type == Staff:
            name = data_type(id_user='456')
            method = '/accounts/remove/456/'
        else:
            name = data_type(id='125987', birth_date='2016-11-03')
            method = '/patients/remove/125987/'

        name.save()
        response = client.delete(method, follow=True)
        assert response.redirect_chain == [(url, 302)]
        assert Patient.objects.count() == 0

    @pytest.mark.parametrize('url, urlredirect', [
        ('/register/patient', '/login'),
        ('/home', '/login'),
        ('/accounts', '/login')])
    def test_unauthorized_status_code(self, client, url, urlredirect):
        response = client.get(url, follow=True)
        last_url, status_code = response.redirect_chain[-1]
        assert response.status_code == 200
        assert last_url == urlredirect

    def test_valid_age_range_1(self, client):
        """
        Test if age_range is updating
        """
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/', {'username': 'email@gmail.com',
                          'password': "1234asdf"})
        Patient()
        name = Patient(id='156498', birth_date='2016-11-03')
        name.save()
        form = RegistrationPatientForm()
        client.post('/register/patient', self.patient_data)
        if form.is_valid():
            assert form.cleaned_data.get['age_range'] == 1

    def test_home_patient_list(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                                          'password': "1234asdf"})
        Patient()
        patient_test = Patient(id='156498', birth_date='2016-11-03')
        patient_test.save()

        response = client.get('/home/')
        assert response.status_code == 200
        assert set(list(response.context['patients'])) == \
            set(list(Patient.objects.all()))

    form1data = ({'patient': '1', 'form1': ''})
    form2data = ({'patient': '2', 'form2': ''})
    form3data = ({'patient': '3', 'form3': ''})
    form4data = ({'patient': '4', 'form4': ''})
    form5data = ({'patient': '5', 'form5': ''})
    formdatas = [form1data, form2data, form3data, form4data, form5data]

    def generate_all_age_patients(self):
        """
            generating one test patient for each age range
        """

        # Patient()
        for x in range(1, 6):
            patient = Patient(id=x, age_range=x)
            patient.save()

    def test_rate_patient(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        self.generate_all_age_patients()

        # the loop below posts the symptoms form for every one of the
        # 5 fictional patients
        classifications = []
        for index, formdata in enumerate(self.formdatas):
            response = client.post('/classify_patient/', formdata)
            import json
            data = json.loads(response.content.decode("utf-8"))
            classifications.append(data["classification"])

        # making sure that no classification is "Não classificado"
        assert "Não classificado" not in classifications

    form1_ml = ({'classification': 1, 'form1_ml': ''})
    form2_ml = ({'classification': 2, 'form2_ml': ''})
    form3_ml = ({'classification': 3, 'form3_ml': ''})
    form4_ml = ({'classification': 1, 'form4_ml': ''})
    form5_ml = ({'classification': 2, 'form5_ml': ''})
    forms_ml = [form1_ml, form2_ml, form3_ml, form4_ml, form5_ml]

    def test_feed_ml_page(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        response = client.get('/feed_ml/')
        assert response.status_code == 200

    def test_feed_ml(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        # this loop will post every classification form into 'feed ml'
        for index, forms_ml in enumerate(self.forms_ml):
            client.post('/feed_ml/', forms_ml)

        # the asserts below make sure that there is one classification
        # for each age range saved now.
        assert MachineLearning_28d.objects.count() == 1
        assert MachineLearning_29d_2m.objects.count() == 1
        assert MachineLearning_2m_3y.objects.count() == 1
        assert MachineLearning_3y_10y.objects.count() == 1
        assert MachineLearning_10yMore.objects.count() == 1

    def test_my_history_view(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                                          'password': "1234asdf"})
        response = client.get('/my_history/')
        assert response.status_code == 200

    def test_edit_patient_is_valid(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        Patient()
        patient_test = Patient(id='1', birth_date='2017-10-10', age_range='0')
        patient_test.save()

        client.post('/patients/edit/1/', {'name': 'New Name',
                                          'age_range': '1'})
        edited_patient = Patient.objects.get(id=1)

        assert edited_patient.name == 'New Name'
        assert edited_patient.age_range == 1

    def test_classifications_chart(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        response = client.get('/classifications_chart/')
        assert response.status_code == 200

    def test_classifications_chart_filter(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        response = client.post('/classifications_chart/', {'month': 12,
                                                           'year': 2017})

        assert response.status_code == 200

    def create_clinical_states(self):
        Patient(id='156498', birth_date='2016-11-03').save()
        clinical_28 = ClinicalState_28d(patient_id='156498')
        clinical_29 = ClinicalState_29d_2m(patient_id='156498')
        clinical_2m = ClinicalState_2m_3y(patient_id='156498')
        clinical_3y = ClinicalState_3y_10y(patient_id='156498')
        clinical_10y = ClinicalState_10yMore(patient_id='156498')
        clinical_28.save()
        clinical_29.save()
        clinical_2m.save()
        clinical_3y.save()
        clinical_10y.save()

    def test_graphic_symptoms_view_28d(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        self.create_clinical_states()

        response_28 = client.post('/graphic/symptoms/under28d', {'month': 12})
        response_29 = client.post('/graphic/symptoms/29d2m', {'month': 12})
        response_2m = client.post('/graphic/symptoms/2m3y', {'month': 12})
        response_3y = client.post('/graphic/symptoms/3y10y', {'month': 12})
        response_10y = client.post('/graphic/symptoms/10ymore', {'month': 12})
        assert response_28.status_code == 200
        assert response_29.status_code == 200
        assert response_2m.status_code == 200
        assert response_3y.status_code == 200
        assert response_10y.status_code == 200


@pytest.mark.django_db
class TestStaffModel:

    def default_user_data(self):
        data = {
            'password': "1234asdf",
            'name': "testuser",
            'email': "email@gmail.com",
            'id_user': "1234",
            'profile': "1"
        }
        return data

    def test_create_user(self):
        test_user = Staff.objects.create_user(**self.default_user_data())
        assert isinstance(test_user, Staff)

    def test_create_super_user(self):
        test_user = Staff.objects.create_superuser(**self.default_user_data())
        assert test_user.is_admin

    def test_user_get_full_name(self):
        name = "Carlinhos Cabral"
        user = Staff(name=name)
        assert user.get_full_name() == name

    def test_get_short_name(self):
        name = "Carlinhos"
        user = Staff(name=name)
        assert user.get_short_name() == name

    def test_create_user_without_email(self):
        user_data = self.default_user_data()
        del user_data['email']

        with pytest.raises(KeyError) as value_err:
            Staff.objects.create_user(**user_data)

        assert 'email' in str(value_err.value)

    def test_has_perm(self):
        perm = None
        app_name = None
        user = Staff()
        assert user.has_perm(perm) is True
        assert user.has_module_perms(app_name) is True

    def test_is_staff_pass(self):
        test_user = Staff.objects.create_superuser(**self.default_user_data())
        assert test_user.is_staff is True

    def test_is_staff_fail(self):
        test_user = Staff.objects.create_user(**self.default_user_data())
        assert test_user.is_staff is False

    def test__str__(self):
        user_email = Staff(email='bruno@gmail.com')
        assert str(user_email) == 'bruno@gmail.com'


@pytest.mark.django_db
class TestPatientModel:

    @pytest.mark.parametrize('age_range, expected_text', [
        ('0', 'Faixa etária indefinida'),
        ('1', '0 até 28 dias'),
        ('2', '29 dias à 2 meses'),
        ('3', '2 meses à 3 anos'),
        ('4', '3 anos à 10 anos'),
        ('5', 'Acima de 10 anos')
    ])
    def test_age_range_verbose(self, age_range, expected_text):
        patient = Patient(age_range=int(age_range))
        assert patient.age_range_verbose() == expected_text

    def test_gender_verbose(self):
        patient = Patient(age_range=1, gender=1)
        assert patient.gender_verbose() == 'Feminino'


class TestUserApp:

    def test_app(self):
        assert UsersConfig.name == 'users'
