from flask import render_template, Blueprint

from project import db
from project.models import Classification, Feature

# define blueprints
features_blueprint = Blueprint(
    'features', __name__,
    template_folder='templates'
)

@features_blueprint.route('/features')
def index():
    features = db.session.query(Feature).all()

    return render_template('features.html', features=features, feature=features[0])

@features_blueprint.route('/features/<id>')
def classifications(id):
    classifies = Classification.query.filter_by(feature_id=id)
    photos = []
    for classify in classifies:
        photos.append(classify.photo)

    return render_template('one_feature.html', photos=photos, photo=photos[0])
