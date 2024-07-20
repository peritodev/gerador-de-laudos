from flask import Blueprint, render_template

bp = Blueprint('in_veiculo', __name__)

@bp.route('/')
def index():
    try:
        return render_template('sinistro_transito/in_veiculo.html')
    except Exception as e:
        print(f"Erro ao renderizar in_veiculo.html: {e}")
        return "Erro ao carregar a página In Veículo"
