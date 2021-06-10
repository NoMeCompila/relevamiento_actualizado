# es necesario el url patterns  #URL CRUD
#from relevamiento.farmacia.models import Provincia
from django.urls import path
# from django.urls import reverse_lazy
from .views import (
    ListarProgramas,
    AgregarPrograma,
    EliminarPrograma,
    Actualizarprograma,
    EliminarProv,
    ActualizarProv,
    CrearProv, 
    CrearFcia, 
    ListarProv,  
    ListarFcias,   
    Login
)

urlpatterns = [
    #-------------------------------- LOGIN --------------------------------
    path('login/', Login.as_view(), name  = 'login'),

    #-------------------------- Ruteo de CRUD  Para Programas --------------------------
    path('lista_programas/', ListarProgramas.as_view(), name = 'lista_programas'),
    path('agregar_programas/', AgregarPrograma.as_view(), name = 'agregar_programas'),
    path('eliminar_programa/<int:pk>', EliminarPrograma.as_view(), name  = 'eliminar_programa'),
    path('actualizar_programa/<int:pk>', Actualizarprograma.as_view(), name  = 'actualizar_programa'),
    
    
    
    path("lista_farmacia/", ListarFcias.as_view(), name = "lista_farmacia"),
    path('listar_provincias/', ListarProv.as_view(), name  = 'listar_provincias'),
    path('agregar_prov/', CrearProv.as_view(), name  = 'agregar_prov'),
    path('eliminar_prov/<int:pk>', EliminarProv.as_view(), name  = 'eliminar_prov'),
    path('actualizar_prov/<int:pk>', ActualizarProv.as_view(), name  = 'actualizar_prov'),
] 
