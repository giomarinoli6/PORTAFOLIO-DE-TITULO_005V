
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm

"""class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields =  ['nombreUsuario','telefono','email','sexo','password']
"""
class departamentoForm(forms.ModelForm):  
    class Meta:  
        model = Departamento 
        fields = "__all__"  


class LocationForm(forms.ModelForm):  
    class Meta:  
        model = Location 
        fields = "__all__"  

class ReservaForm(forms.ModelForm):  
    class Meta:  
        model = Reserva 
        fields =['fecha_inicio', 'n_dias', 'id_usuario', 'id_departamento']
        widgets = {
            'fecha_inicio':  forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control','placeholder': 'Select a date',     'type': 'date'}),
              'id_usuario':forms.TextInput(attrs={'readonly': 'readonly'}),
              'n_dias':forms.NumberInput(attrs={'onchange' : "myFunction();", 'value':0}),
        }

        def clean_date(self):
            date = self.cleaned_data['date']
            if date < datetime.date.today():
                raise forms.ValidationError("The date cannot be in the past!")
            return date

class UserCustom(UserCreationForm):
    pass

class CheckInForm(forms.ModelForm):  
    class Meta:  
        model = CheckIn 
        fields = "__all__"  
        widgets={
            'reserva':forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class CheckInFormAdmin(forms.ModelForm):  
    class Meta:  
        model = CheckIn 
        fields = "__all__"  

class CheckOutFormAdmin(forms.ModelForm):  
    class Meta:  
        model = CheckOut
        fields = "__all__"  
