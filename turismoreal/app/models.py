from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.



# class Cliente(models.Model):
#     id_rut = models.CharField(primary_key=True, max_length=11, unique=True)  # This field type is a guess.
#     nombre = models.CharField(max_length=50 ,blank= False, null=False)  # This field type is a guess.
#     apellido = models.CharField(max_length=50 ,blank= False, null=False)  # This field type is a guess.
#     edad = models.IntegerField(blank= False, null=False)
#     sexo = models.CharField(max_length=9 ,blank= False, null=False)  # This field type is a guess.
#     correo = models.EmailField(max_length=50 ,blank= False, null=False)  # This field type is a guess.
#     telefono = models.IntegerField()
    

#     def __str__(self):
#         return self.nombre


opciones_consultas = [
    [0, "consultas"],
    [1, "reclamos"],
    [2, "sugerencias"],
    [3, "felicitaciones"],
    [4, "registrarme"]
]


class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_registro = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

class Location(models.Model):
    id = models.AutoField(primary_key=True, max_length=11, unique=True)
    region = models.CharField(max_length=50 ,blank= False, null=False)
    numero= models.CharField(max_length=10 ,blank= False, null=False)
    nombre = models.CharField(max_length=50)
    complemento =models.TextField(blank= False, null=False)
    
    def __str__(self):
        return self.region

class Departamento(models.Model): 
    id= models.AutoField(primary_key= True, unique=True)
    nombre = models.CharField(max_length=50 ,blank= False, null=False)
    descripcion = models.TextField(blank= False, null=False)
    precio = models.IntegerField(validators=[MaxValueValidator(9999999999)],blank= False, null=False)
    mantencion= models.CharField(max_length=50 ,blank= False, null=False)
    id_Location=models.ForeignKey(Location, on_delete=models.CASCADE,blank= False, null=False)
    

    class Meta:
        ordering =['nombre']
    
    def __str__(self):
        return self.nombre


# class pago(models.Model): 
#     id= models.AutoField(primary_key= True)
#     tipo = models.TextField(max_length=50)
#     monto_total = models.IntegerField(default=0)
#     fecha_pago = models.DateField('Fecha de pago',auto_now=True, auto_now_add=False)

#     class Meta:
#         ordering =['nombre']
    
#     def __str__(self):
#         return self.nombre