from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from pip import req

from ..formstotal.cliente import ClienteForm
from ..tables.cliente import TablaCliente
from ..models import Cliente


class ClienteVista(TemplateView):
    template_name = "cliente/vista.html"

    def render_to_response(self, context, **response_kwargs):
        context["TablaCliente"] = TablaCliente()
        return super(ClienteVista, self).render_to_response(context, **response_kwargs)


class ClienteAgregar(CreateView):
    template_name = "cliente/formulario.html"
    model = Cliente
    form_class = ClienteForm

    def form_valid(self, form):
        super(ClienteAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Creado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(ClienteAgregar, self).form_invalid(form)
        return render(self.request, self.template_name, {"form": form})


class ClienteEditar(UpdateView):
    template_name = "cliente/formulario.html"
    model = Cliente
    form_class = ClienteForm

    def form_valid(self, form):
        super(ClienteEditar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Actualizado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(ClienteEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {"form": form})


class ClienteEliminar(DeleteView):
    template_name = "cliente/eliminar.html"
    model = Cliente
    form_class = ClienteForm

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
