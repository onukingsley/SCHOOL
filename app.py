from flask import Flask, render_template

from functions import *
from config import *

app = Flask(__name__)


@app.context_processor
def all():
    info = {
        'menu': menu
    }
    return dict(details=details, replacer=replacer, info=info)


@app.route('/')
def hello_world():
    pageInfo = {
        'title': 'Welcome',
    }
    return render_template('index.html', name="Welcome", pg=pageInfo)


@app.route('/about')
def about():
    pageInfo = {
        'title': 'about us',
        'sub': 'Your ward is important to us. Feel free to drop it and pick it up later'
    }
    return render_template('about.html', pg=pageInfo)


@app.route('/admission')
def admissions():
    pageInfo = {
        'title': 'admission',
        'sub': 'Admission is currently undergoing. Rush now before it is too late and stay one year at home'
    }
    return render_template('admissions.html', pg=pageInfo)


@app.route('/contact')
def contact():
    pageInfo = {
        'title': 'contact',
        'sub': 'Here is our contact page! '
    }
    return render_template('contact.html', pg=pageInfo)


@app.route('/login')
def login():
    pageInfo = {
        'title': 'login',
        'sub': 'Welcome back. Please provide the accurate login details'
    }
    return render_template('login.html', pg=pageInfo)


@app.route('/register')
def register():
    pageInfo = {
        'title': 'register',
        'sub': 'You are welcome. Please let us have your accurate information '
    }
    return render_template('register.html', pg=pageInfo)


if __name__ == '__main__':
    app.run(debug=True)
