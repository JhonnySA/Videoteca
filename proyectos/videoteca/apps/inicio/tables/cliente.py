from django.urls import reverse
from table import Table
from table.columns import Column

from apps.inicio.models import Cliente
from .tabladefecto import TablaDefecto, ColumnDefecto

class AccionColumn(Column):

    # Version de column para cada tabla

    def render(self, obj):
        _result = ""
        #Boton Editar
        urlEditar = reverse(viewname="inicio:cliente_editar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Editar' href='" + urlEditar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-pencil'></i></button>&nbsp;"

        # Boton Eliminar
        urlEliminar = reverse(viewname="inicio:cliente_eliminar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Eliminar' href='" + urlEliminar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-trash'></i></button>"
        return _result



class TablaCliente(TablaDefecto):
    nombre = Column(field="nombre", header="Nombre")
    direccion = Column(field="direccion", header="Direccion")
    telefono = Column(field="telefono", header="Telefono")
    columnaA = AccionColumn(field="pk", header="Acciones")

    class Meta(TablaDefecto.Meta):
        model = Cliente
        ajax = True
        id = "tablaCliente"
