from flask import Flask
from flask_restful import Api
from .vistas import VistaAlbumes, VistaAlbum, VistaAlbumUsuario, VistaCancion, VistaAlbumCancion,VistaCanciones
from .modelos import db

def create_app(config= None):
    app = Flask(__name__,instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///canciones.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api = Api(app)
    api.add_resource(VistaAlbumes, '/albumes')
    api.add_resource(VistaAlbum, '/albumes/<int:album_id>')
    api.add_resource(VistaAlbumCancion, '/albumes/<int:album_id>/canciones')
    api.add_resource(VistaAlbumUsuario, '/usuario/<int:usuario_id>/albums')
    api.add_resource(VistaCanciones, '/canciones')
    api.add_resource(VistaCancion, '/canciones/<int:cancion_id>')
    
    return app
    