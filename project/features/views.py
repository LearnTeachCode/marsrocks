from flask import render_template, Blueprint

# define blueprints
features_blueprint = Blueprint(
    'features', __name__,
    template_folder='templates'
)

@features_blueprint.route('/features')
def index():
    return render_template('index.html')
