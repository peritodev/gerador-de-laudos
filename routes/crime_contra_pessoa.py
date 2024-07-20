from flask import Blueprint, render_template

bp = Blueprint('crime_contra_pessoa', __name__, url_prefix='/crime_pessoa')

@bp.route('/')
def index():
    return render_template('crime_pessoa/index_crime_pessoa.html')