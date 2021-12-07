from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib import admin
import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.




opciones_consultas = [
    [0, "consultas"],
    [1, "reclamos"],
    [2, "sugerencias"],
    [3, "felicitaciones"],
    [4, "registrarme"]
]


class Location(models.Model):

    region = models.CharField(max_length=50 ,blank= False, null=False)
    numero= models.CharField(max_length=10 ,blank= False, null=False)
    
    
    def __str__(self):
        return self.region

class Departamento(models.Model): 

    nombre = models.CharField(max_length=50 ,blank= False, null=False)
    descripcion = models.TextField(blank= False, null=False)
    n_cuartos=precio = models.IntegerField(blank= True, null=True)
    precio = models.IntegerField(blank= False, null=False)
    mantencion= models.CharField(max_length=50 ,blank= False, null=False)
    id_Location=models.ForeignKey(Location, on_delete=models.CASCADE,blank= False, null=False)

    imagen=models.ImageField( upload_to='departamento', null=True)
    

    class Meta:
        ordering =['nombre']
    
    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    fecha_creacion=models.DateField( auto_now=False, auto_now_add=True)
    fecha_inicio=models.DateTimeField( auto_now=False, auto_now_add=False)
    n_dias=models.IntegerField()
    id_usuario=models.ForeignKey(User,  on_delete=models.CASCADE, related_name="reservas")
    id_departamento=models.ForeignKey(Departamento,  on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

    def get_total(self):

        total=self.n_dias * self.id_departamento.precio
        return total

    def get_final_date(self):
        final_date=self.fecha_inicio+datetime.timedelta(days=self.n_dias)
        return final_date

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicio','id_usuario')

METODOS_DE_PAGO=(
    ('1','EFECTIVO'),
    ('2','DEBITO'),
    ('3','CREDITO')
    )

class CheckIn(models.Model):
    fecha_creacion=models.DateField( auto_now=False, auto_now_add=True,blank=True, null=True)
    reserva= models.OneToOneField(Reserva, on_delete=models.CASCADE , related_name="checkin")
    n_personas=models.IntegerField()
    tipo_pago= models.CharField(max_length=150,choices=METODOS_DE_PAGO,blank=True, null=True)


REPARO=(
    ('0','NINGUNO'),
    ('1','LEVES'),
    ('3','GRAVES'),
    ('5','GRAVISIMOS')
    )

class CheckOut(models.Model):
    fecha_creacion=models.DateField( auto_now=False, auto_now_add=True)
    fecha_modificacion=models.DateField( auto_now=True, auto_now_add=False)
    reserva= models.OneToOneField(Reserva, on_delete=models.CASCADE , related_name="checkout")
    reparos=models.CharField(max_length=150,choices=REPARO,blank=True, null=True)

    def get_total_reparo(self):

        total=int(self.reparos) * self.reserva.id_departamento.precio
        return total
