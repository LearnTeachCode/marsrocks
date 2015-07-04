import os
from flask.ext.bcrypt import Bcrypt
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

# create the application object
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
print '== APP_SETTINGS:', os.environ['APP_SETTINGS']

#create SQLAlchemy object
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# import models
from models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/classify')
def classify():
    return render_template('classify.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

if __name__ == '__main__':
    app.run()
