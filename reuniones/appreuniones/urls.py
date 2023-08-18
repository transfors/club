from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:year>/<str:mes>/',views.index, name='index'),
    path('listar_reuniones',views.listar_reuniones,name='listar_reuniones'),
    # ruta de ubicación de la vista agregar_empresa del app
    # agregar_empresa nombre de la plantilla html
    path('agregar_empresa',views.agregar_empresa,name='agregar_empresa'),
    path('listar_empresa',views.listar_empresa,name='listar_empresa'),
    # para devolver las empresas por su id creamos un parámetro
    # colocamos slash<empresa_id> para que 
    # django sepa que le vamos a pasar un id de para c/empresa
    path('mostrar_empresa/<empresa_id>',views.mostrar_empresa,name='mostrar_empresa'),
    path('buscar_empresas',views.buscar_empresas,name='buscar_empresas'),
    path('actualizar_empresa/<empresa_id>',views.actualizar_empresa, name='actualizar_empresa'),
    path('agregar_reunion',views.agregar_reunion,name='agregar_reunion'),
    path('actualizar_reunion/<reunion_id>',views.actualizar_reunion,name='actualizar_reunion'),
    path('borrar_reunion/<reunion_id>',views.borrar_reunion,name='borrar_reunion'),
    path('borrar_empresa/<empresa_id>',views.borrar_empresa,name='borrar_empresa'),
    path('csv_empresa',views.csv_empresa,name='csv_empresa'),
    path('pdf_empresa',views.pdf_empresa,name='pdf_empresa'),
]

