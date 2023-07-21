from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=20)
    descrip = models.TextField(max_length=200)
    precio = models.FloatField()
    cantidad = models.CharField(max_length=10)
    perecedero = models.BooleanField()
