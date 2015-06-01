from django.db import models


class Respuesta(models.Model):
    encuesta = models.ForeignKey('Encuesta', related_name="respuestas", null=False)
    opcion = models.ForeignKey('Opcion', related_name="respuestas", null=False)

    def save(self, *args, **kwargs):
        try:
            self.encuesta is None
        except:
            self.encuesta = self.opcion.pregunta.grupo.encuesta

        super(Respuesta, self).save(*args, **kwargs)
