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
]