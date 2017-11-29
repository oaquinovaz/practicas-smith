#Práctica 4: Views
from django.shortcuts import render
#Práctica 7: Managers
from .models import Practicas, Animes, Ninjas, EjercitoDeLasMurallas, GuerrerosZ, Musicos
#Práctica 8: Formularios
from .forms import Practicas_Form, Animes_Form, Ninjas_Form, EjercitoDeLasMurallas_Form, GuerrerosZ_Form, Musicos_Form
#Práctica 9: Vistas basadas en clases
from django.views.generic import ListView
#Práctica 10: Formularios mecanicos
from .forms import Animes_FormMecanico, Ninjas_FormMecanico, EjercitoDeLasMurallas_FormMecanico, GuerrerosZ_FormMecanico, Musicos_FormMecanico
from django.http import HttpResponseRedirect, HttpResponse
#Páctica 11: Login
from django.contrib.auth import authenticate, login
#Páctica 12: SignUp
from .forms import User_Form
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

#from django.views.generic import CreateView

#from django.core import serializers

#Práctica 4: Views
def base(request):
    return render(request, 'base.html', {})

#Práctica 4: Views
def index(request):
    #Práctica 7: Managers
    practicas = list(Practicas.objects.all())
    return render(request, 'index.html', {'practicas': practicas})

#Práctica 4: Views
def anime(request):
    #Práctica 7: Managers
    animes = list(Animes.objects.all())
    return render(request, 'animes.html', {'animes': animes})

#Práctica 4: Views
def naruto(request):
    #Práctica 7: Managers
    ninjas = list(Ninjas.objects.all())
    return render(request, 'naruto.html', {'ninjas': ninjas})

#Práctica 4: Views
def snk(request):
    #Práctica 7: Managers
    soldados = list(EjercitoDeLasMurallas.objects.all())
    return render(request, 'snk.html', {'soldados': soldados})

#Práctica 4: Views
def dbs(request):
    #Práctica 7: Managers
    guerreros = list(GuerrerosZ.objects.all())
    return render(request, 'dbs.html', {'guerreros': guerreros})

#Práctica 4: Views
def swknu(request):
    #Práctica 7: Managers
    musicos = list(Musicos.objects.all())
    return render(request, 'swknu.html', {'musicos': musicos})

#Práctica 8: Formularios
def formPracticas(request):
    form = Practicas_Form(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'formPracticas.html', {"form":form})

#Práctica 8: Formularios
def formAnimes(request):
    form = Animes_Form(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'formAnimes.html', {"form":form})

#Práctica 8: Formularios
def formNaruto(request):
    form = Ninjas_Form(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'formNaruto.html', {"form":form})

#Práctica 8: Formularios
def formSNK(request):
    form = EjercitoDeLasMurallas_Form(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'formSNK.html', {"form":form})

#Práctica 8: Formularios
def formDBS(request):
    form = GuerrerosZ_Form(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'formDBS.html', {"form":form})

#Práctica 8: Formularios
def formSWKNU(request):
    form = Musicos_Form(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'formSWKNU.html', {"form":form})

#Práctica 9: Vistas basadas en clases:
class Animes_List(ListView):
    model = Animes
    template_name = 'animes_list.html'

#Práctica 9: Vistas basadas en clases:
class Ninjas_List(ListView):
    model = Ninjas
    template_name = 'ninjas_list.html'

#Práctica 9: Vistas basadas en clases:
class Soldados_List(ListView):
    model = EjercitoDeLasMurallas
    template_name = 'soldados_list.html'

#Práctica 9: Vistas basadas en clases:
class Guerreros_List(ListView):
    model = GuerrerosZ
    template_name = 'guerreros_list.html'

#Práctica 9: Vistas basadas en clases:
class Musicos_List(ListView):
    model = Musicos
    template_name = 'musicos_list.html'

#Práctica 10: Formularios mecanicos
def formMecanicoAnimes(request):
    if request.method == 'POST':
        form = Animes_FormMecanico(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            genero = form.cleaned_data['genero']
            episodios = form.cleaned_data['episodios']
            añoLanzamiento = form.cleaned_data['añoLanzamiento']
            return HttpResponseRedirect('/anime/')
    else:
        form = Animes_FormMecanico()

    return render(request, 'formMecanicoAnimes.html', {'form': form})

#Práctica 10: Formularios mecanicos
def formMecanicoNinjas(request):
    if request.method == 'POST':
        form = Ninjas_FormMecanico(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            clan = form.cleaned_data['clan']
            aldea = form.cleaned_data['aldea']
            nivelMilitar = form.cleaned_data['nivelMilitar']
            jutsu = form.cleaned_data['jutsu']
            nivelChakra = form.cleaned_data['nivelChakra']
            return HttpResponseRedirect('/naruto/')
    else:
        form = Ninjas_FormMecanico()

    return render(request, 'formMecanicoNinjas.html', {'form': form})

#Práctica 10: Formularios mecanicos
def formMecanicoSNK(request):
    if request.method == 'POST':
        form = EjercitoDeLasMurallas_FormMecanico(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            distrito = form.cleaned_data['distrito']
            muralla = form.cleaned_data['muralla']
            ejercito = form.cleaned_data['ejercito']
            gigantesAsesinados = form.cleaned_data['gigantesAsesinados']
            return HttpResponseRedirect('/snk/')
    else:
        form = EjercitoDeLasMurallas_FormMecanico()

    return render(request, 'formMecanicoSoldados.html', {'form': form})

#Práctica 10: Formularios mecanicos
def formMecanicoDBS(request):
    if request.method == 'POST':
        form = GuerrerosZ_FormMecanico(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            raza = form.cleaned_data['raza']
            nivelKi = form.cleaned_data['nivelKi']
            transformacionMasPoderosa = form.cleaned_data['transformacionMasPoderosa']
            habilidadEspecial = form.cleaned_data['habilidadEspecial']
            planetaOrigen = form.cleaned_data['planetaOrigen']
            universo = form.cleaned_data['universo']
            return HttpResponseRedirect('/dbs/')
    else:
        form = GuerrerosZ_FormMecanico()

    return render(request, 'formMecanicoGuerreros.html', {'form': form})

#Práctica 10: Formularios mecanicos
def formMecanicoSWKNU(request):
    if request.method == 'POST':
        form = Musicos_FormMecanico(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            edad = form.cleaned_data['edad']
            instrumento = form.cleaned_data['instrumento']
            concursosGanados = form.cleaned_data['concursosGanados']
            
            return HttpResponseRedirect('/swknu/')
    else:
        form = Musicos_FormMecanico()

    return render(request, 'formMecanicoMusicos.html', {'form': form})

#Páctica 11: Login
def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

#Páctica 12: SignUp
class SignUp(FormView):
    template_name = 'signup.html'
    form_class = User_Form
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        p = Usuarios()
        p.usuario = user
        p.telefono = form.cleaned_data['telefono']
        p.correo = form.cleaned_data['correo']
        p.save()

        return super(SignUp, self).form_valid(form)
