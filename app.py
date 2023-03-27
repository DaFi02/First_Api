from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.conection_postgresql import db
from routes.contacts import contacts

app = Flask(__name__)

app.secret_key = 'mysecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://first_api:123456@localhost/api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(contacts)
