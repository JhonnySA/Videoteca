from table import Table
from table.columns import Column

from apps.inicio.tables.tabladefecto import TablaDefecto
from ..models import Formato


class TablaFormato(TablaDefecto):
    nombre = Column(field="nombre", header="Nombre Formato")
    descripcion = Column(field="descripcion", header="Descripcion")
    pelicula = Column(field="pelicula.nombre", header="Pelicula")

    class Meta:
        model = Formato
        ajax = True
        id = "tablaFormato"
