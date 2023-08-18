from django.contrib import admin
from appreuniones.models import Empresa,UsuarioReunion,Reunion

# Register your models here.

admin.site.register(UsuarioReunion)

@admin.register(Empresa)
class Empresa_admin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    # SEPARAR CON UNA COMA
    ordering = ('nombre',)
    search_fields = ('nombre','direccion')
    
class Reunion_admin(admin.ModelAdmin):
    fields = (('nombre','empresa'),'presentador','fecha_reunion', 'descripcion','asistentes')
    list_display = ('nombre', 'fecha_reunion', 'empresa')
    list_filter = ('fecha_reunion','empresa')
    ordering = ('fecha_reunion',)

admin.site.register(Reunion,Reunion_admin)
