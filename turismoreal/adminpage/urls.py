from django.urls import path, include
from .views import *



urlpatterns = [
    path('',inicio,name='admin-inicio'),
    path('locacion',crearLocation,name='crear-locacion'),
    path('editar-locacion/<id>/',modificarLocation,name='modificar-locacion'),
    path('eliminar-locacion/<id>/',eliminarLocation,name='eliminar-locacion'),

    path('departamento',crearDepartamento,name='departamento'),
    path('editar-departamento/<id>/',modificarDepartamento,name='modificar-departamento'),
    path('eliminar-departamento/<id>/',eliminarDepartamento,name='eliminar-departamento'),

    path('mantenedor-usuarios',mantenedorUsuarios,name='mantenedor-usuarios'),
    path('mantenedor-reservas',mantenedorReservas,name='mantenedor-reservas'),

    path('checkin/<id>', checkIn,name='checkin-admin'),
    path('checkout/<id>', checkOut,name='checkout-admin'),

    path('checkout-info/<id>', checkOutInfo,name='checkout-info'),
    path('checkin-info/<id>', checkInInfo,name='checkin-info'),
    
    
]

 