from django.db import models


class Respuesta(models.Model):
    encuesta = models.ForeignKey('Encuesta', related_name="respuestas", null=False)
    opcion = models.ForeignKey('Opcion', related_name="respuestas", null=False)
    finalizada = models.BooleanField(default=False)
