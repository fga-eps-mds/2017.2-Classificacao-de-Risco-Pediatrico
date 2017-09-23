# Arquivo: apps/users/urls.py
from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/attendant/$', views.RegistrationAttendantView.as_view(), name="register_attendant"),
    url(r'^register/admin/$', views.RegistrationAdminView.as_view(success_url='logged_admin'), name="register_admin"),
    url(r'^register/patient/$', views.RegistrationPatientView.as_view(), name="register_patient"),
    url(r'^show/patient/(?P<cpf>\d+)/$', views.show_patient_view, name="show_patient_view"),
    url(r'^home/receptionist/$', views.home_receptionist_view, name="home_receptionist")

]
