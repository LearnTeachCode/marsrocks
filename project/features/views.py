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

    return render_template('features.html', features=features)

@features_blueprint.route('/features/<id>')
def classifications(id):
    classifies = Classification.query.filter_by(feature_id=id)
    photos = []
    ids = {}
    for classify in classifies:
        print classify.photo_id
        if classify.photo_id not in ids:
            photos.append(classify.photo)
            ids[classify.photo_id] = classify.photo_id

    feature = Feature.query.filter_by(id=id).first()

    return render_template('one_feature.html', photos=photos, feature=feature)
