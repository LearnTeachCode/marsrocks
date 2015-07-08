from project import db
from project import bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    # 'lazy = dynamic' u.classifications you get the result of evaluating the query,
    # instead of the query object still unevaluated.
    classifications = relationship("Classification", backref='user', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        # hash the plain text password before saving to database
        self.password = bcrypt.generate_password_hash(password)

    # required by flask-login
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<user - {}>'.format(self.username)

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    imageid = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    classifications = relationship("Classification", backref='photo', lazy='dynamic')

    def __init__(self, url, imageid, created_at):
        self.url = url
        self.imageid = imageid
        self.created_at = created_at

    def __repr__(self):
        return '<photo - {}>'.format(self.url)

class Feature(db.Model):
    __tablename__ = 'features'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, nullable=False)
    classifications = relationship("Classification", backref='feature', lazy='dynamic')

    def __init__(self, name, photo_url):
        self.name = name
        self.photo_url = photo_url

    def __repr__(self):
        return '<feature - {}>'.format(self.name)

class Classification(db.Model):
    __tablename__ = 'classifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    photo_id = db.Column(db.Integer, ForeignKey('photos.id'))
    feature_id = db.Column(db.Integer, ForeignKey('features.id'))

    def __init__(self, user_id, photo_id, feature_id):
        self.user_id = user_id
        self.photo_id = photo_id
        self.feature_id = feature_id

    def __repr__(self):
        return '<classification: user {}, photo {}, feature {}>'.format(self.user_id, self.photo_id, self.feature_id)
