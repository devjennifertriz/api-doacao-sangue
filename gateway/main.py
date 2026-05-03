from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import os

app = Flask(__name__)
app.static_folder = 'css'

#  === Configurações de URLs das API's ===
API_DOADORES = "http://127.0.0.1:8000"
API_PACIENTES = "http://127.0.0.1:8001"

# ======= HATEOAS ========
def links_solicitacao(solicitacao):
    solicitacao['_links'] = {
        "criterios": f"{API_DOADORES}/criterios",
        "detalhes": f"/detalhes-solicitacao/{solicitacao['id']}",
        "api_origem": f"{API_PACIENTES}/solicitacoes/{solicitacao['id']}/",
    }
    return solicitacao

def links_navegacao():
    return {
        "home": "/",
        "nova_solicitacao": "/nova-solicitacao",
        "swagger_doadores": f"{API_DOADORES}/swagger/",
        "swagger_pacientes": f"{API_PACIENTES}/swagger/",
        "debug": "/debug"
    }

# === Configurações do Swagger ===
@app.route("/swaggerDoadores/")
def swagger_doadores():
    return redirect(f"{API_DOADORES}/swagger/")

@app.route("/swaggerPacientes/")
def swagger_pacientes():
    return redirect(f"{API_PACIENTES}/swagger/")

# ==== Endpoint de DEBUG ====
@app.route("/debug")
def debug():
    """Mostra qual URL está sendo usada"""
    return jsonify({
        "codespace_name": codespace_name,
        "API_DOADORES": API_DOADORES,
        "API_PACIENTES": API_PACIENTES,
        "swagger_doadores": f"{API_DOADORES}/swagger/",
        "swagger_pacientes": f"{API_PACIENTES}/swagger/",
})

# ==== Página inicial - listagem de solicitações de doação ====
@app.route("/")
def index():
    try:       
        response = requests.get(f"{API_PACIENTES}/solicitacoes/")
        solicitacoes = response.json()
            
        # Aplica HATEOAS em cada item
        for s in solicitacoes:
            links_solicitacao(s)
                
        return render_template('index.html', solicitacoes=solicitacoes)
    except Exception as e:
        return f"Erro ao conectar com API Pacientes (8001): {e}", 500


# ==== Página de uma solicitação específica ====
@app.route("/detalhes-solicitacao/<int:id>")
def detalhes_solicitacao(id):
    try:
        # 1. Busca a solicitação específica (API Pacientes)
        res_paciente = requests.get(f"{API_PACIENTES}/solicitacoes/{id}/")
        print(f"Status Paciente: {res_paciente.status_code}") 
        solicitacao = res_paciente.json()

        # 2. Busca os doadores para o <select> (API Doadores)
        res_doadores = requests.get(f"{API_DOADORES}/doadores/")
        print(f"Status Doadores: {res_doadores.status_code}") 
        doadores = res_doadores.json()

        # 3. Busca os critérios
        res_criterios = requests.get(f"{API_DOADORES}/criterios/")
        todos_criterios = res_criterios.json()

        
        criterios_agrupados = {
            "Requisitos Básicos": [c for c in todos_criterios if c['categoria'] == 'REQ'],
            "Impedimentos Temporários": [c for c in todos_criterios if c['categoria'] == 'IMP_TEMP'],
            "Impedimentos Definitivos": [c for c in todos_criterios if c['categoria'] == 'IMP_DEF'],
        }

       
        return render_template('registrar_doacao.html', 
                               solicitacao=solicitacao, 
                               doadores=doadores, 
                               categorias=criterios_agrupados)

    except Exception as e:
        return f"Erro ao agregar dados das APIs: {e}", 500
    
@app.route("/nova-solicitacao")
def nova_solicitacao():
    res = requests.get(f"{API_PACIENTES}/pacientes/")
    lista_pacientes = res.json()
    
    return render_template("nova_solicitacao.html", pacientes=lista_pacientes)

@app.route("/registrar-solicitacao", methods=['POST'])
def registrar_solicitacao():
    dados = request.form.to_dict()

    # Converte o checkbox 'urgente' para booleano que o Django entende
    dados['urgente'] = 'urgente' in dados
    response = requests.post(f"{API_PACIENTES}/solicitacoes/", json=dados)
    
    if response.status_code == 201:
        return redirect("/") 
    else:
        return f"Erro ao salvar: {response.text}", response.status_code


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


