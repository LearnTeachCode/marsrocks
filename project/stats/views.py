from flask import render_template, Blueprint
from project.models import  Feature

# define blueprints
stats_blueprint = Blueprint(
    'stats', __name__,
    template_folder='templates'
)

@stats_blueprint.route('/stats')
def index():

    features = Feature.query.all()
    json_data=[feature.serialize for feature in features]
    print json_data


    return render_template('stats.html')
