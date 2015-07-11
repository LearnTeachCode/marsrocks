from sqlalchemy import ForeignKey

from project import db

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
