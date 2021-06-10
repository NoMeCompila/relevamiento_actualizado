#from relevamiento.farmacia.models import Farmacia

from usuario.forms import LoginForm
from django.http import request
from django.views.generic.edit import CreateView
from .forms import FarmaciaForm, ProgramaForm, ProvinciaForm
from .models import Farmacia, Fcia, Programa, Provincia
from django.core.exceptions import ObjectDoesNotExist
 #import de las vistas basadas en clases
from django.views.generic import ( 
                                TemplateView, #Vista basada en clase para renderizar una página estática simple 
                                ListView, #Vista basada en clase para renderizar un template de listas
                                UpdateView, #Vista basada en clase para renderizar un template de Actualizacón
                                CreateView, #Vista basada en clase para renderizar un template de Creacion
                                DeleteView) #Vista basada en clase para renderizar un template de Borrado
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout, authenticate


# def login_request(request):
#     login(request)
#     form = LoginForm()
#     return render(request, 'farmacia/login.html',{'form':form})

# def logout_request(request):
#     logout(request)
#     #messages.info(request, "logout exitoso")
#     return redirect('login')
# Vista basada en clase para renderizar un template simple
class Inicio(TemplateView):
    template_name = 'index.html'

class Login(TemplateView):
    template_name = 'farmacia/login.html' # indicar la ruta desde la raiz sin especificar esta misma

#-------------------------- CRUD de programas --------------------------
# Vista basada en clase para listar programas (EN PROCESO)
class ListarProgramas(ListView):
    model = Programa
    template_name = 'farmacia/lista_programas.html'
    context_object_name = 'programas'
    queryset = Programa.objects.all() # esta funcion devuelve una consulta que retorna todas las filas de la tabla programa

# Vista basada en clase para agregar un nuevo programa
class AgregarPrograma(CreateView):
    model = Programa
    template_name = 'farmacia/agregar_programa.html'
    form_class = ProgramaForm
    success_url = reverse_lazy('farmacia:lista_programas')

# Vista basada en clase para eliminar completamente un objeto de la base de datos 
class EliminarPrograma(DeleteView):
    model = Programa
    success_url =  reverse_lazy('farmacia:lista_programas')

class Actualizarprograma(UpdateView):

    model = Programa
    template_name = 'farmacia/agregar_programa.html'
    form_class = ProgramaForm
    success_url = reverse_lazy('farmacia:lista_programas')
#-------------------------------------------------------------------------------------------------
# Vista basada en clase que permite listar los datos de una tabla
class ListarProv(ListView):
    model = Provincia
    template_name = 'farmacia/listar_provincias.html'
    context_object_name = 'provincias'
    queryset = Provincia.objects.all()

# Vista basada en clase que permite crear un nuevo objeto en la base de datos
class CrearProv(CreateView):
    model = Provincia
    template_name = 'farmacia/agregar_prov.html'
    form_class = ProvinciaForm
    success_url = reverse_lazy('farmacia:listar_provincias')

# vista basada en clase que  hace una eliminación directa de los registros de la base de datos
class EliminarProv(DeleteView):
    model = Provincia
    success_url = (reverse_lazy('farmacia:listar_provincias'))   

# Vista para crear un programa
class CrearPrograma(CreateView):
    model = Programa
    template_name = 'farmacia/agregar_programa.html'
    form_class = ProgramaForm
    success_url = reverse_lazy('farmacia:listar_programas')

class ActualizarProv(UpdateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'farmacia/agregar_prov.html'
    success_url = reverse_lazy('farmacia:listar_provincias')

# Codigo para editar una provincia
class EditarProvincia(UpdateView):
    model = Provincia
    template_name = 'farmacia/agregar_prov.html'
    form_class = ProvinciaForm
    success_url = reverse_lazy('farmacia:listar_provincias')

class CrearFcia(TemplateView):
    template_name = 'farmacia/agregar_prov.html' 
# def Lista_Fcia(request):
#     fcias = Fcia.objects.all()
#     return render(request,'farmacia/probando_lista.html',{'fcias':fcias})

# VISTA BASADA EN CLASE PARA LISTAR UNA TABLA
class ListarFcias(ListView):
    model = Fcia
    template_name = 'farmacia/probando_lista.html'
    context_object_name = 'fcias'
    queryset = Fcia.objects.all()