from django.db import models


class Opcion(models.Model):
    pregunta = models.ForeignKey('Pregunta', related_name='opciones')
    opcion = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return "%s: %s - %s - %d: %s" % (
            self.pregunta.grupo.encuesta.nombre,
            self.pregunta.grupo.nombre,
            self.pregunta.pregunta,
            self.id,
            self.opcion
        )
