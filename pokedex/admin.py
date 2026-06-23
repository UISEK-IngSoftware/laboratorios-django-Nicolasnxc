from django.contrib import admin
from .models import Pokemon, Trainer

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass
# Register your models here.
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    pass