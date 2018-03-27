"""videoteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# Probando las URls (estas las definen como patrones)
from apps.alquileres.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^table/', include("table.urls")),
    url(r'^select2/', include('django_select2.urls')),

    url(r'^inicio/', include("apps.inicio.urls", namespace="inicio")),
    url(r'^alquileres/', include("apps.alquileres.urls", namespace="alquileres"))
    # url(r'^time/', form_inicio()),
    # url(r'', actor),
    # url(r'^post/(?P<pk>[0-9]+)/$', actor_detail),
    # url(r'^actores/$', ListadoActores, name="listado_actores"),
    # url(r'^crear_actores/$', CrearActores, name="crear_actores"),
    # url(r'^modificar_actores/(?P<pk>.+)/$', ActualizarActores, name="modificar_actores"),
    # url(r'^detalle_actores/(?P<pk>.+)/$', DetalleActores, name="detalle_actores"),
]
