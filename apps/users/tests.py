import pytest
from apps.users.models import Admin
# import apps.users.views
# from apps.users.views import RegistrationAdminView
# from factories import PatientFactory
# Create your tests here.


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

    def default_user_data(self):
        data = {
            'password': "1234asdf",
            'name': "testuser",
            'email': "email@gmail.com",
            'id_user': "1234"
        }
        return data

    def test_create_user(self):
        test_user = Admin.objects.create_user(**self.default_user_data())
        assert isinstance(test_user, Admin)

    def test_create_super_user(self):
        test_user = Admin.objects.create_superuser(**self.default_user_data())
        assert test_user.is_superuser
