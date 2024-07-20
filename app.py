from flask import Flask, render_template
from routes import bp as routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp)

@app.route('/')
def home():
    try:
        return render_template('index_home.html')
    except Exception as e:
        app.logger.error(f"Erro ao renderizar index_home.html: {e}")
        return "Erro ao carregar a página inicial"

if __name__ == '__main__':
    app.run(debug=True)
