import typing
import enum
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

album_cancion = db.Table('album_cancion',
    db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key = True),
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
    ''' Represents an album table.\n
            titulo = string,\n
            ano = int\n
            description = string\n
            medio = Medio
    '''
    __tablename__ = 'album'

    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50))
    ano = db.Column(db.Integer)
    descripcion = db.Column(db.String(150))
    medio = db.Column(db.Enum(Medio))

    usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    canciones = db.relationship('Cancion', secondary = 'album_cancion', back_populates="albumes")

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))

    albumes = db.relationship('Album', cascade = 'all, delete, delete-orphan')

class EnumerateToDict(fields.Field):
    def _serialize(self, value: typing.Any, attr: str | None, obj: typing.Any, **kwargs):
        if value is None:
            return None
        return {"llave": value.name, "valor" : value.value}

class AlbumSchema(SQLAlchemyAutoSchema):
    medio = EnumerateToDict(attribute=('medio'))
    class Meta:
        model = Album
        include_relationships = True
        load_instance = True

class CancionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cancion
        include_relationships = True
        load_instance = True

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True
