from django.shortcuts import render
from .models import Arriendo
from .forms import RegistroForm

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/login.html')

def registro(request):
    data = {
        'form' : RegistroForm()
    }

    if request.method =='POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "registro guardado"

        else:
            data["form"] = formulario

    return render(request, 'app/registro.html', data)

def arriendo(request):
    return render(request, 'app/arriendo.html')

def hotel(request):
    return render(request, 'app/hotel.html')

def tour(request):
    return render(request, 'app/tour.html')
