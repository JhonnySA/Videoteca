from django.urls import reverse
from table.columns import Column

from ..models import Actor
from ..tables.tabladefecto import TablaDefecto


class AccionColumn(Column):

    # Version de column para cada tabla

    def render(self, obj):
        _result = ""
        # Boton Editar
        urlEditar = reverse(viewname="inicio:actor_editar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Editar' href='" + urlEditar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-pencil'></i></button>&nbsp;"

        # Boton Eliminar
        urlEliminar = reverse(viewname="inicio:actor_eliminar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Eliminar' href='" + urlEliminar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-trash'></i></button>"
        return _result


class TablaActor(TablaDefecto):
    nombre = Column(field="nombre", header="Nombre Actor")
    nacimiento = Column(field="nacimiento", header="Fecha Nacimiento")
    columnaA = AccionColumn(field="pk", header="Acciones")

    class Meta(TablaDefecto.Meta):
        model = Actor
        ajax = True
        id = "tablaActor"
