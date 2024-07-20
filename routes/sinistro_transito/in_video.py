from flask import Blueprint, render_template, current_app as app

bp = Blueprint('in_video', __name__)
app.logger.debug('Blueprint in_video criado')

@bp.route('/')
def index():
    app.logger.debug('Rota /sinistro_transito/in_video acessada')
    return render_template('sinistro_transito/in_video/index.html')
