from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from project import db
from project.users.models import User
from project.classify.models import Classification

class VisitedPhoto(db.Model):
    __tablename__ = 'visited_photos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    photo_id = db.Column(db.Integer, ForeignKey('photos.id'))

    def __init__(self, user_id, photo_id):
        self.user_id = user_id
        self.photo_id = photo_id

    def __repr__(self):
        return '<visited_photos: user {}, photo {}>'.format(self.user_id, self.photo_id)

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    imageid = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime)
    classifications = relationship("Classification", backref='photo', lazy='dynamic')

    def __init__(self, url, imageid, created_at):
        self.url = url
        self.imageid = imageid
        self.created_at = created_at

    def __repr__(self):
        return '<photo - {}>'.format(self.url)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'url': self.url,
            'imageid': self.imageid,
            'created_at': self.created_at
        }

class Feature(db.Model):
    __tablename__ = 'features'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, nullable=False)
    classifications = relationship("Classification", backref='feature', lazy='dynamic')

    def __init__(self, name, photo_url, slug):
        self.name = name
        self.photo_url = photo_url
        self.slug = slug

    def __repr__(self):
        return '<feature - {}>'.format(self.name)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'photo_url': self.photo_url
        }
