from django.urls import path

from . import views


app_name = 'smcovid19'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]