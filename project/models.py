from project import db
from project import bcrypt

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
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
        return '<name - {}>'.format(self.name)
