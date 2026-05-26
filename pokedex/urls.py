from django.urls import path
from django.contrib.auth.views import LogoutView # <-- IMPORTANTE IMPORTAR ESTO
from . import views

app_name = 'pokedex'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    
    # ESTA LÍNEA ES LA QUE TE FALTA PARA EVITAR EL ERROR:
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('pokemon/<int:id>/', views.pokemon, name='pokemon'),
    path('Trainer/<int:id>/', views.trainer, name='Trainer'),
    path('edit_pokemon/<int:id>/', views.edit_pokemon, name='edit_pokemon'),
    path('delete_pokemon/<int:id>/', views.delete_pokemon, name='delete_pokemon'),
    path('add_pokemon/', views.add_pokemon, name='add_pokemon'),
]