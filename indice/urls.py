from django.contrib import admin
from django.urls import path
from .views import numero_random, numero_del_usuario, plantilla,mi_plantilla #asi me traigo inicio la funcion de mi views

urlpatterns = [
  #  path('',inicio),#agregamos un camino a la vista que estamos haciendo
    #path('admin/', admin.site.urls),
    #path('',otra_vista),
    #path('numero-random/',numero_random),#asi la pagina me genera un numero random
    #path('dame-numero/<int:numero>',numero_del_usuario),#esto es para que la pagina me pida un numero con el <> le indico el argumento que va a ir en el link, en la direccion, observar que debe como argumento "numero" ya que este es el argumento que tiene la def que esta en este path
    path('mi-plantilla/', mi_plantilla, name = 'mi-plantilla'),
    path('', plantilla, name = 'plantilla')
  
    

#el primer argumento del path es para el camino que yo quiero que agarre, ese argumento que yo ponga ahi va a ser como la 'direccion' el codigo clave para que agarre ese camnino. si yo pongo /inicion/ al final del link va a l primer path, si dejo el link original va al ultimo path
]
