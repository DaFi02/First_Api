from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.conection_postgresql import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://first_api:123456@localhost/api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'
