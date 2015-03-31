from server import db


class Opcion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grupo_id = db.Column(db.Integer, db.ForeignKey('pregunta.id'))
    opcion = db.Column(db.String(255))
