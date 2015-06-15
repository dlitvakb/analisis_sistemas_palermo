import datetime
import pytz
from django.db import models


class Encuesta(models.Model):
    usuarios = models.ManyToManyField('User', related_name='encuestas_participadas')
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(default="")
    fecha_expiracion = models.DateTimeField(null=True)

    @property
    def is_finalized(self):
        return all([ link.visitado for link in self.links.all() ]) or self._is_expired()

    @property
    def cantidad_visitas(self):
        return self.links.filter(visitado=True).count()

    @property
    def cantidad_respuestas(self):
        return self.links.filter(finalizada=True).count()

    def exportar(self):
        export = {}
        export["nombre"] = self.nombre
        export["descripcion"] = self.descripcion
        export["finalizada"] = self.is_finalized

        export["grupos"] = []
        for grupo in self.grupos.all():
            export["grupos"].append(grupo.exportar())

        export["respuestas_totales"] = self.cantidad_respuestas
        export["cantidad_visitas"] = self.cantidad_visitas

        return export

    def generar_links(self):
        for usuario in self.usuarios.all():
            self.links.create(user=usuario)

        self._enviar_mails()

    def _enviar_mails(self):
        for link in self.links.filter(enviado=False):
            link.enviar()

    def _is_expired(self):
        if self.fecha_expiracion is not None:
            return self.fecha_expiracion < pytz.UTC.localize(datetime.datetime.now())
        return False

    def _finalizada(self):
        if self.is_finalized:
            return "(Finalizada) "
        return ""

    def __unicode__(self):
        return "%s%d - %s (Creada por: %s)" % (
            self._finalizada(),
            self.id,
            self.nombre,
            self.creador.mail
        )
