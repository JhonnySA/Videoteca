# coding=utf-8
from django import forms
from django_select2.forms import ModelSelect2Widget

from ..models import Pelicula, Actor, TipoPelicula


class PeliculaForm(forms.ModelForm):
    # choice oociones fijas (sexo [H,M])
    # Model Choice Field, cuando viene de un modelo

    tipopelicula = forms.ModelChoiceField(
        required=True,
        queryset=TipoPelicula.objects.all(),
        label="Tipo de Película",
        widget=ModelSelect2Widget(
            queryset=TipoPelicula.objects.order_by("nombre"),
            search_fields=["nombre__icontains"],
            max_results=10,
        )
    )

    actor = forms.ModelChoiceField(
        required=True,
        queryset=Actor.objects.all(),
        label="Actor",
        widget=ModelSelect2Widget(
            queryset=Actor.objects.order_by("nombre"),
            search_fields=["nombre__icontains"],
            max_results=10,
        )
    )

    def __init__(self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " form-control"

    class Meta:
        model = Pelicula
        fields = ["nombre", "tipopelicula", "actor"]
