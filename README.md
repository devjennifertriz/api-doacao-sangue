## 🩸 Sistema de Conexão para Doação de Sangue

Este projeto consiste em uma arquitetura de microserviços produzida para a disciplina de desenvolvimento distríbuido 2026.1

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo na ordem exata para garantir que o sistema funcione corretamente.

### 1. Clonagem e Ambiente Virtual
Abra o seu terminal (CMD, PowerShell ou Terminal do VS Code) e execute:
```bash
# Clone o projeto
git clone <url-do-seu-repositorio>
cd <nome-da-pasta>

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Windows (CMD/VS Code):
venv\Scripts\activate
# No Linux/Mac/Codespaces:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```
##Configurando as APis (Django)
### Terminal 1: Api Doadores (Porta 8000)
```bash
cd api_doadores
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8000
```
### Terminal 2: Api Pacientes (Porta 8001)
```bash
cd api_pacientes
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8001
```
### Terminal 3: Gateway (Porta 5000)
```bash
cd gateway
python main.py
```
