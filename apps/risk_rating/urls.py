from django.conf.urls import url

from apps.users import views

app_name = 'risk_rating'
urlpatterns = [
    url(r'^', views.home, name="risk_rating")
]
