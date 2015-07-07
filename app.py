import os

from flask import Flask, render_template

from flask.ext.login import LoginManager

# create (instantiate) the application object
app = Flask(__name__)

# create instance of login manager
login_manager = LoginManager()
# register login manager with the app object
login_manager.init_app(app)

# use try except to so that newbies don't have to set up environment variables
try:
    app.config.from_object(os.environ['APP_SETTINGS'])
    print '== os APP_SETTINGS:', os.environ['APP_SETTINGS']
except:
    app.config.from_object('config.DevelopmentConfig')
    print '== hardcode config.DevelopmentConfig'



# import blueprints
from project.users.views import users_blueprint

# register our blueprints with the app.
app.register_blueprint(users_blueprint)

from project.models import *

# define the login view
login_manager.login_view = "users.login"

# registers user_loader with flask-login.
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


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
