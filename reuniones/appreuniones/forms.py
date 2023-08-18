from django import forms
from django.forms import ModelForm
from . models import Empresa, Reunion

class FormularioEmpresa(ModelForm):
    class Meta:
        model = Empresa
        fields = ("nombre","direccion","codigo_postal","telefono","pagina_web","email")
        labels = {
            'nombre':'',
            'direccion':'',
            'codigo_postal':'',
            'telefono':'',
            'pagina_web':'',
            'email':'',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Direccion'}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Código Postal'}),
            'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Teléfono'}),
            'pagina_web': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Página Web'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'E-mail'}),
        }
        
        
class FormularioReunion(ModelForm):
    class Meta:
        model = Reunion
        fields = ("nombre","fecha_reunion","empresa","presentador","descripcion","asistentes")
        labels = {
            'nombre':'',
            'fecha_reunion':'YYYY-MM-DD HH:MM:SS',
            'empresa':'La empresa',
            'presentador':'El presentador',
            'descripcion':'',
            'asistentes':'Los Asistentes de la Reunión',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'fecha_reunion': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Fecha de la Reunion'}),
            'empresa': forms.Select(attrs={'class':'form-control', 'placeholder': 'Empresa'}),
            'presentador': forms.Select(attrs={'class':'form-control', 'placeholder': 'Presentador'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Descripción'}),
            'asistentes': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'Asistentes'}),
        }