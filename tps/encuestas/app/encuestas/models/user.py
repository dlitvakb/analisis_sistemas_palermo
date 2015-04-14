from django.db import models


class User(models.Model):
    mail = models.EmailField(null=False, unique=True)

    def enviar_link(self, link):
        pass
