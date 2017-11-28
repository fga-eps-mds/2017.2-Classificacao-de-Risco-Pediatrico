# Arquivo: apps/users/urls.py
from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.landing_page, name="landing_page"),
    url(r'^login$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^home/$', views.home, name="home"),
    url(r'^register/user/$', views.sign_up_profile,
        name="register_user"),
    url(r'^register/patient/$', views.register_patient,
        name="register_patient"),
    url(r'^accounts/$', views.manage_accounts_view,
        name="manage_accounts"),
    url(r'^accounts/edit/(?P<id_user>\w+)/$', views.edit_accounts_view,
        name="edit_accounts"),
    url(r'^accounts/remove/(?P<id_user>\w+)/$', views.staff_remove,
        name="staff_remove"),
    url(r'^patients/remove/(?P<id>\w+)/$', views.patient_remove,
        name="patient_remove"),
    url(r'^patients/edit/(?P<id>\w+)/$', views.edit_patient,
        name="edit_patient"),
    url(r'^classify_patient/$', views.machine_learning,
        name='classify_patient')
]
