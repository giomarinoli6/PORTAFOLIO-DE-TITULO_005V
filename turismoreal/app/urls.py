from django.urls import path
from .views import home, login, registro, arriendo, hotel, tour

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('arriendo/', arriendo, name="arriendo"),
    path('hotel/', hotel, name="hotel"),
    path('tour/', tour, name="tour"),
]