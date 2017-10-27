# Arquivo: apps/users/urls.py
from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^home/admin/$', views.admin_view, name="admin"),
    url(r'^home/$', views.home_view, name="home"),
    url(r'^register/profile/$', views.sign_up_profile,
        name="register_profile"),
    url(r'^register/patient/$', views.sign_up_patient,
        name="register_patient"),
    url(r'^show/patient/(?P<cpf>\w+)/$', views.show_pacient_view,  # falta
        name="show_patient"),
    url(r'^home/receptionist/$',  views.registered_patient_view,
        name="home_receptionist"),
    url(r'^home/attendant/$', views.home_attendant_view,
        name="home_attendant"),
    url(r'^accounts/$', views.manage_accounts_view,
        name="manage_accounts"),
    url(r'^patients/$', views.manage_patients_view,
        name="manage_patients"),
    url(r'^accounts/edit/(?P<id_user>\w+)/$', views.edit_accounts_view,
        name="edit_accounts"),  # falta
    url(r'^accounts/remove/(?P<id_user>\w+)/$', views.staff_remove,
        name="staff_remove"),
    url(r'^patients/remove/(?P<cpf>\w+)/$', views.patient_remove,
        name="patient_remove"),  # falta
    url(r'^patients/edit/(?P<cpf>\d+)/$', views.edit_patient,
        name="edit_patient"),
    url(r'^registered/patient/$', views.registered_patient_view,
        name="registered_patient"),  # falta
    url(r'^registered/patient/(?P<cpf_patient>\w+)/$', views.queue_patient,
        name="queue_patient"),  # falta
    url(r'^classification/$', views.classification_view,
        name="classification")  # falta
]
