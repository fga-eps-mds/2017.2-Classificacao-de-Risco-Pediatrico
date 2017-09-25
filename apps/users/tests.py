from django.test import TestCase
import pytest
# Create your tests here.

class TestUsers:

    def test_RegistrationAdminView(self, client):
        response = client.get('/user/register/admin/')
        assert response.status_code == 200

    def test_RegistrationAttendantView(self, client):
        response = client.get('/user/register/attendant/')
        assert response.status_code == 200
