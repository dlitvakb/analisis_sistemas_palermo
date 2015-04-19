from django.db import models


class Pregunta(models.Model):
    grupo = models.ForeignKey('Grupo', related_name='preguntas')
    pregunta = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return "%s: %s - %d: %s" % (
            self.grupo.encuesta.nombre,
            self.grupo.nombre,
            self.id,
            self.pregunta
        )
