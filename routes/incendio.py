from flask import Blueprint, render_template

bp = Blueprint('incendio', __name__, url_prefix='/incendio')

@bp.route('/')
def index():
    return render_template('incendio/index_incendio.html')
