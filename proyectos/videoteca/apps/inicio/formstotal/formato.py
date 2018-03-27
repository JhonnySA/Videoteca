# coding=utf-8
from django import forms
from django_select2.forms import ModelSelect2Widget

from ..models import Formato, Pelicula


class peliculaWidget(ModelSelect2Widget):
    queryset = Pelicula.objects.all()
    search_fields = ["nombre__icontains"]

    def label_from_instance(self, obj):
        return "%s (%s)" % (obj.nombre, obj.actor.nombre)


class FormatoForm(forms.ModelForm):
    pelicula = forms.ModelChoiceField(
        required=True,
        queryset=Pelicula.objects.all(),
        widget=peliculaWidget(
            attrs={'id': "cbPelicula"}
        )
    )

    def __init__(self, *args, **kwargs):
        super(FormatoForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " form-control"
        self.fields["descripcion"].label = "Descripción"
        self.fields["pelicula"].label = "Película"

    class Meta:
        model = Formato
        fields = ["nombre", "descripcion", "pelicula"]
