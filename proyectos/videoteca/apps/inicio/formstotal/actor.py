from django import forms

from apps.inicio.models import Actor


class ActorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActorForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " form-control"

    class Meta:
        model = Actor
        fields = ["nombre", "nacimiento"]
