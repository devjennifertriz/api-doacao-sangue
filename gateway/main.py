from flask import Flask, render_template, request, redirect, url_for, jsonify
from flasgger import Swagger
import requests

app = Flask(__name__)
# === Configurações do Swagger ===
app.config['SWAGGER'] = {
    'title': 'Gateway API - Doação de Sangue',
    'uiversion': 3,
    'specs_route': '/gateway-apidocs/',
    'static_url_path': '/flasgger_static',
}
swagger = Swagger(app)

#  === Configurações de URLs das API's ===
API_DOADORES = "http://127.0.0.1:8000/"
API_PACIENTES = "http://127.0.0.1:8001/"

# ======= HATEOAS ========
def gerar_links_solicitacao(solicitacao):
    solicitacao['_links'] = {
        "criterios": f"{API_DOADORES}/criterios",
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
        print(f"Status Paciente: {res_paciente.status_code}") # Debug
        solicitacao = res_paciente.json()

        #  Busca os doadores para o <select> (API Doadores)
        res_doadores = requests.get(f"{API_DOADORES}/doadores/")
        print(f"Status Doadores: {res_doadores.status_code}") # Debug
        doadores = res_doadores.json()

        res_criterios = requests.get(f"{API_DOADORES}/criterios/")
        print(f"Status Criterios: {res_criterios.status_code}") # Debug
        criterios = res_criterios.json()

        return render_template('registrar_doacao.html', 
                               solicitacao=solicitacao, 
                               doadores=doadores, 
                               criterios=criterios)
    except Exception as e:
        return f"Erro ao agregar dados das APIs: {e}", 500

@app.route("/swaggerDoadores")
def swagger_doadores():
    return redirect(f"{API_DOADORES}/swagger/")

@app.route("/swaggerPacientes")
def swagger_pacientes():
    return redirect(f"{API_PACIENTES}/swagger/")

@app.route("/registrar-comprovante", methods=['POST'])
def registrar_comprovante():
    dados_post = {
        "doador": request.form.get('doador_id'),
        "solicitacao_id": request.form.get('solicitacao_id')
    }
        
    arquivo = {'comprovante': request.files['comprovante']}
    
    response = requests.post(f"{API_DOADORES}/registros/", data=dados_post, files=arquivo)
    
    if response.status_code == 201:
        return redirect(url_for('index'))
    
    return f"Erro ao salvar na API Doadores: {response.text}", 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


