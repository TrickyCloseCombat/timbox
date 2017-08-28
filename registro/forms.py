from django import forms
from .models import Sucursal,Empleado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SucursalForm(forms.ModelForm):
  class Meta:
	model = Sucursal
	fields = ('nombre','calle','colonia','numeroExterior','numeroInterior','codigoPostal','ciudad','pais')

class EmpleadoForm(forms.ModelForm):
  class Meta:
	model = Empleado
	fields = ('nombre','rfc','puesto')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    rfc = forms.CharField(max_length=30, required=True, help_text='Obligatorio.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','rfc' )
