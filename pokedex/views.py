from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import redirect, render
from pokedex.forms import PokemonForm
from pokedex.forms import TrainerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    pokemons = Pokemon.objects.all() #select * from pokedex_pokemon
    trainers = Trainer.objects.all() #select * from pokedex_trainer
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons, 'trainers': trainers }, request))

def pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id) #select * from pokedex_pokemon where id = id
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id) #select * from pokedex_pokemon where id = pokemon_id
    pokemon.delete() #delete from pokedex_pokemon where id = pokemon_id
    return redirect('pokedex:index')

def trainer(request, id: int):
    trainer = Trainer.objects.get(id=id) #select * from pokedex_trainer where id = trainer_id
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def edit_trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def delete_trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id) #select * from pokedex_trainer where id = trainer_id
    trainer.delete() #delete from pokedex_trainer where id = trainer_id
    return redirect('pokedex:index')

class CustomLoginView(LoginView):
    template_name = 'login_form.html'