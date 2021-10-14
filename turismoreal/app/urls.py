from django.urls import path
from .views import   actualizarDepartamento, actualizarLocation, crearLocation, editarDepartamento, editarLocation, eliminarDepartamento, eliminarLocation,home, login, registro, arriendodepa, reserva,createDepa, verLocation

urlpatterns = [
    # paht de inicio ----------------------------------------------------------
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('arriendo/', arriendodepa, name="arriendo"),
    # endpaht de inicio 

    #---------------------------------------------------------------------------
    # paht de location
    path('crudLocation/' , crearLocation, name="crudLocation"),
    path('editarLocation/<int:id>' , editarLocation, name="editarLocation"),
    path('actualizarLocation/<int:id>',actualizarLocation,name="actualizarLocation"),
    path('eliminarLocation/<int:id>',eliminarLocation,name="eliminarLocation"),
    path('verLocation/' ,verLocation , name="verLocation"), 
    # endpath de location
    # ---------------------------------------------------------------------------
    # path de departamento
    path('ingresarDepartamento/', createDepa, name="ingresarDepartamento"),
    path('editarDepartamento/<int:id>', editarDepartamento, name="editarDepartamento"),
    path('actualizarDepartamento/<int:id>', actualizarDepartamento, name="actualizarDepartamento"),
    path('eliminarDepartamento/<int:id>',eliminarDepartamento,name="eliminarDepartamento"),
    path('reservar/<int:id>' , reserva, name="reserva"),
    # end path de departamento
]

 