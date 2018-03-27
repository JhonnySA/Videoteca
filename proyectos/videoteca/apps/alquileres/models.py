# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_bulk_update.manager import BulkUpdateManager
from ..inicio.models import *


# Create your models here.

class Alquiler(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fechaadd = models.DateField()
    fechadev = models.DateField()

    def __unicode__(self):
        return self.cliente.nombre + " - " + str(self.fechaadd) + " - " + str(self.fechadev)

    def get_absolute_url(self):
        return ""

    def Total(self):
        _total = 0
        for det in self.detallealquiler_set.all():
            _total += det.cantidad * det.formato.costo
        return _total

    def ListaPelicula(self):
        lista = ""
        for det in self.detallealquiler_set.all():
            lista += "-> %s (%s)" % (det.formato.pelicula.nombre, det.formato.nombre) + "\n"
        return lista

    class Meta:
        ordering = ["-id"]


class DetalleAlquiler(models.Model):
    alquiler = models.ForeignKey(Alquiler, on_delete=models.PROTECT)
    formato = models.ForeignKey(Formato, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()

    # objects = BulkUpdateManager()

    def __unicode__(self):
        return "\n\t" + "Cliente: " + self.alquiler.cliente.nombre + "\n\t" + "Formato: " + self.formato.nombre + "\n\t" + "Cantidad: " + str(
            self.cantidad)

    def get_absolute_url(self):
        return ""

    def Formato(self):
        return str(self.formato.id)

    def Cantidad(self):
        return str(self.cantidad)

    class Meta:
        ordering = ["id"]
