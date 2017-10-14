# Arquivo: apps/users/urls.py
from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^login/admin$', views.admin_view, name="admin"),
    url(r'^register/profile/$', views.RegistrationStaffView.as_view(),
        name="register_profile"),
    url(r'^register/patient/$', views.RegistrationPatientView.as_view(),
        name="register_patient"),
    url(r'^show/patient/(?P<cpf>\d+)/$', views.show_pacient_view,
        name="show_patient"),
    url(r'^home/receptionist/$', views.home_receptionist_view,
        name="home_receptionist"),
    url(r'^home/attendant/$', views.home_attendant_view,
        name="home_attendant")
]
