from flask import Flask

def create_app(config= None):
    app = Flask(__name__,instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///canciones.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.route('/')
    def hello():
        from .modelos import db
        return str(db.metadata.tables.keys())
    return app
    