import uuid
from django.db import models


class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey('User')
    encuesta = models.ForeignKey('Encuesta')
    visitado = models.BooleanField(default=False)

    def enviar(self):
        self.user.enviar_link(self)
