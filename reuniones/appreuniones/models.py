from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField("Nombre Empresa",max_length=110)
    direccion = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=15)
    telefono = models.CharField("su telefono",max_length=11)
    pagina_web = models.URLField("Direccion pagina web")
    email = models.EmailField("Email")
    
    def __str__(self):
        return self.nombre
    
class UsuarioReunion(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Reunion(models.Model):
    nombre = models.CharField("nombre reunion",max_length=40)
    fecha_reunion = models.DateTimeField("Fecha")
    empresa = models.ForeignKey(Empresa,blank=True,null=True,on_delete=models.CASCADE)
    presentador = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    descripcion = models.TextField(blank=True)
    asistentes = models.ManyToManyField(UsuarioReunion,blank=True)
    
    def __str__(self):
        return self.nombre

