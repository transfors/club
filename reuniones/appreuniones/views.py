from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# Reunion como se llama en Models.py
from . models import Reunion, Empresa
from . forms import FormularioEmpresa, FormularioReunion
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.core.exceptions import ObjectDoesNotExist
import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.paginator import Paginator


# Create your views here.

def pdf_empresa(request):
    Buffer = io.BytesIO()
    canv = canvas.Canvas(Buffer,pagesize=letter,bottomup=0)
    texto = canv.beginText()
    texto.setTextOrigin(inch,inch)
    texto.setFont('Helvetica',15)
    empresas = Empresa.objects.all()
    lineas = []
    for empresa in empresas:
        lineas.append(empresa.nombre)
        lineas.append(empresa.direccion)
        lineas.append(empresa.codigo_postal)
        lineas.append(empresa.telefono)
        lineas.append(empresa.pagina_web)
        lineas.append(empresa.email)
        lineas.append('*****************************************')
    for linea in lineas:
        texto.textLine(linea)
    canv.drawText(texto)
    canv.showPage()
    canv.save()
    Buffer.seek(0)
    return FileResponse(Buffer,as_attachment=True,filename='Empresas.pdf')
    

    

def csv_empresa(request):
    respuesta = HttpResponse(content_type='text/csv')
    respuesta['Content-Disposition'] = 'attachment; filename = Empresas.csv'
    escritor = csv.writer(respuesta)
    empresas = Empresa.objects.all()
    escritor.writerow(['Nombre Empresa','Dirección','Código Postal','Teléfono', 'Página Web', 'Email'])
    for empresa in empresas:
        escritor.writerow([empresa.nombre,
                           empresa.direccion,
                           empresa.codigo_postal,
                           empresa.telefono,
                           empresa.pagina_web,
                           empresa.email])
    return respuesta
    
    

def borrar_empresa(request, empresa_id):
    # vamos a extraer un solo dato
    try:
        mi_empresa = Empresa.objects.get(pk = empresa_id)
        mi_empresa.delete()
    except Empresa.DoesNotExist:
        pass
    return redirect('listar_empresa')
    
    

def borrar_reunion(request, reunion_id):
    # vamos a extraer un solo dato
    try:
        mi_reunion = Reunion.objects.get(pk = reunion_id)
        mi_reunion.delete()
    except Reunion.DoesNotExist:
        pass
    return redirect('listar_reuniones')
    
    
def actualizar_reunion(request,reunion_id):
    mireunion = Reunion.objects.get(pk=reunion_id)
    formulario_reunion = FormularioReunion(request.POST or None,instance=mireunion)
    if formulario_reunion.is_valid():
        formulario_reunion.save()
        return redirect('listar_reuniones')
        
    return render(request,'archivos/actualizar_reunion.html',{'mireunion':mireunion,"formulario_reunion":formulario_reunion})


def agregar_reunion(request):
    enviado = False
    if request.method == 'POST':
        formulario = FormularioReunion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/agregar_reunion?enviado=True')
    else:
        formulario = FormularioReunion
    if 'enviado' in request.GET:
        enviado = True
    return render(request, 'archivos/agregar_reunion.html', {"formulario": formulario, "enviado": enviado})

def actualizar_empresa(request,empresa_id):
    empresa = Empresa.objects.get(pk=empresa_id)
    formulario_empresa = FormularioEmpresa(request.POST or None,instance=empresa)
    if formulario_empresa.is_valid():
        formulario_empresa.save()
        return redirect('listar_empresa')
        
    return render(request,'archivos/actualizar_empresa.html',{'empresa':empresa,"formulario_empresa":formulario_empresa})

def buscar_empresas(request):
    if request.method == "POST":
        buscar = request.POST["buscar"]
        empresas = Empresa.objects.filter(nombre__contains=buscar)
        # primer buscar es el name y el segundo es la variable definida arriba
        return render(request, 'archivos/buscar_empresas.html', {'buscar':buscar,'empresas':empresas})
    else:
        return render(request, 'archivos/buscar_empresas.html')

# acá debo pasar el parámetro que tienen
# que ser igual al nombre del parámetro 
# creado en el path en urls.py
def mostrar_empresa(request,empresa_id):
    # para obtener un solo elemento usamos el 
    # módulo pk: pk=empresa_id
    empresa = Empresa.objects.get(pk=empresa_id)
    # en el diccionario la clave puede ser cualquiera, pero el
    # valor tiene que ser igual a la variable que cree recién
    return render(request,'archivos/mostrar_empresa.html',{'empresa':empresa})

# listar_empresa es el name='listar_empresa' de urls.py
def listar_empresa(request):
    # traer todos los elementos de la tabla Empresa
    # y guardalos en la variable listar_empresa
    # listar_empresa = Empresa.objects.all().order_by('nombre')
    listar_empresa = Empresa.objects.all()
    paginar = Paginator(Empresa.objects.all(), 2)
    page = request.GET.get('page')
    empresas = paginar.get_page(page)
    num_page = "a" * empresas.paginator.num_pages
    
    # empresa.html nombre de mi plantilla
    # listar_empresa nombre de la variable
    # que tiene que ser la misma para el diccionario
    return render(request,'archivos/empresa.html',{'listar_empresa':listar_empresa,
        'empresas':empresas,
        'num_page':num_page})
    

def listar_reuniones(request):
    listar_reunion = Reunion.objects.all().order_by('fecha_reunion')

    return render(request, 'archivos/listar_reuniones.html', {"listar_reunion": listar_reunion})


def index(request, year=datetime.now().year, mes=datetime.now().strftime('%B')):
    nombre = 'Gustavo'
    mes = mes.capitalize()
    numero_mes = list(calendar.month_name).index(mes)
    numero_mes = int(numero_mes)

    # CREAMOS EL CALENDARIO
    calendario = HTMLCalendar().formatmonth(year, numero_mes)
    hoy = datetime.now()
    year_actual = hoy.year
    hora_actual = hoy.strftime("%I:%M:%p")

    return render(request, 'archivos/index.html', {'mi_nombre': nombre,
                                                   'year': year,
                                                   'mes': mes,
                                                   'numero_mes': numero_mes,
                                                   'calendario': calendario,
                                                   'año_actual': year_actual,
                                                   'hora_actual': hora_actual, })

# agregar_empresa es el nombre que le asigne
# a path en el archivo urls.py
def agregar_empresa(request):
    enviado = False
    if request.method == 'POST':
        formulario = FormularioEmpresa(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/agregar_empresa?enviado=True')
    else:
        formulario = FormularioEmpresa
    if 'enviado' in request.GET:
        enviado = True
    return render(request, 'archivos/agregar_empresa.html', {"formulario": formulario, "enviado": enviado})

