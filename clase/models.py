from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)#estos son parametros genericos dentro de los modelos y se definen siempre de esta manera
    apellido = models.CharField(max_length=30)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=20)


class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_de_entrega = models.DateTimeField(max_length=30)
    entregadp = models.BooleanField()


class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()