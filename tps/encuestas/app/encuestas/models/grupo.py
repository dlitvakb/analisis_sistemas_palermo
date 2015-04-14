from django.db import models


class Grupo(models.Model):
    encuesta = models.ForeignKey('Encuesta')
    nombre = models.CharField(max_length=100, blank=False, null=False)
