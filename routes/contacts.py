from flask import Blueprint, render_template, request
from models.contact import Contact
from src.conection_postgresql import db

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def hello_world():
    return render_template('index.html')


@contacts.route('/new', methods=['GET', 'POST'])
def add_contact():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    return 'Saving Contact!'


@contacts.route('/update')
def update_contact():
    return 'Contact updated! and Saving Contact!'


@contacts.route('/delete')
def delete_contact():
    return 'Contact deleted!'


@contacts.route('/about')
def about():
    return render_template('about.html')
