import uuid
from django.db import models

from encuestas.models.user import User


class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, related_name='links')
    encuesta = models.ForeignKey('Encuesta', related_name='links')
    enviado = models.BooleanField(default=False)
    visitado = models.BooleanField(default=False)
    finalizada = models.BooleanField(default=False)

    def enviar(self):
        if not self.enviado:
            self.user.enviar_link(self, self.encuesta.nombre)
            self.enviado = True
            self.save()

    def _visitado(self):
        if self.finalizada:
            return "(Finalizada) "
        if self.visitado:
            return "(Visitado) "
        return ""

    def __unicode__(self):
        return "%s%s - %s" % (
            self._visitado(),
            self.user.mail,
            self.encuesta.nombre
        )
