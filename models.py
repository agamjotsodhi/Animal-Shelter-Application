# Pet model for app.py

from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE= "https://static.vecteezy.com/system/resources/previews/006/470/524/original/animal-pet-logo-template-vector.jpg"

db = SQLAlchemy()

class Pet(db.Model):
    # Template for each pet that is ready for adoption:
    __tablename__ = "listofpets"
    
    # Table columns 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
    
    # Returns back image for model
    def image_url(self):
        return self.photo_url or DEFAULT_IMAGE
    
def connect_db(app):
    db.app = app
    db.init_app(app)
    
    