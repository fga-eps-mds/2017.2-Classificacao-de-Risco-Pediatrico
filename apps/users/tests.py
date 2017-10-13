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

    def test_logout_view(self, client):
        # TODO: review this test:
        kwargs = {'email': 'email@gmail.com', 'password': '1234asdf'}
        is_logged = client.login(
            username=kwargs["email"],
            password=kwargs["password"])
        assert is_logged is False


    @pytest.mark.parametrize('url', ['/user/register/profile/',
                                    '/user/register/patient/',
                                    '/user/home/receptionist/',
                                    '/user/','/user/login/'])

    def test_get_route(self, client, url):
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.parametrize('url, template', [
        ('/user/register/profile/', 'users/registerProfile.html'),
        ('/user/register/patient/', 'users/registerPatient.html')])

    def test_sign_up_template(self, client, url, template):
        response = client.get(url)
        assert response.templates[0].name == template

    profile_data = ({
        'username':'usernameTest', 'password1':'password1Teste',
        'id_user':'idUserTest', 'uf':'ufTest','city':'cityTeste',
        'neighborhood':'neighborhoodTest', 'street':'streetTeste',
        'block':'blockTeste', 'number':'numberTest', 'email':'email@test.com',
        'profile':'1', 'name':'nameTest', 'password2':'password1Teste'})

    patient_data = ({
        'name':'nameTest', 'guardian':'guardianTeste',
        'cpf':'156498', 'parents_name':'parents_nameTest','uf':'ufTest',
        'city':'cityTeste', 'neighborhood':'neighborhoodTest', 'street':'streetTeste',
        'block':'blockTeste', 'number':'numberTest'})

    @pytest.mark.parametrize(' url, model, data', [
        ('/user/register/profile/',Staff, patient_data),
        ('/user/register/profile/', Staff,profile_data)])

    def test_sign_up_post(self, client, url, model, data):
        response = client.post(url, data)
        assert response.status_code == 302
        assert model.objects.count() == 1

    @pytest.mark.parametrize('url, form',[
        ('/user/register/profile/', RegistrationStaffForm),
        ('/user/register/patient/', RegistrationPatientForm)])

    def test_sign_up_has_form(self, client, url, form):
        response = client.get(url)
        assert 'form' in response.context
        assert response.context['form'] is not None
        assert isinstance(response.context['form'], form)

    @pytest.mark.parametrize('url, model, data',[
        ('/user/register/profile/', Staff, profile_data)
        ,
        # ('/user/register/profile/', Patient, patient_data)
        ])

    def test_sign_up_post(self, client, url, model, data):
        response = client.post(url, data)
        assert response.status_code == 302
        assert model.objects.count() == 1

    @pytest.mark.parametrize('url, data, urlredirect',[
        ('/user/register/profile/', profile_data, '/user/login/'),
        ('/user/register/profile/', patient_data, '/user/login/')])

    def test_sign_up_post_redirect(self, client, url, data, urlredirect):
        response = client.get(url, data, follow=True)
        assert response.status_code == 200
        assert response.redirect_chain == []
