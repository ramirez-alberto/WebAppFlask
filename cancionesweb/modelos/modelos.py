import enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

album_cancion = db.Table('album_cancion',
    db.Column('album_id', db.Integer, db.ForeignKey('album.id', primary_key = True)),
    db.Column('cancion_id', db.Integer, db.ForeignKey('cancion.id'), primary_key = True))

class Cancion(db.Model):
    __tablename__ = 'cancion'

    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(150))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(50))

    albumes = db.relationship('Album', secondary = 'album_cancion', back_populates="canciones")

class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3

class Album(db.Model):
    __tablename__ = 'album'

    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50))
    ano = db.Column(db.Integer)
    descripcion = db.Column(db.String(150))
    medio = db.Column(db.Enum(Medio))

    canciones = db.relationship('Cancion', secondary = 'album_cancion', back_populates="albumes")

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))

    albumes = db.relationship('Album', cascade = 'all, delete, delete-orphan')
