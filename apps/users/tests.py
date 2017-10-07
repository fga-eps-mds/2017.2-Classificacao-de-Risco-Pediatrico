# from django.test import TestCase
import pytest
# from apps.users.models import UserManager
# import apps.users.views
# from apps.users.views import RegistrationAdminView
# from factories import PatientFactory
# Create your tests here.

from apps.users.models import Staff


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

    def test_user_get_full_name(self):
        name = "Carlinhos"
        user = Staff(name=name)

        assert user.get_full_name() == name

