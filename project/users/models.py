from sqlalchemy.orm import relationship

from project import db
from project import bcrypt

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
