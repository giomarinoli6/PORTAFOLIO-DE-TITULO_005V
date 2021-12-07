from django.shortcuts import render, redirect, get_object_or_404
from .models import  Departamento, Location, Reserva
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def home(request):
    context={
        'lista_departamentos':Departamento.objects.all(),
        'reserva_precio':Reserva.objects.all(),
    }
    return render(request, 'app/index.html', context)

    
@login_required(login_url='/accounts/login/')
def reserva(request, id_depa):
   
        
       
        depa=Departamento.objects.get(id=id_depa)
        user = User.objects.get(id=request.user.id)
        dato={'id_usuario':user, 'id_departamento':depa}
        data={
        
    
            'form':ReservaForm(initial=dato),
            'user':request.user,
        }
        return render(request, 'app/arriendo.html', data)


@login_required(login_url='/accounts/login/')
def crear_reserva(request):
    context={
            'form':ReservaForm,
            
        }

    if request.method == "POST":
        formulario_reserva = ReservaForm(data=request.POST)

        if formulario_reserva.is_valid():
            formulario_reserva.save()
            return redirect(to='historial')
    else:
        formulario_reserva = departamentoForm()
 
    return render(request, 'app/reserva.html')   

def registro_de_usuario(request):
    data={
        'form':UserCustom(),
    }

    if request.method == 'POST':
        formualario = UserCustom(data=request.POST)
        if formualario.is_valid:
            formualario.save()
            user = authenticate(username=formualario.cleaned_data['username'], password=formualario.cleaned_data['password1'])
            login(request, user)
            return redirect(to='home')
        data['form']=formualario

    return render(request, 'registration/registro.html', data)

def departamento(request):
    context={
        'lista_departamentos':Departamento.objects.all()
    }
    
    return render(request, 'app/departamentos.html', context)

def dep_individual(request, id):
    dpto=Departamento.objects.get(id=id)

    context={
        'dpto':dpto,
    }
    return render(request,'app/depa_individual.html', context )

def historial(request):
    user=request.user
    historial=Reserva.objects.filter(id_usuario=user)
    return render(request,"app/historial.html", { 'historial':historial})

def eliminarReserva(request, id):

    reserva= get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect(to='historial')

def checkIn(request, id):

    reserva= get_object_or_404(Reserva, id=id)
    if request.user.id == reserva.id_usuario.id:
        
        dato={'reserva':reserva}
        if request.method == "POST":
            formulario = CheckInForm(request.POST)
            if formulario.is_valid():
                print("ESTOY EN IF 2")
                formulario.save()
                return redirect(to='historial')
        else:
            formulario = CheckInForm(initial=dato)

        
        context={
            'form':formulario
        }
    


        
        return render(request,"app/checkin.html", context)
    else:

        return redirect(to='historial')