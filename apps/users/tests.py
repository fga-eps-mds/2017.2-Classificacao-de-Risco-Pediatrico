import pytest
# import apps.users.views
# from apps.users.views import RegistrationAdminView
# from factories import PatientFactory
# Create your tests here.

from apps.users.forms import RegistrationStaffForm, RegistrationPatientForm
from apps.users.models import Staff, Patient


@pytest.mark.django_db
class TestUsers:

    def test_home(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_login_view(self, client):

        # if this simple test is failing,
        # try running 'python manage.py collectstatic'
        response = client.get('/')
        assert response.status_code == 200

    def test_login_view_for_admin(self, client):

        Staff.objects.create_superuser(**self.default_user_data())
        response = client.post('/', {'username': 'email@gmail.com',
                                     'password': "1234asdf"})

        assert response.url == '/home/admin'

    def test_login_view_for_receptionist(self, client):

        Staff.objects.create_user(**self.default_user_data())
        response = client.post('/', {'username': 'email@gmail.com',
                                     'password': "1234asdf"})

        assert response.url == '/home/receptionist/'

    def test_login_view_for_attendant(self, client):

        user_data = self.default_user_data()
        user_data['profile'] = '2'

        Staff.objects.create_user(**user_data)
        response = client.post('/', {'username': 'email@gmail.com',
                                     'password': "1234asdf"})

        assert response.url == '/risk_rating'

    def test_login_view_user_do_not_exists(self, client):
        response = client.post('/', {'username': 'email@gmail.com',
                                     'password': "1234asdf"})

        assert response.template_name[0] == 'users/login.html'

    def test_logout_view(self, client):
        # TODO: review this test:
        kwargs = {'email': 'email@gmail.com', 'password': '1234asdf'}
        is_logged = client.login(
            username=kwargs["email"],
            password=kwargs["password"])
        assert is_logged is False

    @pytest.mark.parametrize(
                            'url',
                            ['/register/profile/',
                                '/register/patient/',
                                '/home/receptionist/', '/'])
    def test_get_route(self, client, url):
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.parametrize('url, template', [
        ('/register/profile/', 'users/registerProfile.html'),
        ('/register/patient/', 'users/registerPatient.html')])
    def test_sign_up_template(self, client, url, template):
        response = client.get(url)
        assert response.templates[0].name == template

    profile_data = ({
        'username': 'usernameTest', 'password1': 'password1Teste',
        'id_user': 'idUserTest', 'uf': 'ufTest', 'city': 'cityTeste',
        'neighborhood': 'neighborhoodTest', 'street': 'streetTeste',
        'block': 'blockTeste', 'number': 'numberTest',
        'email': 'email@test.com', 'profile': '1', 'name': 'nameTest',
        'password2': 'password1Teste'})

    patient_data = ({
        'name': 'nameTest', 'guardian': 'guardianTeste',
        'birth_date': '12/2/12', 'cpf': '156498',
        'parents_name': 'parents_nameTest', 'uf': 'ufTest',
        'city': 'cityTeste', 'neighborhood': 'neighborhoodTest',
        'street': 'streetTeste', 'block': 'blockTeste',
        'number': 'numberTest', 'isInQueue': 'True',
        'queuePosition': '5'})

    @pytest.mark.parametrize('url, model, data', [
        ('/register/patient/', Patient, patient_data),
        ('/register/profile/', Staff, profile_data)])
    def test_sign_up_post(self, client, url, model, data):
        response = client.post(url, data)
        assert response.status_code == 302
        assert model.objects.count() == 1

    @pytest.mark.parametrize('url, form', [
        ('/register/profile/', RegistrationStaffForm),
        ('/register/patient/', RegistrationPatientForm)])
    def test_sign_up_has_form(self, client, url, form):
        response = client.get(url)
        assert 'form' in response.context
        assert response.context['form'] is not None
        assert isinstance(response.context['form'], form)

    @pytest.mark.parametrize('url, data, urlredirect', [
        ('/register/profile/', profile_data, '/'),
        ('/register/patient/', patient_data, '/queue/patient/')])
    def test_sign_up_post_redirect(self, client, url, data, urlredirect):
        response = client.post(url, data, follow=True)
        assert response.status_code == 200
        assert response.redirect_chain == [(urlredirect, 302)]

    def test_home_receptionist_view(self, client):
        response = client.get('/home/receptionist/')
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
