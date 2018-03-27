import itertools

from django.urls import reverse
from table import Table
from table.columns import Column

from .tabladefecto import TablaDefecto, ColumnDefecto
from ..models import *


# Esto puede personalizarse haciendose igual que la TableDefecto

class AccionColumn(Column):

    # Version de column para cada tabla

    def render(self, obj):
        _result = ""
        #Boton Editar
        urlEditar = reverse(viewname="inicio:pelicula_editar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Editar' href='" + urlEditar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-pencil'></i></button>&nbsp;"

        # Boton Eliminar
        urlEliminar = reverse(viewname="inicio:pelicula_eliminar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Eliminar' href='" + urlEliminar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-trash'></i></button>"
        return _result


class TablaListaPelicula(TablaDefecto):
    nombre = Column(field="nombre", header="Nombre de la pelicula")
    tipopelicula = Column(field="tipopelicula.nombre", header="Tipo de pelicula")
    actor = Column(field="actor.nombre", header="Actor principal")
    columnaA = AccionColumn(field="pk", header="Acciones")

    class Meta(TablaDefecto.Meta):
        model = Pelicula
        id = "tablaPelicula"
