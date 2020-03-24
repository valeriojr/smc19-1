from django.urls import path

from . import views


app_name = 'monitoring'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('cadastrar/paciente', views.NewProfile.as_view(), name='new_profile'),
    path('cadastrar/atendimento', views.CadastrarAtendimento.as_view(), name='cadastrar_atendimento'),
]