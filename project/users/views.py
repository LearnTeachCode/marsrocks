from flask import flash, redirect, render_template, request, \
    url_for, Blueprint
from flask.ext.login import login_user, login_required, logout_user

from .forms import LoginForm, RegisterForm
from project import db
from project.models import User, bcrypt

# define blueprints
users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

@users_blueprint.route('/login', methods = ['POST', 'GET'])
def login():
    error = None
    # instance of login form
    form = LoginForm(request.form)

    # if POST, check data from form
    if request.method == 'POST':
        # check if form is valid
        if form.validate_on_submit():
            # look for input user in the db
            user = User.query.filter_by(name=request.form['username']).first()
            # authenication. check if user and hash password are in db.
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']):
                # use flask-login to handle session
                login_user(user)
                flash('You are logged in')
                return redirect(url_for('index'))
            # if credentials is invalid, rerender the form
            else:
                error = 'Invalid credentials'
    # if GET, show login template
    return render_template('login.html', form=form, error=error)

@users_blueprint.route('/logout')
@login_required
def logout():
    # logout_user from flask-login
    logout_user()
    flash('You are logged out')
    return redirect(url_for('index'))


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        # add user to db
        db.session.add(user)
        db.session.commit()
        # flask-login creates a session
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html', form=form)
