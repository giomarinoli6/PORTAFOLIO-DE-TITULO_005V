from django.urls import path, include


from .views import  *

urlpatterns = [
    # paht de inicio ----------------------------------------------------------
    path('', home, name="home"),
    path('registro', registro_de_usuario, name='registro-usuario'),
    path('reserva/<id_depa>', reserva, name='reserva'),
    path('crear-reserva',crear_reserva, name='crear-reserva'),
    path('eliminar-reserva/<id>', eliminarReserva,name='eliminar-reserva'),
    path('departamentos', departamento, name='departamentos'),
    path('departamento/<id>', dep_individual,name='departamento'),
    path('historial', historial,name='historial'),
    
    path('checkin/<id>', checkIn,name='checkin'),

  
]

 