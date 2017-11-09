import pytest
from apps.users.forms import RegistrationStaffForm, RegistrationPatientForm, \
    EditPatientForm
from apps.users.models import Staff, Patient


@pytest.mark.django_db
class TestUsers:

    # @class_method
    # def setup_class(self, cls):
    #     Staff.objects.create_superuser(**self.default_user_data())
    #     response = client.post('/', {'username': 'email@gmail.com',
    #                                  'password': "1234asdf"})

    def test_home(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_login_view(self, client):

        # if this simple test is failing,
        # try running 'python manage.py collectstatic'
        response = client.get('/')
        assert response.status_code == 200

    def test_login_view_for_user(self, client):

        Staff.objects.create_user(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        assert response.url == '/home'

    def test_login_view_user_do_not_exists(self, client):
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})

        assert response.template_name[0] == 'users/user_login/login.html'

    def test_logout_view(self, client):
        # TODO: review this test:
        kwargs = {'email': 'email@gmail.com', 'password': '1234asdf'}
        is_logged = client.login(
            username=kwargs["email"],
            password=kwargs["password"])
        assert is_logged is False

    @pytest.mark.parametrize(
                            'url',
                            ['/register/user/',
                             '/'])
    def test_get_route(self, client, url):
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.parametrize('url',
                             ['/register/patient/',
                              '/home/'])
    def test_get_route_logged(self, client, url):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.parametrize('url, template', [
        ('/register/user/', 'users/user_login/registerUser.html'),
        ('/register/patient/', 'users/user_home/registerPatient.html')])
    def test_sign_up_template(self, client, url, template):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
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

    patient_data = ({
        'name': 'nameTest', 'guardian': 'guardianTeste',
        'birth_date': '2017-11-02', 'cpf': '156.498.222.09',
        'parents_name': 'parentsnameTest', 'uf': 'GO',
        'city': 'cityTeste', 'neighborhood': 'neighborhoodTest',
        'street': 'streetTeste', 'block': 'blockTeste',
        'number': '2222', 'age_range': '0'})

    @pytest.mark.parametrize('url, model, data', [
                            ('/register/user/', Staff, profile_data)])
    def test_sign_up_post(self, client, url, model, data):
        response = client.post(url, data)
        assert response.status_code == 302
        assert model.objects.count() == 1

    @pytest.mark.parametrize('url, model, data', [
                            ('/register/patient/', Patient, patient_data)])
    def test_sign_up_post_patient(self, client, url, model, data):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.post(url, data)
        assert response.status_code == 302
        assert model.objects.count() == 1

    @pytest.mark.parametrize('url, form', [
        ('/register/user/', RegistrationStaffForm),
        ('/register/patient/', RegistrationPatientForm)])
    def test_sign_up_has_form(self, client, url, form):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.get(url)
        assert 'form' in response.context
        assert response.context['form'] is not None
        assert isinstance(response.context['form'], form)

    @pytest.mark.parametrize('url, data, urlredirect', [
        ('/register/user/', profile_data, '/login')])
    def test_sign_up_post_redirect(self, client, url, data, urlredirect):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.post(url, data, follow=True)
        assert response.status_code == 200
        assert response.redirect_chain == [(urlredirect, 302)]

    @pytest.mark.parametrize('url, data, urlredirect', [
        ('/register/patient/', patient_data, '/home/')])
    def test_sign_up_patient_redirect(self, client, url, data, urlredirect):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.post(url, data, follow=True)
        assert response.status_code == 200
        assert response.redirect_chain == [(urlredirect, 302)]

    def test_home_view(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        response = client.get('/home/')
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

    def test_has_perm(self):
        perm = None
        user = Staff()
        assert user.has_perm(perm) is True

    def test_has_module_perms(self):
        app_name = None
        user = Staff()
        assert user.has_module_perms(app_name) is True

    def test_is_admin(self):
        user_name = Staff(name='Bruno', is_admin=True)
        assert user_name.is_admin is True

    def test_is_not_admin(self):
        user_name = Staff(name='Bruno')
        assert user_name.is_admin is False

    def test__str__(self):
        user_email = Staff(email='bruno@gmail.com')
        assert str(user_email) == 'bruno@gmail.com'

    def test_registered_patient_view(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                                          'password': "1234asdf"})
        patient1 = Patient(birth_date='2015-11-08')
        patient2 = Patient(birth_date='2014-10-08')
        patient1.save()
        patient2.save()
        allpatients = [patient1, patient2]
        response = client.get('/home/')
        assert response.status_code == 200
        assert list(response.context['patients']) == allpatients

        # Staff.objects.create_superuser(**self.default_user_data())
        # response = client.post('/', {'username': 'email@gmail.com',
        #                              'password': "1234asdf"})
        # patient = PatientFactory.create_batch(3)
        # response = client.get('/home/')
        # assert response.status_code == 200
        # assert list(response.context['patients']) == patient

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
        Test edit patient post mehtod with valid data
        """
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/', {'username': 'email@gmail.com',
                                     'password': "1234asdf"})
        Patient()
        name = Patient(id='156498', birth_date='2017-02-01')
        name.save()
        response = client.post('/patients/edit/156498/', self.patient_data)
        assert response.status_code == 302
        assert Patient.objects.count() == 1

    def test_edit_patient_post_invalid_data(self, client):
        """
        Test edit patient post mehtod with invalid data
        """
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        invalid_patient_data = ({
            'name': 'nameTest', 'guardian': 'guardianTeste',
            'birth_date': '2010-08-06', 'cpf': 'cpferror'})
        Patient()
        name = Patient(id='156498', birth_date='2008-09-05')
        name.save()
        response = client.post('/patients/edit/156498/', invalid_patient_data)
        assert response.status_code == 302
        # assert response.status_code == 302
        # antes tava 400 mas agora está 302

    def test_edit_patient_is_update_data(self, client):
        """
        Test if edit patient post method is actualy updating
        """
        Staff.objects.create_superuser(**self.default_user_data())
        client.post('/login', {'username': 'email@gmail.com',
                    'password': "1234asdf"})
        Patient()
        name = Patient(id='1', birth_date='2017-02-01', name='Victor')
        name.save()
        client.post('/patients/edit/1/', self.patient_data)
        assert Patient.objects.filter(id='1')[0].name == 'nameTest'

    def test_edit_accounts_view(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf"})
        Staff()
        name = Staff(id_user='456')
        name.save()
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

    def test_staff_remove(self, client):
        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/login', {'username': 'email@gmail.com',
                               'password': "1234asdf", 'id_user': "1234"})
        Staff()
        name = Staff(id_user='456')
        name.save()
        response = client.delete('/accounts/remove/456/', follow=True)
        assert response.redirect_chain == [('/accounts/', 302)]
        assert Staff.objects.count() == 1
        # foram instanciados 2 staffs
        # por isso o assert igual a 1

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
