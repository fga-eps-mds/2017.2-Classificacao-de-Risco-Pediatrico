# from django.test import TestCase
import pytest
# from apps.users.models import UserManager
# import apps.users.views
# from apps.users.views import RegistrationAdminView
# from factories import PatientFactory
# Create your tests here.

from apps.users.forms import RegistrationStaffForm, RegistrationPatientForm
from apps.users.models import Staff, Patient


@pytest.mark.django_db
class TestUsers:

    def test_home(self, client):
        response = client.get('/user/')
        assert response.status_code == 200

    def test_login_view(self, client):

        # if this simple test is failing,
        # try running 'python manage.py collectstatic'
        response = client.get('/user/login/')
        assert response.status_code == 200

    def test_logout_view(self, client):
        # TODO: review this test:
        kwargs = {'email': 'email@gmail.com', 'password': '1234asdf'}
        is_logged = client.login(
            username=kwargs["email"],
            password=kwargs["password"])
        assert is_logged is False

    def test_home_receptionist_view(self, client):
        response = client.get('/user/home/receptionist/')
        assert response.status_code == 200

    def test_sign_up_profile(self, profile_fixture):
        assert profile_fixture.status_code == 200

    def test_sign_up_profile_template(self, profile_fixture):
        assert profile_fixture.templates[0].name == "users/registerProfile.html"

    def test_sign_up_profile_has_form(self, profile_fixture):
        assert 'form' in profile_fixture.context
        assert profile_fixture.context['form'] is not None
        assert isinstance(profile_fixture.context['form'], RegistrationStaffForm)

    def test_sign_up_profile_post(self, client, profile_data):
        response = client.post('/user/register/profile/', profile_data)
        assert response.status_code == 302
        assert Staff.objects.count() == 1

    def test_sign_up_profile_post_redirect(self, client, profile_data):
        response = client.post('/user/register/profile/', profile_data,
                               follow=True)
        assert response.status_code == 200
        assert response.redirect_chain == [('/user/login/', 302)]


#Patient views test
    def test_sign_up_patient(self, patient_fixture):
        assert patient_fixture.status_code == 200

    def test_sign_up_patient_template(self, patient_fixture):
        assert patient_fixture.templates[0].name == "users/registerPatient.html"

    def test_sign_up_patient_has_form(self, patient_fixture):
        assert 'form' in patient_fixture.context
        assert patient_fixture.context['form'] is not None
        assert isinstance(patient_fixture.context['form'],  RegistrationPatientForm)

    def test_sign_up_patient_post(self, client, patient_data):
        response = client.post('/user/register/profile/', patient_data)
        assert response.status_code == 302
        assert Staff.objects.count() == 1

    def test_sign_up_patient_post_redirect(self, client, patient_data):
        response = client.post('/user/register/profile/', patient_data,
                                follow=True)
        assert response.status_code == 200
        assert response.redirect_chain == [('/user/login/', 302)]

    @pytest.fixture
    def profile_fixture(self, client):
        return client.get('/user/register/profile/')

    @pytest.fixture
    def profile_data(self, client):
        return ({'username':'usernameTest', 'password1':'password1Teste',
                'id_user':'idUserTest', 'uf':'ufTest','city':'cityTeste',
                'neighborhood':'neighborhoodTest', 'street':'streetTeste',
                'block':'blockTeste', 'number':'numberTest', 'email':'email@test.com',
                'profile':'1', 'name':'nameTest', 'password2':'password1Teste'})

    @pytest.fixture
    def patient_fixture(self, client):
        return client.get('/user/register/patient/')

    @pytest.fixture
    def patient_data(self, client):
        return ({'username':'usernameTest', 'password1':'password1Teste',
                'id_user':'idUserTest', 'uf':'ufTest','city':'cityTeste',
                'neighborhood':'neighborhoodTest', 'street':'streetTeste',
                'block':'blockTeste', 'number':'numberTest', 'email':'email@test.com',
                'profile':'1', 'name':'nameTest', 'password2':'password1Teste'})
