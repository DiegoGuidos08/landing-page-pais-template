from utils.db import db
 
class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellido = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(30), nullable=False)
    mensaje = db.Column(db.String(300), nullable=False)

    def __init__(self, nombre, apellido, correo, mensaje)-> None:
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.mensaje = mensaje

    def __repr__(self):
        return f"User({self.id}, '{self.nombre}', '{self.apellido}', '{self.correo}', '{self.mensaje}')"