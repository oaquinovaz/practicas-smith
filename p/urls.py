#Práctica 4: Views
from django.conf.urls import include, url
from . import views
#Páctica 11: Login
from django.contrib.auth.views import login, logout_then_login
#Páctica 12: SignUp
from .views import SignUp
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static

from Practicas import settings

from django.views.static import serve



urlpatterns = [
    #Práctica 4: Views
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),
    url(r'^anime/$', views.anime, name="anime"),
    url(r'^naruto/$', views.naruto, name="naruto"),
    url(r'^snk/$', views.snk, name="snk"),
    url(r'^dbs/$', views.dbs, name="dbs"),
    url(r'^swknu/$', views.swknu, name="swknu"),
    #Práctica 8: Formularios
    url(r'^formPracticas/$', views.formPracticas, name="formPracticas"),
    url(r'^formAnimes/$', views.formAnimes, name="formAnimes"),
    url(r'^formNaruto/$', views.formNaruto, name="formNaruto"),
    url(r'^formSNK/$', views.formSNK, name="formSNK"),
    url(r'^formDBS/$', views.formDBS, name="formDBS"),
    url(r'^formSWKNU/$', views.formSWKNU, name="formSWKNU"),
    #Práctica 9: Vistas basadas en clases
    url(r'^animes_list/$', views.Animes_List.as_view(), name="animes_list"),
    url(r'^ninjas_list/$', views.Ninjas_List.as_view(), name="ninjas_list"),
    url(r'^soldados_list/$', views.Soldados_List.as_view(), name="soldados_list"),
    url(r'^guerreros_list/$', views.Guerreros_List.as_view(), name="guerreros_list"),
    url(r'^musicos_list/$', views.Musicos_List.as_view(), name="musicos_list"),
    #Práctica 10: Formularios mecanicos
    url(r'^formMecanicoAnimes/$', views.formMecanicoAnimes, name="formMecanicoAnimes"),
    url(r'^formMecanicoNinjas/$', views.formMecanicoNinjas, name="formMecanicoNinjas"),
    url(r'^formMecanicoSoldados/$', views.formMecanicoSNK, name="formMecanicoSoldados"),
    url(r'^formMecanicoDBS/$', views.formMecanicoDBS, name="formMecanicoDBS"),
    url(r'^formMecanicoSWKNU/$', views.formMecanicoSWKNU, name="formMecanicoSWKNU"),
    #Páctica 11: Login
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    #Páctica 12: SignUp
    url(r'^signup/$', views.SignUp.as_view(), name="signup"),


    url(r'^accounts/', include ('allauth.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
