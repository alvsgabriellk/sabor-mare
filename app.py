from flask import Flask, request, jsonify, render_template, send_from_directory, redirect
from models.user import User
from services.user_services import UserService

app = Flask(__name__)

@app.route("/css/<path:css>")
def custom_css(css):
    return send_from_directory('css', css)



@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("password")

        if UserService.validar_login(email, senha):
            return redirect("/home")
        else:
            return "Email ou senha incorretos."

    return render_template("login.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        repetir = request.form.get("repetir_senha")

        if "gmail.com" not in email:
            return "Email inválido. Tem que ser gmail."
        
        if senha != repetir:
            return "As senhas não combinam"
        
        if UserService.email_existe(email):
            return "Esse email já está cadastrado."
        
        user = User(nome, email, senha)
        UserService.salvar_usuario(user)

        return redirect("/login")

    return render_template("cadastro.html")



if __name__ == "__main__":
    app.run(debug=True)