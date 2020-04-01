from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'prediction'
urlpatterns = [
    path('', views.HealthCenterStatusCreate.as_view(), name='prediction_hub'),
]
