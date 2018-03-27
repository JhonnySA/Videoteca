# coding=utf-8
from django.urls import reverse
from table import Table
from table.columns import Column

from ..tables.tabladefecto import TablaDefecto
from ..models import TipoPelicula


class AccionColumn(Column):

    # Version de column para cada tabla

    def render(self, obj):
        _result = ""
        # Boton Editar
        urlEditar = reverse(viewname="inicio:tipopelicula_editar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Editar' href='" + urlEditar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-pencil'></i></button>&nbsp;"

        # Boton Eliminar
        urlEliminar = reverse(viewname="inicio:tipopelicula_eliminar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Eliminar' href='" + urlEliminar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-trash'></i></button>"
        return _result


class TablaTipoPelicula(TablaDefecto):
    nombre = Column(field="nombre", header="Nombre")
    descripcion = Column(field="descripcion", header="Descripción")
    columnaA = AccionColumn(field="pk", header="Acciones")

    class Meta:
        model = TipoPelicula
        ajax = True
        id = "tablaTipoPelicula"
