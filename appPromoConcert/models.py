from django.db import models

# Create your models here.

class PromotorMusical(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Festival(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ubicacion = models.CharField(max_length=200)                            #promotor.festivales.all()
    promotor = models.ForeignKey(PromotorMusical, on_delete=models.CASCADE, related_name='festivales')    

    def __str__(self):
        return self.nombre
    
class Interprete(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=100)   #festival.interpretes.all()
    festivales = models.ManyToManyField(Festival, related_name='interpretes')

    def __str__(self):
        return self.nombre