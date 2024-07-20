from flask import request, current_app as app
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'odt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
    try:
        app.logger.debug('Upload de arquivo iniciado')
        if 'file' not in request.files:
            app.logger.error('Nenhum arquivo enviado')
            return None, "Nenhum arquivo foi enviado."
        file = request.files['file']
        if file.filename == '':
            app.logger.error('Nenhum arquivo selecionado')
            return None, "Nenhum arquivo foi selecionado."
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            app.logger.debug(f'Arquivo {filename} salvo em {file_path}')
            return file_path, None
        app.logger.error('Arquivo inválido')
        return None, "Arquivo inválido."
    except Exception as e:
        app.logger.error(f'Erro ao fazer upload do arquivo: {e}', exc_info=True)
        return None, "Erro no servidor ao fazer upload do arquivo."
