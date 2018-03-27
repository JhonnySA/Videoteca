from django import forms

from ..models import TipoPelicula


class TipoPeliculaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TipoPeliculaForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " form-control"

    class Meta:
        model = TipoPelicula
        fields = ["nombre", "descripcion"]
