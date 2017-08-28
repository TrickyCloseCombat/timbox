from django.shortcuts import render, get_object_or_404,redirect
from .models import Sucursal,Empleado,UserProfile
from .forms import SucursalForm,EmpleadoForm,SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

######################################################################################################
#home
######################################################################################################
@login_required
def home(request):
    return render(request,'home/home.html', {})

#########################################################################################################
#Vistas de los empleados
####################################################################################################
@login_required
def empleado_list(request):
    empleados =  Empleado.objects.all()
    return render(request, 'empleados/empleado_list.html',{'empleados':empleados})
@login_required
def empleado_new(request):
    if request.method == "POST":
	form = EmpleadoForm(request.POST)
	if form.is_valid():
	   empleado = form.save(commit = False)
	   empleado.save()
    else:
	form = EmpleadoForm()
    return render(request,'empleados/empleado_edit.html',{'form':form})
@login_required
def empleado_edit(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        form = EmpleadoForm(request.POST,instance=empleado)
	if form.is_valid():
	   empleado = form.save(commit = False)
	   empleado.save()
	   return redirect ('empleado_list')
    else:
       form = EmpleadoForm(instance=empleado)
    return render(request,'empleados/empleado_edit.html',{'form':form})

######################################################################################################
#Vistas de las sucursales
######################################################################################################
@login_required
def sucursal_list(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/sucursal_list.html',{'sucursales': sucursales})
@login_required
def sucursal_new(request):
    if request.method == "POST":
        form = SucursalForm(request.POST)
        if form.is_valid():
           sucursal = form.save(commit=False)
           sucursal.save()
    else:
      form = SucursalForm()
    return render(request, 'sucursal/sucursal_edit.html',{'form':form})
@login_required
def sucursal_edit(request, pk):
    sucursal = get_object_or_404(Sucursal,pk=pk)
    if request.method == "POST":
       form = SucursalForm(request.POST, instance=sucursal)
       if form.is_valid():
          sucursal = form.save(commit = False)
	  sucursal.save()
	  return redirect('sucursal_list')
    else:
	form = SucursalForm(instance=sucursal)
    return render(request, 'sucursal/sucursal_edit.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
	    #user.refresh_from_db()
	    #user.userprofile.rfc = form.cleaned_data.get('rfc')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

























