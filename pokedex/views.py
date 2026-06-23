from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PokemonSerializer, TrainerSerializer


def index(request):
    pokemons = Pokemon.objects.all() #Select * from pokedex_pokemon
    trainers = Trainer.objects.all() #Select * from pokedex_trainer
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'trainers': trainers
    }, request))

def pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id) #select * from pokedex_pokemon where id = id
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, id: int):
    trainer = Trainer.objects.get(id=id) #select * from pokedex_trainer where id = id
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # GET público, lo demás protegido

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]