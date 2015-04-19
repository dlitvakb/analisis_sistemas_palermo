from django.db import models


class Encuesta(models.Model):
    creador = models.ForeignKey('User', related_name='encuestas')
    usuarios = models.ManyToManyField('User', related_name='encuestas_participadas')
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(default="")

    def generar_links(self):
        for usuario in self.usuarios.all():
            self.links.create(user=usuario)

        self._enviar_mails()

    def _enviar_mails(self):
        for link in self.links.filter(enviado=False):
            link.enviar()

    def _is_finalized(self):
        return all([ link.visitado for link in self.links.all() ])

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
