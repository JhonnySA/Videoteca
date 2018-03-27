# coding=utf-8
from django.urls import reverse
from table.columns import Column

from apps.alquileres.models import Alquiler
from ..tables.tablaDefecto import TablaDefecto


class AccionColumn(Column):
    def render(self, obj):
        _result = ""
        # Boton Editar
        urlEditar = reverse(viewname="alquileres:alquiler_editar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Editar' href='" + urlEditar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-pencil'></i></button>&nbsp;"

        # Boton Eliminar
        urlEliminar = reverse(viewname="alquileres:alquiler_eliminar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Eliminar' href='" + urlEliminar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-trash'></i></button>"
        return _result


class columnTotal(Column):
    def render(self, obj):
        return obj.Total()


class ColumnLista(Column):
    def render(self, obj):
        return obj.ListaPelicula()


class TablaAlquiler(TablaDefecto):
    cliente = Column(field="cliente.nombre", header="Nombre Cliente")
    fechaadd = Column(field="fechaadd", header="Fecha Adquisición")
    fechadev = Column(field="fechadev", header="Fecha Devolución")
    lista = ColumnLista(field="pk", header="Lista Peliculas")
    total = columnTotal(field="pk", header="Total")
    columnaA = AccionColumn(field="pk", header="Acciones", attrs={"class": "text-right"})

    class Meta(TablaDefecto.Meta):
        model = Alquiler
        id = "tablaAlquiler"