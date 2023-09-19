from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Owner (db.model):
    __tablename__='owners'
    id = db.Colmn (db.Integer , primary_key = True)
    name = db.Column(db.string , unique = True)

    pets = db.relationship('pet',backref = 'owner')

    def __repr__ (self):
        return f'<pet owner {self.name}'

class Pet(db.model):
    __tablename__ ='pets'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.string)
    species = db.Column(db.string)

    owner_id = db.Column(db.Integer,db.Foreignkey('owner.id'))

    def __repr__ (self):
        return f'<pet{self.name},{self.species}>'
    
    
