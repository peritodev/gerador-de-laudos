from flask import Blueprint, render_template

bp = Blueprint('engenharia', __name__, url_prefix='/engenharia')

@bp.route('/')
def index():
    return render_template('engenharia/index_engenharia.html')
