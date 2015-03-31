from server import db


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    encuesta_id = db.Column(db.Integer, db.ForeignKey('encuesta.id'))
    link = db.Column(db.String(100), unique=True)
    visitado = db.Column(db.Boolean, default=False)

    def enviar_mail(self):
        self.user.enviar_mail(self)
