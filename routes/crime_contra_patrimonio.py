from flask import Blueprint, render_template

bp = Blueprint('crime_contra_patrimonio', __name__, url_prefix='/crime_patrimonio')

@bp.route('/')
def index():
    return render_template('crime_patrimonio/index_crime_patrimonio.html')
