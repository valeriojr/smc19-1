from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'evolution'
urlpatterns = [
    path('', views.GraphEvolution.as_view(), name='graph_evolution'),
    path('data', views.DataGraphEvolution.as_view(), name='data_graph_evolution')
]
