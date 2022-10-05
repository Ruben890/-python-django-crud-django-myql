from django.db import models


class Personas(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=25)
    cedula = models.CharField(max_length=11)
