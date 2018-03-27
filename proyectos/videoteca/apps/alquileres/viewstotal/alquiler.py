from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render
from django.template import Context
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django_select2.views import AutoResponseView

from ..formstotal.alquiler import AlquilerForm
from ..models import Alquiler, DetalleAlquiler
from ..tables.alquiler import TablaAlquiler


class AlquilerVista(TemplateView):
    template_name = "alquiler/vista.html"

    def render_to_response(self, context, **response_kwargs):
        context["tablaAlquiler"] = TablaAlquiler()
        return super(AlquilerVista, self).render_to_response(context, **response_kwargs)


class AlquilerAgregar(CreateView):
    template_name = "alquiler/formulario.html"
    form_class = AlquilerForm
    model = Alquiler

    def form_valid(self, form):
        super(AlquilerAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Creado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(AlquilerAgregar, self).form_invalid(form)
        print(form.errors)
        return render(self.request, self.template_name, {"form": form})


class AlquilerEditar(UpdateView):
    template_name = "alquiler/formulario.html"
    model = Alquiler
    form_class = AlquilerForm
    context_object_name = "oAlquiler"

    def form_valid(self, form):
        super(AlquilerEditar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Actualizado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(AlquilerEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {"form": form})


class AlquilerEliminar(DeleteView):
    template_name = "alquiler/eliminar.html"
    model = Alquiler
    form_class = AlquilerForm

    def delete(self, request, *args, **kwargs):
        msg = {}
        msg["msg"] = "Eliminado correctamente"
        msg["value"] = True
        try:
            self.get_object().delete()
        except ProtectedError as e:
            msg["value"] = False
            return render(request, self.template_name,
                          {'object': self.get_object(), 'delete_error': "Este registro no puede ser eliminado"})
        except Exception as e:
            msg["value"] = False
            return render(request, self.template_name,
                          {'object': self.get_object(), 'delete_error': str(e)})
        return JsonResponse(msg)

class DetalleAlquilerFormatoCombo(AutoResponseView):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        self.widget=self.get_widget_or_404()
        self.term=kwargs.get('term', request.GET.get('term', ''))
        self.object_list=self.get_queryset()
        context = self.get_context_data()
        return JsonResponse({
            'results':[
                {
                    'text': self.widget.label_from_instance(obj),
                    'id': obj.pk,
                    'costo': obj.Costo()
                }
                for obj in context['object_list']
            ],
            'more': context['page_obj'].has_next()
        })