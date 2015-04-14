from django.db import models


class Encuesta(models.Model):
    creador = models.ForeignKey('User')
    nombre = models.CharField(max_length=100, blank=False, null=False)

    def is_finalized(self):
        return all([ link.visitado for link in self.link_set ])

    def enviar_mails(self):
        for link in self.link_set:
            link.enviar()
