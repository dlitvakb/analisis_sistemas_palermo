from django.db import models


class Grupo(models.Model):
    encuesta = models.ForeignKey('Encuesta', related_name='grupos')
    nombre = models.CharField(max_length=100, blank=False, null=False)

    def exportar(self):
        export = {}
        export["nombre"] = self.nombre

        export["preguntas"] = []
        for pregunta in self.preguntas.all():
            export["preguntas"].append(pregunta.exportar())

    def __unicode__(self):
        return "Encuesta %d: %s - %s" % (
            self.encuesta.id,
            self.encuesta.nombre,
            self.nombre
        )
