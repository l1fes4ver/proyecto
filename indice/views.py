##EN ESTA APP SECCIONO TODO EL BACKGROUND DE MI PROYECTO, aca voy a tener todo lo que son las views, el url ertc
from django.shortcuts import render

# Create your views here.
from re import template
from django.http import HttpResponse
import random
from django.template import loader



def otra_vista(request):
    return HttpResponse('''
                        <h1> Este es un titulo en h1</h1>
                        ''') #FORMATO HTTML, osea para que te aparezca en negrito

#ta clave el command + slash (te abre multiples pestanas)
def numero_random(request):
    numero = random.randrange(15,180)
    return HttpResponse(numero)

def numero_del_usuario(request,numero):
    numero = random.randrange(15,180)
    texto = f'<h1>Este es tu numero:{numero}</h1>'
    return HttpResponse(texto)




def plantilla(request):#para una view si o si le tenemos que pasar la 'request' como primer parametro
    dicc1 = {

    }
    return render(request, 'indice/index.html', dicc1)#esto es lo que YO quiero que aparezca en la pagina

 
#lista = [1,2,3,4,5,6,7,8,9]
#nombre = 'Jorgelina'
#apellido = 'Atahualpa'

#diccionario_de_datos = {
#    'nombre': nombre,
#    'apellido': apellido,
#    'nombre_largo' : len(nombre),

    #'nombre_largo': len(nombre),
#    'lista' : lista
#}

  # {% if len(nombre) < 5  %}
  #      <p style="color:red">{{nombre}}</p>##esto es para que el nombre tenga cierto color
  #      <p style="color:blue">{{apellido}}</p>
  # {% endif %}## en este lenguaje se le indica el finalizamiento del if
  # {{nombre}}{{plantilla}}

def mi_plantilla(request):#la carpeta que contiene mi plantilla
    dicc= {

   }
    #plantilla_preparada = template.render({dicc})
    #return HttpResponse(plantilla_preparada)
    return render(request, "indice/mi_plantilla.html", dicc)
