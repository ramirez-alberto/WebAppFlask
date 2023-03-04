from flask_restful import Resource
from ..modelos import AlbumSchema , Album

a_schema = AlbumSchema(many = True)

class VistaAlbumes(Resource):
    def get(self):
        album = Album.query.all()
        return a_schema.dump(album)