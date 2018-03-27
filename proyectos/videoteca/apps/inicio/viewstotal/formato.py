from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from ..formstotal.formato import FormatoForm
from ..models import Formato
from ..tables.formato import TablaFormato


class FormatoVista(TemplateView):
    template_name = 'formato/vista.html'
    
    def render_to_response(self, context, **response_kwargs):
        context["TablaFormato"] = TablaFormato()
        return super(FormatoVista, self).render_to_response(context, **response_kwargs)

class FormatoAgregar(CreateView):
    template_name = "formato/formulario.html"
    model = Formato
    form_class = FormatoForm

    def form_valid(self, form):
        super(FormatoAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Creado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(FormatoAgregar, self).form_invalid(form)
        return render(self.request, self.template_name, {"form": form})
