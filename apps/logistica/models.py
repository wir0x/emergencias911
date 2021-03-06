# encoding:utf-8
from django.db import models
from ..servicios.models import CentroEmergencia, Vehiculo
from django.contrib.auth.models import User

# Create your models here.

ESTADO_INCIDENTE = (
    ('NUEVO', 'NUEVO'),
    ('EN CURSO', 'EN CURSO (ASIGNADO)'),
    ('RESULTO', 'RESUELTO'),
    ('FINALIZADO', 'FINALIZADO'),
)

ESTADO_ASIGNACION = (
    ('EN CURSO', 'EN CURSO (ASIGNADO)'),
    ('RESULTO', 'RESUELTO'),
    ('FINALIZADO', 'FINALIZADO'),
)


class TipoIncidente(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name='Descripción')
    is_active = models.BooleanField(verbose_name='Activo', default=True)

    def __str__(self):
        return '{}'.format(self.name)


class Incidente(models.Model):
    time = models.DateTimeField(verbose_name='Tiempo', null=True)
    descripcion = models.TextField()
    estado = models.CharField(verbose_name='Estado', max_length=20, choices=ESTADO_INCIDENTE, default='NUEVO')
    lat = models.FloatField(verbose_name='Latitud')
    lng = models.FloatField(verbose_name='Longitud')
    is_active = models.BooleanField(verbose_name='Activo', default=True)
    tipo = models.ManyToManyField(TipoIncidente)
    user = models.ForeignKey(User)

    def __str__(self):
        return '{}'.format(self.id)

    def get_string_tipo(self):
        return ', '.join([tipos.name for tipos in self.tipo.all()])


class AsignacionIncidente(models.Model):
    time = models.DateTimeField(verbose_name='Fecha y hora', null=True)
    estado = models.CharField(verbose_name='Estado', max_length=20, choices=ESTADO_ASIGNACION, default='EN CURSO')
    incidente = models.OneToOneField(Incidente)
    centro_emergencia = models.ForeignKey(CentroEmergencia, blank=True)
    vehiculos = models.ManyToManyField(Vehiculo)
    is_active = models.BooleanField(verbose_name='Activo', default=True)

    def __str__(self):
        return '{}'.format(self.id)

    def get_string_vehiculos(self):
        return ', '.join([vehiculo.placa for vehiculo in self.vehiculos.all()])
