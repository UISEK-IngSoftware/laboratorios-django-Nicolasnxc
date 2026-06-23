<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# 1. Creamos el router de REST Framework
router = DefaultRouter()

# 2. Registramos las rutas para tus Pokémons y Entrenadores en la API
router.register(r'pokemons', views.PokemonViewSet)
router.register(r'trainers', views.TrainerViewSet)

urlpatterns = [
    # Tus rutas web clásicas (no las tocamos)
    path("", views.index, name="index"),
    path("<int:id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:id>/", views.trainer, name="trainer"),
    
    # Tu ruta de la API funcionando correctamente
    path('api/', include(router.urls)),
=======
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
>>>>>>> a5c6ce8190ac06cb3294de6115736b90d3855c9d
]