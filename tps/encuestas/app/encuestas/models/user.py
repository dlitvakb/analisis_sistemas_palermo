from django.db import models
from django.core.mail import send_mail


class User(models.Model):
    mail = models.EmailField(null=False, unique=True)

    def enviar_link(self, link, nombre_encuesta):
        subject = "Encuesta: %s" % (nombre_encuesta,)
        message = "Haga click en el siguiente link: %s%s" % (
            "http://localhost:8000/responder?ref=",
            link.id.int
        )
        from_mail = "kroma.harry@gmail.com"
        to_mail = [self.mail]
        send_mail(subject, message, from_mail, to_mail, fail_silently=False)

    def __unicode__(self):
        return "%s" % (self.mail,)
