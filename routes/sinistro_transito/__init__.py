from flask import Blueprint

bp = Blueprint('sinistro_transito', __name__)

from .in_veiculo import bp as bp_in_veiculo

bp.register_blueprint(bp_in_veiculo, url_prefix='/in_veiculo')
