from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Configurações de URLs das API's
API_DOADORES = "http://127.0.0.1:8000/api/doadores/"
API_PACIENTES = "http://127.0.0.1:8001/api/pacientes/"

@app.route('/')
def home():
    
    user_id = request.args.get('user_id', default=1, type=int)
    
    doador_info = None
    lista_pacientes = []

    try:
        # Busca os dados do doador logado
        res_doador = requests.get(f"{API_DOADORES}?user_id={user_id}", timeout=3)
        if res_doador.status_code == 200:
            dados_busca = res_doador.json() # lista de doadores
            if dados_busca:
                doador_info = dados_busca[0] # Primeiro da lista de doador

        # Busca todos os pacientes
        res_pacientes = requests.get(API_PACIENTES, timeout=3)
        if res_pacientes.status_code == 200:
            lista_pacientes = res_pacientes.json()

    except Exception as e:
        print(f"Erro de conexão: {e}")

    # Envia os dados para o HTML
    return render_template('home.html', 
                           doador=doador_info, 
                           pacientes=lista_pacientes, 
                           atual_id=user_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)
