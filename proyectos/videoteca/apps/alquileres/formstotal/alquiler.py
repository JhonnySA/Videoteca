from datetime import datetime
from datetimewidget.widgets import DateWidget
from django import forms
from django_bulk_update.helper import bulk_update
from django_select2.forms import ModelSelect2Widget

from apps.alquileres.models import Alquiler, DetalleAlquiler
from apps.inicio.models import Cliente, Pelicula, Formato


# Clase para capturar los ids_formatos a exlcluir


class peliculaWidget(ModelSelect2Widget):
    queryset = Pelicula.objects.filter(id__in=Formato.objects.all().values_list("pelicula_id")).order_by("nombre")
    search_fields = ["nombre__icontains", "tipopelicula__nombre__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return "%s (%s)" % (obj.nombre, obj.tipopelicula.nombre)


class AlquilerForm(forms.ModelForm):
    pelicula = forms.ModelChoiceField(
        required=True,
        queryset=Pelicula.objects.filter(
            id__in=Formato.objects.all().values_list('pelicula_id')).order_by("nombre"),
        label="Pelicula",
        widget=peliculaWidget(
            attrs={'id': 'cbPelicula'}
        )
    )

    formato = forms.ModelChoiceField(
        required=True,
        queryset=Formato.objects.all(),
        label="Formato",
        widget=ModelSelect2Widget(
            queryset=Formato.objects.order_by("nombre"),
            search_fields=["nombre__icontains"],
            dependent_fields={'pelicula': 'pelicula'},
            max_results=10,
            data_view='alquileres:formato_combo',
            attrs={'id': 'cbFormato'},
        )
    )

    cliente = forms.ModelChoiceField(
        required=True,
        queryset=Cliente.objects.all(),
        label="Cliente",
        widget=ModelSelect2Widget(
            queryset=Cliente.objects.order_by("nombre"),
            search_fields="nombre__icontains",
            max_results=10,
            attrs={'id': 'cbcliente'}
        )
    )

    cantidad = forms.FloatField(min_value=1, initial=1)

    costo = forms.FloatField(disabled=True, required=False, widget=forms.NumberInput(
        attrs={'id': 'txtCosto'}
    ))

    detalle = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"id": "detalle"}), required=False)

    fechaadd = forms.DateField(
        input_formats=["%d/%m/%Y"],
        initial=datetime.now().date(),
        widget=DateWidget(
            attrs={'id': "fechaadd", "data-datepicker-type": "4", "data-provider": "datepicker-inline"},
            # usel10n=True,
            bootstrap_version=3,
            options={
                "format": "dd/mm/yyyy",
                # "startView": "2",
                "autoclose": "true",
                "language": "es",
                "fontAwesome": "true",
                # "todayBtn": "true",
                "clearBtn": "false"
            }
        )
    )

    fechadev = forms.DateField(
        input_formats=["%d/%m/%Y"],
        initial=datetime.now().date(),
        widget=DateWidget(
            attrs={'id': "fechaadd", "data-datepicker-type": "4", "data-provider": "datepicker-inline"},
            # usel10n=True,
            bootstrap_version=3,
            options={
                "format": "dd/mm/yyyy",
                # "startView": "2",
                "autoclose": "true",
                "language": "es",
                "fontAwesome": "true",
                # "todayBtn": "true",
                "clearBtn": "false"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(AlquilerForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " form-control"

    class Meta:
        model = Alquiler
        fields = ["cliente", "fechaadd", "fechadev", "detalle"]

    # Tuve que modificar el save de bulk_create para poder actualizar

    def save(self, commit=True):
        alquiler = super(AlquilerForm, self).save(commit=True)

        # Grabamos el detalle

        # Capturar el detalle que se solicita
        detalle = self.cleaned_data["detalle"].split("//")

        # Capturar lista de detalle
        lista_detalle = Alquiler.objects.get(id=alquiler.pk).detallealquiler_set.all()

        detAlq = []
        ids_formatos = []
        ids_actualizados = []

        for reg in detalle:
            if len(reg) > 0:
                regs = reg.split("/")
                formato = int(regs[0])
                cantidad = int(regs[1])
                costo = float(regs[2])
                detAlq.append(
                    DetalleAlquiler(
                        alquiler=alquiler,
                        formato_id=formato,
                        cantidad=cantidad
                    )
                )
                ids_formatos.append(
                    formato
                )

        # Lista eliminados[], actualizados[], nuevos[], ids_formatos[] (excluir los que se removieron de la tabla)
        eliminados = []
        actualizados = []
        nuevos = []

        # Preguntar de la lista de detalle quienes no estan en la BD
        # A esos se tiene k eliminar y agregar a la lista de eliminados

        excluidos = DetalleAlquiler.objects.filter(alquiler=alquiler.pk).exclude(formato_id__in=ids_formatos)

        for exc in excluidos:
            eliminados.append(exc.formato_id)

        print("IdsFormatos")
        print(len(ids_formatos))
        print("ELiminados")
        print(len(eliminados))

        # Traer la lista de nuevos
        for id in detAlq:
            if lista_detalle.filter(formato_id=id.formato_id).exists() and lista_detalle.get(
                    formato_id=id.formato_id).cantidad != id.cantidad:
                actualizados.append(id)
                ids_actualizados.append(id.formato_id)
            elif not lista_detalle.filter(formato_id=id.formato_id).exists():
                nuevos.append(id)

        print("Actualizados")
        print(len(actualizados))
        print(actualizados)
        print("Nuevos")
        print(len(nuevos))
        print(nuevos)

        # Eliminacion masiva
        if len(eliminados) > 0:
            lista_detalle.filter(formato_id__in=eliminados).delete();

        # Actualizacion masiva
        if len(ids_actualizados) > 0:
            list_actualizados = lista_detalle.filter(formato_id__in=ids_actualizados)

            contador = 0
            for item in list_actualizados:
                item.cantidad = actualizados[contador].cantidad
                contador += 1
            bulk_update(list_actualizados, update_fields=['cantidad'])

        # Creacion masiva
        if len(nuevos) > 0:
            DetalleAlquiler.objects.bulk_create(nuevos)
        return alquiler
