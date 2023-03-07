from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .vistas import (VistaAlbumes, VistaAlbum, VistaAlbumUsuario, VistaCancion,
    VistaAlbumCancion,VistaCanciones, VistaSignIn, VistaLogin)
from .modelos import db

def create_app(config= None):
    app = Flask(__name__,instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///canciones.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "super-secret" 

    db.init_app(app)

    api = Api(app)
    api.add_resource(VistaAlbumes, '/albumes')
    api.add_resource(VistaAlbum, '/albumes/<int:album_id>')
    api.add_resource(VistaAlbumCancion, '/albumes/<int:album_id>/canciones')
    api.add_resource(VistaAlbumUsuario, '/usuario/<int:usuario_id>/albums')
    api.add_resource(VistaCanciones, '/canciones')
    api.add_resource(VistaCancion, '/canciones/<int:cancion_id>')
    api.add_resource(VistaSignIn, '/signin')
    api.add_resource(VistaLogin, '/login')
    
    jwt = JWTManager(app)
    cors = CORS(app)
    return app
