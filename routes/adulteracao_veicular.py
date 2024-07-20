from flask import Blueprint, render_template

bp = Blueprint('adulteracao_veicular', __name__, url_prefix='/adulteracao_veicular')

@bp.route('/')
def index():
    return render_template('adulteracao_veicular/index_adulteracao_veicular.html')
