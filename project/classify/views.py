from flask import render_template, Blueprint

# define blueprints
classify_blueprint = Blueprint(
    'classify', __name__,
    template_folder='templates'
)

@classify_blueprint.route('/classify')
def index():
    return render_template('classify.html')
