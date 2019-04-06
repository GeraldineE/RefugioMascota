#Informacion de los animalitos que llegan al refugio
from django.db import models
from apps.adopcion.models import Persona

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Mascto(models.Model):
    folio = models.CharField(max_length=10,primary_key= True)
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    #creamos el atributo que sera nuestra llave foranea con el modelo Persona
    #creamos el atributo de vacuna 
    persona = models.ForeignKey(Persona, null=True, blank= True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna,blank=True)

