from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'mathmodels'
urlpatterns = [
    path('', views.SirSeirMathModel.as_view(), name='sir_seir_math_model'),
]
