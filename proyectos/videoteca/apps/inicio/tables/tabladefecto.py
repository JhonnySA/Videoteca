from django.urls import reverse
from table import Table
from table.columns import Column


class TablaDefecto(Table):
    class Meta:
        ajax = True
        template_name = "tabla.html"
        attrs = {
            "style": 'background-color: #fff; width: 100%',
            "class": 'table-bordered table-striped table-hover dt-responsive',
            "width": '100%'
        }
        pagination = True
        pagination_firts = "<<"
        pagination_prev = "<"
        pagination_next = ">"
        pagination_last = ">>"
        search_placeholder = "Buscar"
        zero_records = "Ningun registro"


# Esta clase se puede mejorar si se recibe parametros como URLS opcionales, en caso de recibir un update crea
# el boton UPDATE, etc

class ColumnDefecto(Column):
    def render(self, obj):
        _result = ""

        # Boton Editar
        urlEditar = reverse(viewname="inicio:pelicula_editar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Editar' href='" + urlEditar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-pencil'></i></button>&nbsp;"
        # Boton Eliminar
        urlEliminar = reverse(viewname="inicio:pelicula_eliminar", kwargs={"pk": obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Eliminar' href='" + urlEliminar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-trash'></i></button>"
        #
        return _result
