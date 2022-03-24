from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Curso# Create your views here.
import random

def nuevo_curso(request): # me creo una view para ir modificando mi base de datos de Clase, mi aplicacion
    camada = random.randrange(1500,3000)
    nuevo_curso = Curso (nombre='Curso 25', camada=camada)
    nuevo_curso.save()#me guardo los dos valores de los atrivutos de mi curso.
    return HttpResponse(f'se creo el curso {nuevo_curso.nombre} camada{nuevo_curso.camada}') 