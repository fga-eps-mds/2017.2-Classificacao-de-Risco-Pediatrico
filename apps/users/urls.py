# Arquivo: apps/users/urls.py
from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.landing_page, name="landing_page"),
    url(r'^login$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^home/$', views.home, name="home"),
    url(r'^graphic/symptoms/under28d$', views.graphic_symptoms_view_28d,
        name="graphic_symptoms_28d"),
    url(r'^graphic/symptoms/29d2m$', views.graphic_symptoms_view_29d_2m,
        name="graphic_symptoms_29d_2m"),
    url(r'^graphic/symptoms/2m3y$', views.graphic_symptoms_view_2m_3y,
        name="graphic_symptoms_2m_3y"),
    url(r'^graphic/symptoms/3y10y$', views.graphic_symptoms_view_3y_10y,
        name="graphic_symptoms_3y_10y"),
    url(r'^graphic/symptoms/10ymore$', views.graphic_symptoms_view_10y_more,
        name="graphic_symptoms_10yMore"),
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
        name='classify_patient'),
    url(r'^feed_ml/$', views.feed_ml,
        name="feed_ml"),
    url(r'^my_history/$', views.my_history,
        name="my_history"),
    url(r'^classifications_chart/$', views.classifications_chart,
        name="classifications_chart"),
    url(r'^get/data/$', views.get_chart_data, name="get_data")
]
