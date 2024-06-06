from flask import Flask, render_template, request, redirect, url_for
from verificar_login import verificar_login

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login_action', methods=['POST'])
def login_action():
    username = request.form['username']
    senha = request.form['password']
    if verificar_login(username, senha):
        return redirect(url_for('main_menu'))
    else:
        return "Usuário ou senha incorretos!"

@app.route('/main_menu')
def main_menu():
    return "Login bem-sucedido! Bem-vindo ao menu principal."

if __name__ == '__main__':
    app.run(debug=True)
