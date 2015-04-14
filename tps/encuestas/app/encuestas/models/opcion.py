from django.db import models


class Opcion(models.Model):
    pregunta = models.ForeignKey('Pregunta')
    opcion = models.TextField(blank=False, null=False)
