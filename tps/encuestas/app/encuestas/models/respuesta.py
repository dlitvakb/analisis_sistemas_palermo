from django.db import models


class Respuesta(models.Model):
    opciones = models.ManyToManyField('Opcion')
    finalizada = models.BooleanField(default=False)
