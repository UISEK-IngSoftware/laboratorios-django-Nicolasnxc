from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404 
from .models import Pokemon, Trainer
from pokedex.forms import PokemonForm

# Imports de Django REST Framework para tu API
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PokemonSerializer, TrainerSerializer

# IMPORTS PARA LA VISTA BASADA EN CLASES Y PROTECCIÓN
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required  # Para proteger las vistas
from django.urls import reverse_lazy

# ==========================================
# 1. VISTA DE INICIO (INDEX) - PROTEGIDA
# ==========================================
@login_required
def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    
    # Recorremos cada Pokémon para inventarle una descripción según su nombre
    for pokemon_obj in pokemons:
        nombre_minuscula = pokemon_obj.name.lower() if pokemon_obj.name else ""
        
        if "charmander" in nombre_minuscula:
            pokemon_obj.descripcion_inventada = "Prefiere las cosas calientes. Dicen que cuando llueve sale vapor de la punta de su cola."
        elif "pikachu" in nombre_minuscula:
            pokemon_obj.descripcion_inventada = "Mantiene la cola en alto para vigilar los alrededores. A veces le cae un rayo en esa misma postura."
        elif "squirtle" in nombre_minuscula:
            pokemon_obj.descripcion_inventada = "El caparazón de Squirtle no sirve solo para protegerlo. La forma redondeada y sus hendiduras reducen la resistencia al agua."
        elif "bulbasaur" in nombre_minuscula:
            pokemon_obj.descripcion_inventada = "Lleva una semilla en el lomo desde que nace. Esta va creciendo poco a poco a medida que el Pokémon se desarrolla."
        else:
            pokemon_obj.descripcion_inventada = "Un misterioso ejemplar registrado en la región. Su comportamiento y habilidades siguen bajo constante investigación."

    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'trainers': trainers
    }, request))

# ==========================================
# 2. VISTA PARA VER UN POKÉMON - PROTEGIDA
# ==========================================
@login_required
def pokemon(request, id: int):
    pokemon_obj = get_object_or_404(Pokemon, id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon_obj
    }
    return HttpResponse(template.render(context, request))

# ==========================================
# 3. VISTA PARA VER UN ENTRENADOR - PROTEGIDA
# ==========================================
@login_required
def trainer(request, id: int):
    trainer_obj = get_object_or_404(Trainer, id=id)
    
    # Obtenemos el nombre convirtiendo el objeto a string directamente
    nombre_entrenador = str(trainer_obj)
    
    # 1. Fecha de nacimiento totalmente inventada
    fecha_inventada = "15/05/1996"
        
    # 2. Asignamos fotos oficiales de entrenadores usando enlaces de internet según el texto del nombre
    nombre_minuscula = nombre_entrenador.lower()
    if "kukui" in nombre_minuscula:
        foto_link = "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/5/51/latest/20160602131830/Profesor_Kukui.png/230px-Profesor_Kukui.png"
    elif "oak" in nombre_minuscula:
        foto_link = "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/f/f8/latest/20180820010545/Profesor_Oak_LGPE.png/250px-Profesor_Oak_LGPE.png"
    else:
        # Enlace de una silueta de entrenador por defecto si es otro nombre
        foto_link = "https://images.wikidex.org/thumb/c/cd/latest/20160905221946/Silueta_de_entrenador_frenes%C3%AD_Sol_y_Luna.png/200px-Silueta_de_entrenador_frenes%C3%AD_Sol_y_Luna.png"

    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer_obj,
        'nombre_entrenador': nombre_entrenador,
        'fecha_nacimiento': fecha_inventada,
        'foto_link': foto_link
    }
    return HttpResponse(template.render(context, request))


# ==========================================
# VISTAS DE LA API (REST FRAMEWORK)
# ==========================================
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # GET público, lo demás protegido

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ==========================================
# 4. VISTA PARA EDITAR Y GUARDAR UN POKÉMON - PROTEGIDA
# ==========================================
@login_required
def edit_pokemon(request, id: int):
    # 1. Buscamos el Pokémon por su ID
    pokemon_obj = get_object_or_404(Pokemon, id=id)
    
    # 2. Traemos los entrenadores de la Base de Datos para que aparezcan en el select
    trainers_list = Trainer.objects.all()
    
    template = loader.get_template('pokemon_form.html')
    
    # Si el usuario procesa el formulario (da clic en Guardar)
    if request.method == 'POST':
        pokemon_obj.name = request.POST.get('name', pokemon_obj.name)
        pokemon_obj.type = request.POST.get('type', pokemon_obj.type)
        pokemon_obj.height = request.POST.get('height', pokemon_obj.height)
        
        # Enlazamos la relación con el entrenador seleccionado
        trainer_id = request.POST.get('trainer')
        if trainer_id:
            pokemon_obj.trainer = get_object_or_404(Trainer, id=trainer_id)
        else:
            pokemon_obj.trainer = None
            
        if request.FILES.get('picture'):
            pokemon_obj.picture = request.FILES.get('picture')
            
        pokemon_obj.save()
        return redirect('pokedex:index')
        
    # 3. Enviamos el contexto correcto a la plantilla
    context = {
        'pokemon': pokemon_obj,
        'trainers': trainers_list
    }
    return HttpResponse(template.render(context, request))

# ==========================================
# 5. VISTA PARA ELIMINAR UN POKÉMON - PROTEGIDA
# ==========================================
@login_required
def delete_pokemon(request, id: int):
    if request.method == 'POST':
        pokemon_obj = get_object_or_404(Pokemon, id=id)
        pokemon_obj.delete()
    return redirect('pokedex:index')

# ==========================================
# VISTA PARA AÑADIR UN NUEVO POKÉMON - PROTEGIDA
# ==========================================
@login_required
def add_pokemon(request):
    trainers_list = Trainer.objects.all()
    template = loader.get_template('add_pokemon.html')
    
    if request.method == 'POST':
        nuevo_pokemon = Pokemon()
        nuevo_pokemon.name = request.POST.get('name')
        nuevo_pokemon.type = request.POST.get('type')
        nuevo_pokemon.height = request.POST.get('height')
        
        trainer_id = request.POST.get('trainer')
        if trainer_id:
            nuevo_pokemon.trainer = get_object_or_404(Trainer, id=trainer_id)
            
        if request.FILES.get('picture'):
            nuevo_pokemon.picture = request.FILES.get('picture')
            
        nuevo_pokemon.save()
        return redirect('pokedex:index')
        
    context = {
        'trainers': trainers_list
    }
    return HttpResponse(template.render(context, request))

# ==========================================
# 6. VISTA DE LOGIN PERSONALIZADO
# ==========================================
class CustomLoginView(LoginView):
    template_name = 'login_form.html'  
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('pokedex:index')