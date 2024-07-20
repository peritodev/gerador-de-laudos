from flask import Blueprint

bp = Blueprint('crime_contra_pessoa', __name__)

@bp.route('/')
def index():
    return "Página de Crime contra a Pessoa"
