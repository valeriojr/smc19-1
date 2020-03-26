from django.urls import path

from . import views


app_name = 'monitoring'
urlpatterns = [
    path('pacientes/', views.IndexProfile.as_view(), name='index_profile'),
    path('pacientes/cadastrar', views.CreateProfile.as_view(), name='create_profile'),
    path('pacientes/<int:pk>/', views.GetProfile.as_view(), name='get_profile'),
    path('pacientes/<int:pk>/editar', views.UpdateProfile.as_view(), name='edit_profile'),
    path('pacientes/<int:pk>/remover', views.DeleteProfile.as_view(), name='delete_profile'),
    path('pacientes/<int:profile>/enderecos/cadastrar', views.CreateAddress.as_view(), name='create_address'),
    path('pacientes/<int:profile>/enderecos/<int:pk>/remover', views.DeleteAddress.as_view(), name='delete_address'),
    path('pacientes/<int:profile>/enderecos/<int:pk>/editar', views.UpdateAddress.as_view(), name='update_address'),
    path('pacientes/<int:profile>/viagens/cadastrar', views.CreateTrip.as_view(), name='create_trip'),
    path('pacientes/<int:profile>/viagens/<int:pk>/remover', views.DeleteTrip.as_view(), name='delete_trip'),
    path('pacientes/<int:profile>/enderecos/<int:pk>/editar', views.UpdateTrip.as_view(), name='update_trip'),
    path('atendimento/cadastrar', views.CadastrarAtendimento.as_view(), name='cadastrar_atendimento'),
]