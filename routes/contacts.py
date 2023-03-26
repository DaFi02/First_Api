from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def hello_world():
    return render_template('index.html')


@contacts.route('/new')
def add_contact():
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
