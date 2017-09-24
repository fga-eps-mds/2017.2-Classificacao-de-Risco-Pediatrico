# from django.test import TestCase
import pytest
# Create your tests here.


@pytest.mark.django_db
class TestUsers:
    def test_login_view(self, client):

        # if this simple test is failing,
        # try running 'python manage.py collectstatic'
        response = client.get('/user/login/')
        assert response.status_code == 200
