# coding=utf-8
from django import forms

from ..models import Cliente


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " form-control"
        self.fields["direccion"].label = "Dirección"
        self.fields["telefono"].label = "Teléfono"

    class Meta:
        model = Cliente
        fields = ["nombre", "direccion", "telefono"]
