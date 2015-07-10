from project import db
from project.models import Feature

db.drop_all()
db.create_all()

# insert data
db.session.add(Feature('layered rocks', 'features/layered_rock.jpg', 'layered_rocks'))
db.session.add(Feature('gypsum vein', 'features/gypsum_vein.jpg', 'gypsum_vein'))
db.session.add(Feature('bright rocks', 'features/bright_rocks.jpg', 'bright_rocks'))
db.session.add(Feature('meteorites', 'features/meteorites.jpg', 'meteorites'))
db.session.add(Feature('blueberries', 'features/blueberries.jpg', 'blueberries'))
db.session.add(Feature('wheel wear', 'features/wheel_wear.jpg', 'wheel_wear'))

# commit the changes
db.session.commit()
