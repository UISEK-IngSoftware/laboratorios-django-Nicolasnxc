from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birthday = models.DateField(null=False) #Permie almacenar fechas
    level = models.IntegerField(default=1) #Permite almacenar numeros enteros, el default es el valor por defecto que se le asigna a ese campo

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {
        ("A", "Agua"),
        ("F", "Fuego"),
        ("T", "Tierra"),
        ("P", "Planta"),
        ("E", "Electrico"),
        ("L", "Lagartija"),
    }
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    wight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=2, max_digits=6)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True) #Permite establecer una relacion entre dos tablas, en este caso entre Pokemon y Trainer, el on_delete=models.CASCADE indica que si se elimina un entrenador, se eliminaran todos los pokemones asociados a ese entrenador
    picture = models.ImageField(upload_to="pokemon_images") #Permite almacenar imagenes, el upload_to indica la carpeta donde se almacenaran las imagenes, el null=True permite que el campo sea opcional, el blank=True permite que el campo sea opcional en los formularios

    def __str__(self):
        return self.name