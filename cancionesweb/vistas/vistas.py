from typing import Any, Tuple
from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from ..modelos import AlbumSchema , Album, Usuario, CancionSchema, Cancion, db

album_schema = AlbumSchema()
albums_schema = AlbumSchema(many = True)

cancion_schema = CancionSchema()

class VistaAlbumes(Resource):
    def get(self) -> Any | list:
        album = Album.query.all()
        return albums_schema.dump(album)

class VistaAlbumUsuario(Resource):
    def post(self, usuario_id: int) -> int | Tuple[str,int]:
        album = Album(
            titulo = request.json['titulo'],
            ano = request.json['ano'],
            descripcion = request.json['descripcion'],
            medio = request.json['medio']
        )
        usuario = Usuario.query.get_or_404(usuario_id)
        usuario.albumes.append(album)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return 'El usuario ya tiene un album con el mismo nombre',409
        
        return album_schema.dump((album))
    
    def get(self,usuario_id: int) -> int | list:
        usuario = Usuario.query.get_or_404(usuario_id)
        return [album_schema.dump(album) for album in usuario.albumes]

class VistaAlbum(Resource):
    def get(self, album_id: int) -> str | int:
        album = Album.query.get_or_404(album_id)
        return album_schema.dump(album)
    
    def put(self,album_id: int) -> str | int:
        album = Album.query.get_or_404(album_id)

        album.titulo = request.json.get('titulo',album.titulo),
        album.ano = request.json.get('ano',album.ano),
        album.descripcion = request.json.get('descripcion',album.descripcion),
        album.medio = request.json.get('medio',album.medio)
        
        db.session.commit()
        return album_schema.dump(album)
    
    def delete(self, album_id: int) -> int | Tuple[str, int]:
        album = Album.query.get_or_404(album_id)

        db.session.delete(album)
        db.session.commit()
        return '',204

class VistaCanciones(Resource):
    def get(self):
        return [ cancion_schema.dump(cancion) for cancion in Cancion.query.all() ]

    def post(self):
        cancion = Cancion(
            titulo = request.json['titulo'],
            minutos = request.json['minutos'],
            segundos = request.json['segundos'],
            interprete = request.json['interprete']
        )

        db.session.add(cancion)
        db.session.commit()

        return cancion_schema.dump(cancion)
    
class VistaCancion(Resource):
    def get(self, cancion_id):
        return cancion_schema.dumps(Cancion.query.get_or_404(cancion_id))
    
    def put(self, cancion_id: int) -> Tuple[str,int]:
        cancion = Cancion.query.get_or_404(cancion_id)

        cancion.titulo = request.json['titulo']
        cancion.minutos = request.json['minutos']
        cancion.segundos = request.json['segundos']
        cancion.interprete = request.json['interprete']

        db.session.commit()

        return cancion_schema.dump(cancion)

    def delete(self, cancion_id: int) -> Tuple[str, int]:
        cancion = Cancion.query.get_or_404(cancion_id)

        db.session.delete(cancion)
        db.session.commit()
        return '',204

class VistaAlbumCancion(Resource):
    def get(self,album_id):
        album = Album.query.get_or_404(album_id)
        return [cancion_schema.dump(cancion) for cancion in album.canciones]
    
    def post(self,album_id):
        album = Album.query.get_or_404(album_id)

        if 'cancion_id' in request.json.keys():
            cancion = Cancion.query.get(request.json['cancion_id'])
            if cancion is not None:
                album.canciones.append(cancion)
            else:
                return 'Cancion erronea',404
        else:
            cancion = Cancion(
                titulo = request.json['titulo'],
                minutos = request.json['minutos'],
                segundos = request.json['segundos'],
                interprete = request.json['interprete']
            )
            album.canciones.append(cancion)
        
        db.session.commit()
        return cancion_schema.dump(cancion)

            
