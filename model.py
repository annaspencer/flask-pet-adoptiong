from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__='pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(50),
                            nullable=False,
                            unique=False)

    species = db.Column(db.String(50),
                            nullable=True)
    image_url=db.Column(db.String(50), nullable=True)

    age = db.Column(db.Integer,
                            nullable=True)

    notes=db.Column(db.String(150),
                            nullable=True)

    available=db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        p =self
        return f"<Pet id={p.id} name={p.name} species={p.species} image_url={p.image_url}>"

    def show_details(self):
        p = self
        return f"{p.name}  {p.species}  {p.image_url}  {p.available}"