from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Sucursal(models.Model):
    title = models.CharField(max_length=150, blank = True)
    nombre = models.CharField(max_length=150)
    calle = models.CharField(max_length=150)
    colonia = models.CharField(max_length=150)
    numeroExterior = models.CharField(max_length=150, blank = True)
    numeroInterior = models.CharField(max_length=150, blank = True)
    codigoPostal = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    
    def __str__(self):
         return self.nombre	

class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    rfc = models.CharField(max_length=150)
    puesto = models.CharField(max_length=150)
    def __str__(self):
	return self.nombre
    
class UserProfile(models.Model):
   user = models.OneToOneField(User)
   rfc = models.CharField(max_length=256, blank=True, null=True)
