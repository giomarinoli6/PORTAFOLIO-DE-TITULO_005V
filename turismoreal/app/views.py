from django.shortcuts import render, redirect 
from .models import Arriendo, Departamento
from .forms import RegistroForm ,departamentoForm

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

def reserva(request, id):
    departamento = Departamento.objects.get(id=id)
    return render(request, 'app/reservar.html', {'departamento':departamento})

def arriendodepa(request):
    departamentos = Departamento.objects.all()

    return render(request, "app/arriendo.html",{'departamentos': departamentos})

  
# Create your views here.  
def createDepa(request):  
    if request.method == "POST":  
        form = departamentoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('arriendo')  
            except:  
                pass  
    else:  
        form = departamentoForm()  
    return render(request,'app/departamento.html',{'form':form})