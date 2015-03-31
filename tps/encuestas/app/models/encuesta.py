from server import db


class Encuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    links = db.relationship('Link', backref=db.backref('encuesta', lazy='joined'),
            lazy='dynamic')
    grupos = db.relationship('Grupo', backref=db.backref('encuesta', lazy='joined'),
            lazy='dynamic')
    nombre = db.Column(db.String(100))


    def is_finalized(self):
        return all([link.visitado for link in self.links.all()])

    def enviar_mails(self):
        for link in self.links.all():
            link.enviar_mail()
