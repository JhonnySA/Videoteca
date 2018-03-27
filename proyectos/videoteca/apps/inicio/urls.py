# coding=utf-8
from django.conf.urls import url

from .viewstotal.actor import *
from .viewstotal.formato import *
from .viewstotal import formato
from .viewstotal.cliente import *
from .viewstotal.tipopelicula import *
from .viewstotal.pelicula import *
from .viewstotal.inicio import *

urlpatterns = [
    url(r'^$', Inicio.as_view(), name="inicio"),

    # Tipos de Películas
    url(r'tipopelicula/$', TipoPeliculaVista.as_view(), name="tipopelicula_vista"),
    url(r'tipopelicula/agregar/$', TipoPeliculaAgregar.as_view(), name="tipopelicula_agregar"),
    url(r'tipopelicula/editar/(?P<pk>\d+)$', TipoPeliculaEditar.as_view(), name="tipopelicula_editar"),
    url(r'tipopelicula/eliminar/(?P<pk>\d+)$', TipoPeliculaEliminar.as_view(), name="tipopelicula_eliminar"),

    # Peliculas
    url(r'pelicula/$', PeliculaVista.as_view(), name="pelicula_vista"),
    url(r'pelicula/agregar$', PeliculaAgregar.as_view(), name="pelicula_agregar"),
    url(r'pelicula/editar/(?P<pk>\d+)$', PeliculaEditar.as_view(), name="pelicula_editar"),
    url(r'pelicula/eliminar/(?P<pk>\d+)$', PeliculaEliminar.as_view(), name="pelicula_eliminar"),

    # Cliente
    url(r'cliente/$', ClienteVista.as_view(), name="cliente_vista"),
    url(r'cliente/agregar/$', ClienteAgregar.as_view(), name="cliente_agregar"),
    url(r'cliente/editar/(?P<pk>\d+)$', ClienteEditar.as_view(), name="cliente_editar"),
    url(r'cliente/eliminar/(?P<pk>\d+)$', ClienteEliminar.as_view(), name="cliente_eliminar"),

    # Formato
    url(r'formato/$', formato.FormatoVista.as_view(), name="formato_vista"),
    url(r'formato/agregar/$', FormatoAgregar.as_view(), name="formato_agregar"),

    # Actor
    url(r'actor/$', ActorVista.as_view(), name="actor_vista"),
    url(r'actor/agregar/$', ActorAgregar.as_view(), name="actor_agregar"),
    url(r'actor/editar/(?P<pk>\d+)$', ActorEditar.as_view(), name="actor_editar"),
    url(r'actor/eliminar/(?P<pk>\d+)$', ActorEliminar.as_view(), name="actor_eliminar"),
]
