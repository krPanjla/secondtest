from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kartik panjla'}
    posts = [
    {'author': {'username': 'Alok'},
    'body': 'Hey buddy '
    },
    {
    'author': {'username': 'Moksh'},
    'body': 'Spider man is my favourite super hero'
    }
    ]
    return render_template('index.html', title='Home', user=user,posts=posts)    