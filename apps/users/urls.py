# Arquivo: apps/users/urls.py
from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.login_view, name="login"),
    url(r'^landing/page/$', views.landing_page, name="landing_page"),
    url(r'^home/$', views.home, name="home"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/user/$', views.sign_up_profile,
        name="register_user"),
    url(r'^register/patient/$', views.register_patient,
        name="register_patient"),
    url(r'^show/patient/(?P<cpf>\w+)/$', views.show_patient_view,  # falta
        name="show_patient"),
    url(r'^accounts/$', views.manage_accounts_view,
        name="manage_accounts"),
    url(r'^accounts/edit/(?P<id_user>\w+)/$', views.edit_accounts_view,
        name="edit_accounts"),  # falta
    url(r'^accounts/remove/(?P<id_user>\w+)/$', views.staff_remove,
        name="staff_remove"),
    url(r'^patients/remove/(?P<cpf>\w+)/$', views.patient_remove,
        name="patient_remove"),  # falta
    url(r'^patients/edit/(?P<cpf>\d+)/$', views.edit_patient,
        name="edit_patient"),
    url(r'^registered/patient/(?P<cpf_patient>\w+)/$', views.queue_patient,
        name="queue_patient"),  # falta
]
