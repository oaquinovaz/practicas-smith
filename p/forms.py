#Práctica 8: Formularios
from django import forms
from .models import Practicas, Animes, Ninjas, EjercitoDeLasMurallas, GuerrerosZ, Musicos
#Páctica 12: SignUp
from django.contrib.auth.forms import UserCreationForm

#Práctica 8: Formularios
class Practicas_Form(forms.ModelForm):
	class Meta:
		model = Practicas
		fields = '__all__'

#Práctica 8: Formularios
class Animes_Form(forms.ModelForm):
	class Meta:
		model = Animes
		fields = '__all__'

#Práctica 8: Formularios
class Ninjas_Form(forms.ModelForm):
	class Meta:
		model = Ninjas
		fields = '__all__'

#Práctica 8: Formularios
class EjercitoDeLasMurallas_Form(forms.ModelForm):
	class Meta:
		model = EjercitoDeLasMurallas
		fields = '__all__'

#Práctica 8: Formularios
class GuerrerosZ_Form(forms.ModelForm):
	class Meta:
		model = GuerrerosZ
		fields = '__all__'

#Práctica 8: Formularios
class Musicos_Form(forms.ModelForm):
	class Meta:
		model = Musicos
		fields = '__all__'

#Práctica 10: Formularios mecanicos
class Animes_FormMecanico(forms.Form):
    Accion = 'Acción'
    ArtesMarciales = "Artes Marciales"
    Aventuras = "Aventuras"
    Carreras = "Carreras"
    CienciaFiccion = "Ciencia Ficción"
    Comedia = "Comedia"
    Demencia = "Demencia"
    Demonios = "Demonios"
    Deportes = "Deportes"
    Drama = "Drama"
    Ecchi = "Ecchi"
    Escolares = "Ecolares"
    Espacial = "Espacial"
    Fantasia = "Fantasía"
    Harem = "Harem"
    Historico = "Historico"
    Infantil = "Infantil"
    Josei = "Josei"
    Juegos = "Jegos"
    Magia = "Magia"
    Mecha = "Mecha"
    Militar = "Militar"
    Misterio = "Misterio"
    Musica = "Música"
    Parodia = "Parodia"
    Policia = "Policía"
    Psicologico = "Psicológico"
    Recuentrosdelavida = "Recuentros de la vida"
    Romance = "Romance"
    Samurai = "Samurai"
    Seinen = "Seinen"
    Shoujo = "Shoujo"
    Shounen = "Shounen"
    Sobrenatural = "Sobrenatural"
    Superpoderes = "Superpoeders"
    Suspenso = "Suspenso"
    Terror = "Terror"
    Vampiros = "Vampiros"
    Yaoi = "Yaoi"
    Yuri = "Yuri"

    generos = {
        (Accion, 'Acción'),
        (ArtesMarciales, "Artes Marciales"),
        (Aventuras, "Aventuras"),
        (Carreras, "Carreras"),
        (CienciaFiccion, "Ciencia Ficción"),
        (Comedia, "Comedia"),
        (Demencia, "Demencia"),
        (Demonios, "Demonios"),
        (Deportes, "Deportes"),
        (Drama, "Drama"),
        (Ecchi, "Ecchi"),
        (Escolares, "Ecolares"),
        (Espacial, "Espacial"),
        (Fantasia, "Fantasía"),
        (Harem, "Harem"),
        (Historico, "Historico"),
        (Infantil, "Infantil"),
        (Josei, "Josei"),
        (Juegos, "Jegos"),
        (Magia, "Magia"),
        (Mecha, "Mecha"),
        (Militar, "Militar"),
        (Misterio, "Misterio"),
        (Musica, "Música"),
        (Parodia, "Parodia"),
        (Policia, "Policía"),
        (Psicologico, "Psicológico"),
        (Recuentrosdelavida, "Recuentros de la vida"),
        (Romance, "Romance"),
        (Samurai,"Samurai"),
        (Seinen, "Seinen"),
        (Shoujo, "Shoujo"),
        (Shounen, "Shounen"),
        (Sobrenatural, "Sobrenatural"),
        (Superpoderes, "Superpoeders"),
        (Suspenso, "Suspenso"),
        (Terror, "Terror"),
        (Vampiros, "Vampiros"),
        (Yaoi, "Yaoi"),
        (Yuri, "Yuri"),
    }

    nombre = forms.CharField(max_length = 50)
    genero = forms.ChoiceField(generos)
    episodios = forms.IntegerField()
    añoLanzamiento = forms.DateTimeField()

#Práctica 10: Formularios mecanicos
class Ninjas_FormMecanico(forms.Form):
    Genin = 'Genin'
    Chunin = 'Chunin'
    Jonin = 'Jonin'
    Anbu = 'Anbu'
    Sannin = 'Sannin'
    Kage = 'Kage'
    nvlMil = {
        (Genin, 'Genin'),
        (Chunin, 'Chunin'),
        (Jonin, 'Jonin'),
        (Anbu, 'Anbu'),
        (Sannin, 'Sannin'),
        (Kage, 'Kage'),
    }

    nombre = forms.CharField(max_length = 35)
    clan = forms.CharField(max_length = 35)
    aldea = forms.CharField(max_length = 35)
    nivelMilitar = forms.ChoiceField(nvlMil)
    jutsu = forms.CharField(max_length = 50)
    nivelChakra = forms.FloatField()

#Práctica 10: Formularios mecanicos
class EjercitoDeLasMurallas_FormMecanico(forms.Form):
    Reconocimiento = 'Legion de Reconocimiento'
    Estacionarias = 'Tropas Estacionarias'
    Policia = 'Policia Militar'
    EjecitoMuralla = {
        (Reconocimiento,'Legion de Reconocimiento'),
        (Estacionarias, 'Tropas Estacionarias'),
        (Policia,'Policia Militar'),
    }

    Maria = 'Muralla Maria'
    Rose = 'Muralla Rose'
    Sina = 'Muralla Sina'
    Murallas = {
        (Maria, 'Muralla Maria'),
        (Rose, 'Muralla Rose'),
        (Sina, 'Muralla Sina'),
    }

    nombre = forms.CharField(max_length = 35)
    distrito = forms.CharField(max_length = 35)
    muralla = forms.ChoiceField(Murallas)
    ejercito = forms.ChoiceField(EjecitoMuralla)
    gigantesAsesinados = forms.IntegerField()

#Práctica 10: Formularios mecanicos
class GuerrerosZ_FormMecanico(forms.Form):
    Universo1 = '1'
    Universo2 = '2'
    Universo3 = '3'
    Universo4 = '4'
    Universo5 = '5'
    Universo6 = '6'
    Universo7 = '7'
    Universo8 = '8'
    Universo9 = '9'
    Universo10 = '10'
    Universo11 = '11'
    Universo12 = '12'
    Universos = {
        (Universo1, '1'),
        (Universo2, '2'),
        (Universo3, '3'),
        (Universo4, '4'),
        (Universo5, '5'),
        (Universo6, '6'),
        (Universo7, '7'),
        (Universo8, '8'),
        (Universo9, '9'),
        (Universo10, '10'),
        (Universo11, '11'),
        (Universo12, '12'),
    }
    nombre = forms.CharField(max_length = 35)
    raza = forms.CharField(max_length = 20)
    nivelKi = forms.FloatField()
    transformacionMasPoderosa = forms.CharField(max_length = 30)
    habilidadEspecial = forms.CharField(max_length = 30)
    planetaOrigen = forms.CharField(max_length = 20)
    universo = forms.ChoiceField(Universos)

#Práctica 10: Formularios mecanicos
class Musicos_FormMecanico(forms.Form):
    Piano = 'Piano'
    Violin = 'Violin'
    instrumentos = {
        (Piano, 'Piano'),
        (Violin, 'Violin'),
    }

    nombre = forms.CharField(max_length = 35)
    edad = forms.IntegerField()
    instrumento = forms.ChoiceField(instrumentos)
    concursosGanados = forms.IntegerField()

#Páctica 12: SignUp
class User_Form(UserCreationForm):
    telefono = forms.CharField(max_length=10)
    correo = forms.CharField(max_length=50)
