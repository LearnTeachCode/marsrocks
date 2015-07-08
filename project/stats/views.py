from flask import render_template, Blueprint

# define blueprints
stats_blueprint = Blueprint(
    'stats', __name__,
    template_folder='templates'
)

@stats_blueprint.route('/stats')
def index():
    return render_template('stats.html')
