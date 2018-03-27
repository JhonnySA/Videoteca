from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView, UpdateView, DeleteView

from ..formstotal.pelicula import PeliculaForm
from ..tables.listapelicula import TablaListaPelicula
from ..models import *


class PeliculaVista(TemplateView):
    template_name = "pelicula/pelicula.html"

    def render_to_response(self, context, **response_kwargs):
        context["tablaPelicula"] = TablaListaPelicula()
        return super(PeliculaVista, self).render_to_response(context, **response_kwargs)


class PeliculaAgregar(CreateView):
    template_name = "pelicula/formulario.html"
    model = Pelicula
    form_class = PeliculaForm

    def form_valid(self, form):
        super(PeliculaAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Creado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(PeliculaAgregar, self).form_invalid(form)
        return render(self.request, self.template_name, {"form": form})


class PeliculaEditar(UpdateView):
    template_name = "pelicula/formulario.html"
    model = Pelicula
    form_class = PeliculaForm

    def form_valid(self, form):
        super(PeliculaEditar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Actualizado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(PeliculaEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {"form": form})


class PeliculaEliminar(DeleteView):
    template_name = "pelicula/eliminar.html"
    model = Pelicula
    form_class = PeliculaForm

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
                          {'object': self.get_object(),'delete_error': str(e)})
        return JsonResponse(msg)
