from django.db import models
from encuestas.models.user import User


class Respuesta(models.Model):
    usuario = models.ForeignKey(User, related_name="respuestas", null=False)
    encuesta = models.ForeignKey('Encuesta', related_name="respuestas", null=False)
    opcion = models.ForeignKey('Opcion', related_name="respuestas", null=False)

    def save(self, *args, **kwargs):
        try:
            self.usuario is None
        except:
            self.encuesta = self.opcion.pregunta.grupo.encuesta

        super(Respuesta, self).save(*args, **kwargs)
