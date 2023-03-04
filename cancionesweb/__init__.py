from flask import Flask
from flask_restful import Api
from .vistas import VistaAlbumes
from .modelos import db

def create_app(config= None):
    app = Flask(__name__,instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///canciones.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api = Api(app)
    api.add_resource(VistaAlbumes, '/albumes')
    
    return app
    