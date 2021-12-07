from django.contrib import admin
from .models import  *

# Register your models here.




admin.site.register(Departamento)
admin.site.register(Location)
admin.site.register(Reserva, ReservaAdmin)

admin.site.register(CheckIn)

