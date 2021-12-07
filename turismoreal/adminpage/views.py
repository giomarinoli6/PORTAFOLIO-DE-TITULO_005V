from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from app.forms import *
from app.models import Location, Reserva
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url='/accounts/login/')
@staff_member_required
def inicio(request):

    total=0
    reserva=Reserva.objects.all()
    for dato in reserva:
        total+=dato.get_total()


    context={
        'user_count':User.objects.all().count(),
        'ganancias':total,
        'reservas':Reserva.objects.all().count(),
        'depa':Departamento.objects.all().count(),
        'reserva':reserva,
        
    }

    return render(request, 'inicio.html',context)

@login_required(login_url='/accounts/login/')
@staff_member_required
def crearLocation(request):

    if request.method == "POST":
        formularioLocation = LocationForm (request.POST)
        if formularioLocation.is_valid():
            print("ESTOY EN IF 2")
            formularioLocation.save()
    else:
        formularioLocation = LocationForm()
    return render(request,'admin/crearLocation.html',{'formularioLocation':formularioLocation, 'lista_locaciones':Location.objects.all()})

@login_required(login_url='/accounts/login/')
@staff_member_required
def modificarLocation(request, id):
    print("entra en actualizarLocation 2")
    
    locacion = get_object_or_404(Location, id=id)

    data={
        'form':LocationForm(instance=locacion),
       
    }
    
    if request.method == 'POST':
        formulario= LocationForm(data=request.POST, instance=locacion)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='crear-locacion')
        data['form']=formulario

    return render(request,"admin/editarLocation.html", data)

@login_required(login_url='/accounts/login/')
@staff_member_required
def eliminarLocation(request, id):

    locacion= get_object_or_404(Location, id=id)
    locacion.delete()
    return redirect(to='crear-locacion')

@login_required(login_url='/accounts/login/')
@staff_member_required    
def crearDepartamento(request):
    context={
            'form':departamentoForm,
            'lista':Departamento.objects.all()
        }

    if request.method == "POST":
        formulario_departamento = departamentoForm(data=request.POST, files=request.FILES)

        if formulario_departamento.is_valid():
            formulario_departamento.save()
    else:
        formulario_departamento = departamentoForm()
 
    return render(request,'admin/ingresarDepartamento.html',context)

@login_required(login_url='/accounts/login/')
@staff_member_required
def modificarDepartamento(request, id):
    
    
    departamento = get_object_or_404(Departamento, id=id)

    data={
        'form':departamentoForm(instance=departamento),
       
    }
    
    if request.method == 'POST':
        formulario= departamentoForm(data=request.POST, instance=departamento,  files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='departamento')
        data['form']=formulario

    return render(request,"admin/editarLocation.html", data)

@login_required(login_url='/accounts/login/')
@staff_member_required
def eliminarDepartamento(request, id):

    departamento= get_object_or_404(Departamento, id=id)
    departamento.delete()
    return redirect(to='departamento')

def mantenedorUsuarios(request):
    users=User.objects.all()
    reservas=Reserva.objects.all()
    return render(request, 'admin/mantenedorUsuarios.html', {'users':users, 'reservas':reservas})

def mantenedorReservas(request):
    reservas=Reserva.objects.all()
    
    return render(request, 'admin/reservas.html', {'reservas':reservas})

def checkIn(request, id):
    reserva= get_object_or_404(Reserva, id=id)
    dato={'reserva':reserva}


    if request.method == "POST":
        formulario = CheckInForm(request.POST)
        if formulario.is_valid():
               
                formulario.save()
                return redirect(to='mantenedor-reservas')


    return render(request, 'admin/checkin.html',{'form':CheckInFormAdmin(initial=dato)} )


def checkOut(request, id):
    reserva= get_object_or_404(Reserva, id=id)
    dato={'reserva':reserva}


    if request.method == "POST":
        formulario = CheckOutFormAdmin(request.POST)
        if formulario.is_valid():
               
                formulario.save()
                return redirect(to='mantenedor-reservas')


    return render(request, 'admin/checkin.html',{'form':CheckOutFormAdmin(initial=dato)} )


def checkOutInfo(request, id):
    checkout= get_object_or_404(CheckOut, id=id)
    context={
        'checkout':checkout,
        'name':'CHECK-OUT'
    }
    return render(request, 'admin/info.html',context )

def checkInInfo(request, id):
    checkout= get_object_or_404(CheckIn, id=id)
    context={
        'checkout':checkout,
        'name':'CHECK-IN'
    }
    return render(request, 'admin/info.html',context )