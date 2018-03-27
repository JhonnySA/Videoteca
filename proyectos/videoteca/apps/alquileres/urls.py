from django.conf.urls import url

from .viewstotal.alquiler import *
from .viewstotal.alquileres import *

urlpatterns = [
    url(r'^$', Alquileres.as_view(), name="alquileres"),

    # Alquiler
    url(r'^alquiler/$', AlquilerVista.as_view(), name="alquiler_vista"),
    url(r'^alquiler/agregar$', AlquilerAgregar.as_view(), name="alquiler_agregar"),
    url(r'alquiler/editar/(?P<pk>\d+)$', AlquilerEditar.as_view(), name="alquiler_editar"),
    url(r'alquiler/eliminar/(?P<pk>\d+)$', AlquilerEliminar.as_view(), name="alquiler_eliminar"),

    # URL Personalizadda para traer el costo del formato y reseetearlo cada vez que se cambia de opcion de combo
    url(r'^detallealquiler/formatocombo$', DetalleAlquilerFormatoCombo.as_view(), name="formato_combo"),
]
