#Práctica 6: Modelos
from django.db import models
#Páctica 12: SignUp
from django.contrib.auth.models import User

#Práctica 6: Modelos
class Practicas(models.Model):
    practica = models.IntegerField()
    nombre = models.CharField(max_length = 75)
    realizado = models.BooleanField(default = False)

    def __str__(self):
        return self.nombre

#Práctica 22: Managers
class AccionManager(models.Manager):
    def get_queryset(self):
        return super(AccionManager, self).get_queryset().filter(genero='Accion')

class ArtesMarcialesManager(models.Manager):
    def get_queryset(self):
        return super(ArtesMarcialesManager, self).get_queryset().filter(genero='ArtesMarciales')

class ArtesMarcialesManager(models.Manager):
    def get_queryset(self):
        return super(ArtesMarcialesManager, self).get_queryset().filter(genero='ArtesMarciales')

class AventurasManager(models.Manager):
    def get_queryset(self):
        return super(AventurasManager, self).get_queryset().filter(genero='Aventuras')

class CarrerasManager(models.Manager):
    def get_queryset(self):
        return super(CarrerasManager, self).get_queryset().filter(genero='Carreras')

class CienciaFiccionManager(models.Manager):
    def get_queryset(self):
        return super(CienciaFiccionManager, self).get_queryset().filter(genero='CienciaFiccion')

class ComediaManager(models.Manager):
    def get_queryset(self):
        return super(ComediaManager, self).get_queryset().filter(genero='Comedia')

class DemenciaManager(models.Manager):
    def get_queryset(self):
        return super(DemenciaManager, self).get_queryset().filter(genero='Demencia')

class DemoniosManager(models.Manager):
    def get_queryset(self):
        return super(DemoniosManager, self).get_queryset().filter(genero='Demonios')

class DeportesManager(models.Manager):
    def get_queryset(self):
        return super(DeportesManager, self).get_queryset().filter(genero='Deportes')

class DramaManager(models.Manager):
    def get_queryset(self):
        return super(DramaManager, self).get_queryset().filter(genero='Drama')

class EcchiManager(models.Manager):
    def get_queryset(self):
        return super(EcchiManager, self).get_queryset().filter(genero='Ecchi')

class EscolaresManager(models.Manager):
    def get_queryset(self):
        return super(EscolaresManager, self).get_queryset().filter(genero='Escolares')

class EspacialManager(models.Manager):
    def get_queryset(self):
        return super(EspacialManager, self).get_queryset().filter(genero='Espacial')

class FantasiaManager(models.Manager):
    def get_queryset(self):
        return super(FantasiaManager, self).get_queryset().filter(genero='Fantasia')

class HaremManager(models.Manager):
    def get_queryset(self):
        return super(HaremManager, self).get_queryset().filter(genero='Harem')

class HistoricoManager(models.Manager):
    def get_queryset(self):
        return super(HistoricoManager, self).get_queryset().filter(genero='Historico')

class InfantilManager(models.Manager):
    def get_queryset(self):
        return super(InfantilManager, self).get_queryset().filter(genero='Infantil')

class JoseiManager(models.Manager):
    def get_queryset(self):
        return super(JoseiManager, self).get_queryset().filter(genero='Josei')

class JuegosManager(models.Manager):
    def get_queryset(self):
        return super(JuegosManager, self).get_queryset().filter(genero='Juegos')

class MagiaManager(models.Manager):
    def get_queryset(self):
        return super(MagiaManager, self).get_queryset().filter(genero='Magia')

class MechaManager(models.Manager):
    def get_queryset(self):
        return super(MechaManager, self).get_queryset().filter(genero='Mecha')

class MilitarManager(models.Manager):
    def get_queryset(self):
        return super(MilitarManager, self).get_queryset().filter(genero='Militar')

class MisterioManager(models.Manager):
    def get_queryset(self):
        return super(MisterioManager, self).get_queryset().filter(genero='Misterio')

class MusicaManager(models.Manager):
    def get_queryset(self):
        return super(MusicaManager, self).get_queryset().filter(genero='Musica')

class ParodiaManager(models.Manager):
    def get_queryset(self):
        return super(ParodiaManager, self).get_queryset().filter(genero='Parodia')

class PoliciaManager(models.Manager):
    def get_queryset(self):
        return super(PoliciaManager, self).get_queryset().filter(genero='Policia')

class PsicologicoManager(models.Manager):
    def get_queryset(self):
        return super(PsicologicoManager, self).get_queryset().filter(genero='Psicologico')

class RecuentrosdelavidaManager(models.Manager):
    def get_queryset(self):
        return super(RecuentrosdelavidaManager, self).get_queryset().filter(genero='Recuentrosdelavida')

class RomanceManager(models.Manager):
    def get_queryset(self):
        return super(RomanceManager, self).get_queryset().filter(genero='Romance')

class SamuraiManager(models.Manager):
    def get_queryset(self):
        return super(SamuraiManager, self).get_queryset().filter(genero='Samurai')

class SeinenManager(models.Manager):
    def get_queryset(self):
        return super(SeinenManager, self).get_queryset().filter(genero='Seinen')

class ShoujoManager(models.Manager):
    def get_queryset(self):
        return super(ShoujoManager, self).get_queryset().filter(genero='Shoujo')

class ShounenManager(models.Manager):
    def get_queryset(self):
        return super(ShounenManager, self).get_queryset().filter(genero='Shounen')

class SobrenaturalManager(models.Manager):
    def get_queryset(self):
        return super(SobrenaturalManager, self).get_queryset().filter(genero='Sobrenatural')

class SuperpoderesManager(models.Manager):
    def get_queryset(self):
        return super(SuperpoderesManager, self).get_queryset().filter(genero='Superpoderes')

class SuspensoManager(models.Manager):
    def get_queryset(self):
        return super(SuspensoManager, self).get_queryset().filter(genero='Suspenso')

class TerrorManager(models.Manager):
    def get_queryset(self):
        return super(TerrorManager, self).get_queryset().filter(genero='Terror')

class VampirosManager(models.Manager):
    def get_queryset(self):
        return super(VampirosManager, self).get_queryset().filter(genero='Vampiros')

class YaoiManager(models.Manager):
    def get_queryset(self):
        return super(YaoiManager, self).get_queryset().filter(genero='Yaoi')

class YuriManager(models.Manager):
    def get_queryset(self):
        return super(YuriManager, self).get_queryset().filter(genero='Yuri')

#Práctica 6: Modelos
class Animes(models.Model):
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

    nombre = models.CharField(max_length = 50)
    genero = models.CharField(max_length = 21, choices = generos)
    episodios = models.IntegerField()
    añoLanzamiento = models.DateTimeField(blank = True, null = True)

    #Práctica 22: Managers
    objects = models.Manager()
    Accion_objects = AccionManager()
    ArtesMarciales_objects = ArtesMarcialesManager()
    Aventuras_objects = AventurasManager()
    Carreras_objects = CarrerasManager()
    CienciaFiccion_objects = CienciaFiccionManager()
    Comedia_objects = ComediaManager()
    Demencia_objects = DemenciaManager()
    Demonios_objects = DemoniosManager()
    Deportes_objects = DeportesManager()
    Drama_objects = DramaManager()
    Ecchi_objects = EcchiManager()
    Escolares_objects = EscolaresManager()
    Espacial_objects = EspacialManager()
    Fantasia_objects = FantasiaManager()
    Harem_objects = HaremManager()
    Historico_objects = HistoricoManager()
    Infantil_objects = InfantilManager()
    Josei_objects = JoseiManager()
    Juegos_objects = JuegosManager()
    Magia_objects = MagiaManager()
    Mecha_objects = MechaManager()
    Militar_objects = MilitarManager()
    Misterio_objects = MisterioManager()
    Musica_objects = MusicaManager()
    Parodia_objects = ParodiaManager()
    Policia_objects = PoliciaManager()
    Psicologico_objects = PsicologicoManager()
    Recuentrosdelavida_objects = RecuentrosdelavidaManager()
    Romance_objects = RomanceManager()
    Samurai_objects = SamuraiManager()
    Seinen_objects = SeinenManager()
    Shoujo_objects = ShoujoManager()
    Shounen_objects = ShounenManager()
    Sobrenatural_objects = SobrenaturalManager()
    Superpoderes_objects = SuperpoderesManager()
    Suspenso_objects = SuspensoManager()
    Terror_objects = TerrorManager()
    Vampiros_objects = VampirosManager()
    Yaoi_objects = YaoiManager()
    Yuri_objects = YuriManager()

    def __str__(self):
        return self.nombre

#Práctica 22: Managers
class GeninManager(models.Manager):
    def get_queryset(self):
        return super(GeninManager, self).get_queryset().filter(nivelMilitar='Genin')

class ChuninManager(models.Manager):
    def get_queryset(self):
        return super(ChuninManager, self).get_queryset().filter(nivelMilitar='Chunin')

class JoninManager(models.Manager):
    def get_queryset(self):
        return super(JoninManager, self).get_queryset().filter(nivelMilitar='Jonin')

class AnbuManager(models.Manager):
    def get_queryset(self):
        return super(AnbuManager, self).get_queryset().filter(nivelMilitar='Anbu')

class SanninManager(models.Manager):
    def get_queryset(self):
        return super(SanninManager, self).get_queryset().filter(nivelMilitar='Sannin')

class KageManager(models.Manager):
    def get_queryset(self):
        return super(KageManager, self).get_queryset().filter(nivelMilitar='Kage')

#Práctica 6: Modelos
class Ninjas(models.Model):
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

    nombre = models.CharField(max_length = 35)
    clan = models.CharField(max_length = 35)
    aldea = models.CharField(max_length = 35)
    nivelMilitar = models.CharField(max_length = 6, choices = nvlMil)
    jutsu = models.CharField(max_length = 50)
    nivelChakra = models.FloatField()

    #Práctica 22: Managers
    objects = models.Manager()
    Genin_objects = GeninManager()
    Chunin_objects = ChuninManager()
    Jonin_objects = JoninManager()
    Anbu_objects = AnbuManager()
    Sannin_objects = SanninManager()
    Kage_objects = KageManager()

    def __str__(self):
        return self.nombre

#Práctica 22: Managers
class ReconocimientoManager(models.Manager):
    def get_queryset(self):
        return super(ReconocimientoManager, self).get_queryset().filter(ejercito='Reconocimiento')

class EstacionariasManager(models.Manager):
    def get_queryset(self):
        return super(EstacionariasManager, self).get_queryset().filter(ejercito='Estacionarias')

class PoliciaManager(models.Manager):
    def get_queryset(self):
        return super(PoliciaManager, self).get_queryset().filter(ejercito='Policia')

#Práctica 6: Modelos
class EjercitoDeLasMurallas(models.Model):
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

    nombre = models.CharField(max_length = 35)
    distrito = models.CharField(max_length = 35)
    muralla = models.CharField(max_length = 13, choices = Murallas)
    ejercito = models.CharField(max_length = 24, choices = EjecitoMuralla)
    gigantesAsesinados = models.IntegerField()

    #Práctica 22: Managers
    objects = models.Manager()
    Reconocimiento_objects = ReconocimientoManager()
    Estacionarias_objects = EstacionariasManager()
    Policia_objects = PoliciaManager()

    def __str__(self):
        return self.nombre

#Práctica 22: Managers
class Universo1Manager(models.Manager):
    def get_queryset(self):
        return super(Universo1Manager, self).get_queryset().filter(universo='1')

class Universo2Manager(models.Manager):
    def get_queryset(self):
        return super(Universo2Manager, self).get_queryset().filter(universo='2')

class Universo3Manager(models.Manager):
    def get_queryset(self):
        return super(Universo3Manager, self).get_queryset().filter(universo='3')

class Universo4Manager(models.Manager):
    def get_queryset(self):
        return super(Universo4Manager, self).get_queryset().filter(universo='4')

class Universo5Manager(models.Manager):
    def get_queryset(self):
        return super(Universo5Manager, self).get_queryset().filter(universo='5')

class Universo6Manager(models.Manager):
    def get_queryset(self):
        return super(Universo6Manager, self).get_queryset().filter(universo='6')

class Universo7Manager(models.Manager):
    def get_queryset(self):
        return super(Universo7Manager, self).get_queryset().filter(universo='7')

class Universo8Manager(models.Manager):
    def get_queryset(self):
        return super(Universo8Manager, self).get_queryset().filter(universo='8')

class Universo9Manager(models.Manager):
    def get_queryset(self):
        return super(Universo9Manager, self).get_queryset().filter(universo='9')

class Universo10Manager(models.Manager):
    def get_queryset(self):
        return super(Universo10Manager, self).get_queryset().filter(universo='10')

class Universo11Manager(models.Manager):
    def get_queryset(self):
        return super(Universo11Manager, self).get_queryset().filter(universo='11')

class Universo12Manager(models.Manager):
    def get_queryset(self):
        return super(Universo12Manager, self).get_queryset().filter(universo='12')


#Práctica 6: Modelos
class GuerrerosZ(models.Model):
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

    nombre = models.CharField(max_length = 35)
    raza = models.CharField(max_length = 20)
    nivelKi = models.FloatField()
    transformacionMasPoderosa = models.CharField(max_length = 30, null = True)
    habilidadEspecial = models.CharField(max_length = 30)
    planetaOrigen = models.CharField(max_length = 20)
    universo = models.CharField(max_length = 2, choices = Universos)

    #Práctica 22: Managers
    objects = models.Manager()
    Universo1_objects = Universo1Manager()
    Universo2_objects = Universo2Manager()
    Universo3_objects = Universo3Manager()
    Universo4_objects = Universo4Manager()
    Universo5_objects = Universo5Manager()
    Universo6_objects = Universo6Manager()
    Universo7_objects = Universo7Manager()
    Universo8_objects = Universo8Manager()
    Universo9_objects = Universo9Manager()
    Universo10_objects = Universo10Manager()
    Universo11_objects = Universo11Manager()
    Universo12_objects = Universo12Manager()

    def __str__(self):
        return self.nombre

#Práctica 22: Managers
class PianoManager(models.Manager):
    def get_queryset(self):
        return super(PianoManager, self).get_queryset().filter(instrumento='Piano')

class ViolinManager(models.Manager):
    def get_queryset(self):
        return super(ViolinManager, self).get_queryset().filter(instrumento='Violin')

#Práctica 6: Modelos
class Musicos(models.Model):
    Piano = 'Piano'
    Violin = 'Violin'
    instrumentos = {
        (Piano, 'Piano'),
        (Violin, 'Violin'),
    }

    nombre = models.CharField(max_length = 35)
    edad = models.IntegerField()
    instrumento = models.CharField(max_length = 6, choices = instrumentos)
    concursosGanados = models.IntegerField()

    #Práctica 22: Managers
    objects = models.Manager()
    Piano_objects = PianoManager()
    Violin_objects = ViolinManager()

    def __str__(self):
        return self.nombre

#Páctica 12: SignUp
class Usuarios(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
