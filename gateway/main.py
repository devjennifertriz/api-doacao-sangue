from flask import Flask, render_template, request, redirect, url_for, jsonify
from flasgger import Swagger
import requests

app = Flask(__name__)
# === Configurações do Swagger ===
app.config['SWAGGER'] = {
    'title': 'Gateway API - Doação de Sangue',
    'description': 'Interface Unificada para API Doadores e API Pacientes',
    'uiversion': 3
}
swagger = Swagger(app)

#  === Configurações de URLs das API's ===
API_DOADORES = "http://127.0.0.1:8000/doadores/"
API_PACIENTES = "http://127.0.0.1:8001"

# ======= HATEOAS ========
def gerar_links_solicitacao(solicitacao):
    solicitacao['_links'] = {
        "detalhes": f"/detalhes-solicitacao/{solicitacao['id']}",
        "api_origem": f"{API_PACIENTES}/solicitacoes/{solicitacao['id']}/"
    }
    return solicitacao

# ======= HATEOAS ========
@app.route("/")
# ==== Página inicial - listagem de solicitações de doação ====
def index():
    try:       
        response = requests.get(f"{API_PACIENTES}/solicitacoes/")
        solicitacoes = response.json()
            
        # Aplica HATEOAS em cada item
        for s in solicitacoes:
            gerar_links_solicitacao(s)
                
        return render_template('index.html', solicitacoes=solicitacoes)
    except Exception as e:
        return f"Erro ao conectar com API Pacientes (8001): {e}", 500

@app.route("/detalhes-solicitacao/<int:id>")
def detalhes_solicitacao(id):
    try:
        # Busca a solicitação específica (API Pacientes)
        res_paciente = requests.get(f"{API_PACIENTES}/solicitacoes/{id}/")
        demanda = res_paciente.json()

        #  Busca os doadores para o <select> (API Doadores)
        res_doadores = requests.get(f"{API_DOADORES}/doadores/")
        doadores = res_doadores.json()

        res_criterios = requests.get(f"{API_DOADORES}/criterios/")
        criterios = res_criterios.json()

        return render_template('registrar_doacao.html', 
                               demanda=demanda, 
                               doadores=doadores, 
                               criterios=criterios)
    except Exception as e:
        return f"Erro ao agregar dados das APIs: {e}", 500

@app.route("/registrar-comprovante", methods=['POST'])
def registrar_comprovante():
    dados_post = {
        "doador": request.form.get('doador_id'),
        "solicitacao_id": request.form.get('solicitacao_id')
    }
        
    arquivo = {'comprovante': request.files['comprovante']}
    
    response = requests.post(f"{API_DOADORES}/registros-doacao/", data=dados_post, files=arquivo)
    
    if response.status_code == 201:
        return redirect(url_for('index'))
    
    return f"Erro ao salvar na API Doadores: {response.text}", 400
if __name__ == '__main__':
    # Roda o Gateway na porta 5000
    app.run(port=5000, debug=True)
