# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    nacimiento = models.DateField()

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return ""

    class Meta:
        ordering = ["-id"]


class TipoPelicula(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, default="", null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return ""

    class Meta:
        ordering = ["-id"]


class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    tipopelicula = models.ForeignKey(TipoPelicula, on_delete=models.PROTECT)
    actor = models.ForeignKey(Actor, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return ""

    class Meta:
        ordering = ["-id"]

    def Tipopelicula(self):
        return self.tipopelicula.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return ""

    class Meta:
        ordering = ["-id"]


class Formato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    pelicula = models.ForeignKey(Pelicula)
    costo = models.FloatField()

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return ""

    class Meta:
        ordering = ["-id"]

    def Costo(self):
        return self.costo;