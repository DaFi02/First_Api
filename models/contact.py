from src.conection_postgresql import db
from flask_migrate import Migrate
from app import app

migrate = Migrate(app, db)


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, fullname, email, phone):
        self.fullname = fullname

