from server import db


class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    encuesta_id = db.Column(db.Integer, db.ForeignKey('encuesta.id'))
    nombre = db.Column(db.String(100))
    preguntas = db.relationship('Pregunta', backref=db.backref('grupo', lazy='joined'),
            lazy='dynamic')
