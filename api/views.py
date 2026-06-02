from rest_framework import serializers
from pokedex.models import Pokemon
from .serializers import PokemonSerializer
from rest_framework import viewsets

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer