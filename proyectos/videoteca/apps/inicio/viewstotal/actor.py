from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from apps.inicio.tables.actor import TablaActor
from ..formstotal.actor import ActorForm
from ..models import Actor
from ..tables.cliente import TablaCliente


class ActorVista(TemplateView):
    template_name = "actor/vista.html"

    def render_to_response(self, context, **response_kwargs):
        context["TablaActor"] = TablaActor()
        return super(ActorVista, self).render_to_response(context, **response_kwargs)


class ActorAgregar(CreateView):
    template_name = "actor/formulario.html"
    model = Actor
    form_class = ActorForm

    def form_valid(self, form):
        super(ActorAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Creado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(ActorAgregar, self).form_invalid(form)
        return render(self.request, self.template_name, {"form": form})


class ActorEditar(UpdateView):
    template_name = "actor/formulario.html"
    model = Actor
    form_class = ActorForm

    def form_valid(self, form):
        super(ActorEditar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Actualizado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(ActorEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {"form": form})


class ActorEliminar(DeleteView):
    template_name = "actor/eliminar.html"
    model = Actor
    form_class = ActorForm

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
