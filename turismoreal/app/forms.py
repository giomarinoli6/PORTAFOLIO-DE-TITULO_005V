
from django import forms
from django.forms import widgets
from .models import Departamento, Location, Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = fields = "__all__" 

class departamentoForm(forms.ModelForm):  
    class Meta:  
        model = Departamento 
        fields = "__all__"  


class LocationForm(forms.ModelForm):  
    class Meta:  
        model = Location 
        fields = "__all__"  

