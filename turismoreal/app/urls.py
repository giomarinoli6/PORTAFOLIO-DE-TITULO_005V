from django.urls import path
from .views import  createDepa, home, login, registro, arriendodepa, hotel, reserva, tour ,createDepa

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('arriendo/', arriendodepa, name="arriendo"),
    path('hotel/', hotel, name="hotel"),
    path('tour/', tour, name="tour"),
    path('departamento/', createDepa, name="departamento"),
    path('reservar/<int:id>' , reserva, name="reserva"), 
]
