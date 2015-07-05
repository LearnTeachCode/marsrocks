from project import db
from project.models import User

db.create_all()

# insert data
db.session.add(User("admin", "password"))

# commit the changes
db.session.commit()
