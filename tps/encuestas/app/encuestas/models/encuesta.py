from django.db import models
import datetime


class Encuesta(models.Model):
    creador = models.ForeignKey('User', related_name='encuestas')
    usuarios = models.ManyToManyField('User', related_name='encuestas_participadas')
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(default="")
    fecha_expiracion = models.DateTimeField(null=True)

    def exportar(self):
        if not self._is_finalized():
            raise Exception("La Encuesta no esta finalizada")

        export = {}
        export["nombre"] = self.nombre
        export["descripcion"] = self.descripcion

        export["grupos"] = []
        for grupo in self.grupos.all():
            export["grupos"].append(grupo.exportar())

        export["respuestas_totales"] = self.respuestas.count()

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
            return self.fecha_expiracion < datetime.now()
        return False

    def _is_finalized(self):
        return all([ link.visitado for link in self.links.all() ]) or self._is_expired()

    def _finalizada(self):
        if self._is_finalized():
            return "(Finalizada) "
        return ""

    def __unicode__(self):
        return "%s%d - %s (Creada por: %s)" % (
            self._finalizada(),
            self.id,
            self.nombre,
            self.creador.mail
        )
