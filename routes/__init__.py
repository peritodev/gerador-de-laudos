from flask import Blueprint, render_template

bp = Blueprint('routes', __name__)

from .sinistro_transito import bp as sinistro_transito_bp

bp.register_blueprint(sinistro_transito_bp, url_prefix='/sinistro_transito')

@bp.route('/sinistro_transito/')
def sinistro_transito_index():
    try:
        return render_template('sinistro_transito/index_sinistro_transito.html')
    except Exception as e:
        print(f"Erro ao renderizar index_sinistro_transito.html: {e}")
        return "Erro ao carregar a página de Sinistro de Trânsito"
