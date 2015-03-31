from server import db


class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'))
    pregunta = db.Column(db.String(255))
    opciones = db.relationship('Opcion', backref=db.backref('pregunta', lazy='joined'),
            lazy='dynamic')
