from django.db import models


class Pregunta(models.Model):
    grupo = models.ForeignKey('Grupo')
    pregunta = models.TextField(blank=False, null=False)
