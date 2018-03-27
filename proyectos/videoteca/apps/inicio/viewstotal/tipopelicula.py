from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from ..formstotal.tipopelicula import TipoPeliculaForm
from ..models import TipoPelicula
from ..tables.tipopelicula import TablaTipoPelicula


class TipoPeliculaVista(TemplateView):
    template_name = "tipopelicula/vista.html"

    def render_to_response(self, context, **response_kwargs):
        context["TablaTipoPelicula"] = TablaTipoPelicula()
        return super(TipoPeliculaVista, self).render_to_response(context, **response_kwargs)


class TipoPeliculaAgregar(CreateView):
    template_name = "tipopelicula/formulario.html"
    model = TipoPelicula
    form_class = TipoPeliculaForm

    def form_valid(self, form):
        super(TipoPeliculaAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Creado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(TipoPeliculaAgregar, self).form_invalid(form)
        return render(self.request, self.template_name, {"form": form})


class TipoPeliculaEditar(UpdateView):
    template_name = "tipopelicula/formulario.html"
    model = TipoPelicula
    form_class = TipoPeliculaForm

    def form_valid(self, form):
        super(TipoPeliculaEditar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Actualizado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(TipoPeliculaEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {"form": form})


class TipoPeliculaEliminar(DeleteView):
    template_name = "tipopelicula/eliminar.html"
    model = TipoPelicula
    form_class = TipoPeliculaForm

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
