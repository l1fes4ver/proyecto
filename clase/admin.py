from django.contrib import admin

from clase.models import Estudiante, Profesor

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Profesor)
