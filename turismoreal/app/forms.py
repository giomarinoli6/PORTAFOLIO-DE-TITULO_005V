from django import forms
from django.forms import widgets
from .models import Registro

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = ["nombre", "correo", "tipo_registro", "mensaje", "avisos"]
    widgets
    
        #fields = '__all__'