"""miproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("indice.urls")),
    path('admin/', admin.site.urls),# me traigo los urls de indice, asi solo en esta carpeta tengo las configuraciones
    #para que aparezca en la pag de mi poryecto debo traerme los urls de mis apps, tanto el de clase como el del indice
    path("clase/", include("clase.urls"))
]    

