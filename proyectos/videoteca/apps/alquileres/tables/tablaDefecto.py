from table import Table


class TablaDefecto(Table):
    class Meta:
        ajax = True
        template_name = "tabla.html"
        attrs = {
            "style": 'background-color: #91E2EB; width: 100%',
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