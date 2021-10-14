from django.shortcuts import render, redirect 
from .models import  Departamento, Location
from .forms import LocationForm, RegistroForm ,departamentoForm

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



def reserva(request, id):
    departamento = Departamento.objects.get(id=id)
    return render(request, 'app/reservar.html', {'departamento':departamento})



  


# Views Location-----------------------------------------------------------------------------------------
def crearLocation(request):
    if request.method == "POST":
        formularioLocation = LocationForm (request.POST)
        if formularioLocation.is_valid():
            print("ESTOY EN IF 2")
            try:
                formularioLocation.save()
                return redirect('/verLocation')
            except:
                pass
        else:
            print(formularioLocation.is_valid())
    else:
        formularioLocation = LocationForm()
    return render(request,'app/crudLocation.html',{'formularioLocation':formularioLocation})

def verLocation(request):
    locaciones = Location.objects.all()
    return render (request, "app/verLocation.html",{'locaciones':locaciones})


def editarLocation(request, id):
    print("entra en editarLocation 1")
    
    locacion= Location.objects.get(id=id) 
    # formularioLocation = LocationForm (instance= locacion) 
    return render(request,"app/editarLocation.html", {'locacion':locacion})  



def actualizarLocation(request, id):
    print("entra en actualizarLocation 2")
    
    locacion = Location.objects.get(id=id)

    data={
        'form':LocationForm(instance=locacion)
    }

    formularioLocation = LocationForm(data=request.POST , instance = locacion)
    if formularioLocation.is_valid():
        print("entra a guardar")
        formularioLocation.save()
        return redirect('/verLocation/')
    return render(request,"app/editarLocation.html", {'locacion':locacion, 'formulario':formularioLocation})

def eliminarLocation(request, id):  
    locaciones = Location.objects.get(id=id)  
    locaciones.delete()  
    return redirect('/verLocation/')

# end Views Location-----------------------------------------------------------------------------------------------------






    

# Views Departamento

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
    return render(request,'app/ingresarDepartamento.html',{'form':form})

def arriendodepa(request):
    departamentos = Departamento.objects.all()

    return render(request, "app/arriendo.html",{'departamentos': departamentos})

def editarDepartamento(request, id):
    print("entra en editarDepartament 1")
    departamento= Departamento.objects.get(id=id) 
    return render(request,"app/editarDepartamento.html", {'departamento':departamento})  

def actualizarDepartamento(request, id):
    print("entra en actualizardepartamento 2")
    
    departamento = Departamento.objects.get(id=id)

    data={
        'form':departamentoForm(instance=departamento)
    }

    formularioLocation = departamentoForm(data=request.POST , instance = departamento)
    if formularioLocation.is_valid():
        print("entra a guardar")
        formularioLocation.save()
        return redirect('/arriendo/')
    return render(request,"app/editarDepartamento.html", {'departamento':departamento, 'formulario':formularioLocation})

def eliminarDepartamento(request, id):  
    departamentos = Departamento.objects.get(id=id)  
    departamentos.delete()  
    return redirect('/arriendo/')