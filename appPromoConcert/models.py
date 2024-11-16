from django.db import models

# Create your models here.

class PromotorMusical(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    def get_imagen_promotor(self):
        return f'img/promotores/{self.id}.png'
    
class Festival(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ubicacion = models.CharField(max_length=200)              #promotor.festivales.all()
    promotor = models.ForeignKey(PromotorMusical, on_delete=models.CASCADE, related_name='festivales')    

    def __str__(self):
        return self.nombre
    
    def get_imagen_festival(self):
        return f'img/festivales/{self.id}.png'
    
class Interprete(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=100)   #festival.interpretes.all()
    festivales = models.ManyToManyField(Festival, related_name='interpretes')

    def __str__(self):
        return self.nombre
    
    def get_imagen_interprete(self):
        return f'img/interpretes/{self.id}.png'