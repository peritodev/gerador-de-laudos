from flask import Blueprint, render_template, request, redirect, url_for, current_app, session
import os
from utils.document_utils import atualizar_documento
from utils.upload_utils import upload_file

bp = Blueprint('in_loco', __name__, url_prefix='/sinistro_transito/in_loco')

@bp.before_app_first_request
def setup_logging():
    current_app.logger.debug('Blueprint in_loco criado')

@bp.route('/')
def index():
    current_app.logger.debug('Rota /sinistro_transito/in_loco acessada')
    return render_template('sinistro_transito/in_loco/layout_in_loco.html')

@bp.route('/historico', methods=['GET', 'POST'])
def historico_loco():
    if request.method == 'POST':
        try:
            current_app.logger.debug('POST /sinistro_transito/in_loco/historico')
            historico = request.form['historico']
            file_path = session.get('uploaded_file_path')
            if not file_path or not os.path.exists(file_path):
                raise Exception("Arquivo carregado não encontrado")
            current_app.logger.debug(f'Atualizando documento em {file_path} com o histórico fornecido')
            atualizar_documento(file_path, 'historico', historico)
            current_app.logger.debug('Documento atualizado com sucesso')
            return redirect(url_for('in_loco.historico_loco'))
        except Exception as e:
            current_app.logger.error(f'Erro ao atualizar documento: {e}', exc_info=True)
            return "Erro no servidor ao atualizar documento."
    current_app.logger.debug('Rota /sinistro_transito/in_loco/historico acessada (GET)')
    return render_template('sinistro_transito/in_loco/1_historico.html')

@bp.route('/consideracoes_iniciais')
def consideracoes_iniciais_loco():
    current_app.logger.debug('Rota /sinistro_transito/in_loco/consideracoes_iniciais acessada')
    return render_template('sinistro_transito/in_loco/2_consideracoes_iniciais.html')

@bp.route('/caracteristicas')
def caracteristicas_loco():
    current_app.logger.debug('Rota /sinistro_transito/in_loco/caracteristicas acessada')
    return render_template('sinistro_transito/in_loco/3_caracteristicas.html')

@bp.route('/exames_periciais')
def exames_periciais_loco():
    current_app.logger.debug('Rota /sinistro_transito/in_loco/exames_periciais acessada')
    return render_template('sinistro_transito/in_loco/4_exames_periciais.html')

@bp.route('/consideracoes_tecnicas_conclusao')
def consideracoes_tecnicas_conclusao_loco():
    current_app.logger.debug('Rota /sinistro_transito/in_loco/consideracoes_tecnicas_conclusao acessada')
    return render_template('sinistro_transito/in_loco/5_consideracoes_tecnicas_conclusao.html')

@bp.route('/quesitos_respostas')
def quesitos_respostas_loco():
    current_app.logger.debug('Rota /sinistro_transito/in_loco/quesitos_respostas acessada')
    return render_template('sinistro_transito/in_loco/6_quesitos_respostas.html')

@bp.route('/consideracoes_finais')
def consideracoes_finais_loco():
    current_app.logger.debug('Rota /sinistro_transito/in_loco/consideracoes_finais acessada')
    return render_template('sinistro_transito/in_loco/7_consideracoes_finais.html')

@bp.route('/upload', methods=['POST'])
def upload():
    current_app.logger.debug('POST /sinistro_transito/in_loco/upload')
    file_path, error = upload_file()
    if error:
        current_app.logger.error(f'Erro ao fazer upload do arquivo: {error}')
        return error
    session['uploaded_file_path'] = file_path
    current_app.logger.debug(f'Arquivo carregado com sucesso: {file_path}')
    return redirect(url_for('in_loco.index'))
