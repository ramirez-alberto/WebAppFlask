from cancionesweb import create_app
from modelos import db

app = create_app()
db.init_app(app)
with app.app_context():
    from modelos import Album, Medio, AlbumSchema
    a = Album(titulo="Prueba", ano=1999, descripcion="Lorem Ipsum", medio=Medio.CASETE)
    a_schema = AlbumSchema()
    db.session.add(a)
    db.session.commit()

    print([a_schema.dump(a) for a in Album.query.all()])
