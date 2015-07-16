import json
from flask import render_template, Blueprint
from project.stats.process_classifications import get_data

# define blueprints
stats_blueprint = Blueprint(
    'stats', __name__,
    template_folder='templates'
)

@stats_blueprint.route('/stats')
def index():
    #Justin, you can access the json through the variable json_data
    json_data = json.dumps(get_data())

    return render_template('stats.html', json_data=json_data)
