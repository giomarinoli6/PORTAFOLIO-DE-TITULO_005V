
from django import forms
from django.forms import widgets
from .models import Departamento, Registro
class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = fields = "__all__" 

class departamentoForm(forms.ModelForm):  
    class Meta:  
        model = Departamento 
        fields = "__all__"  