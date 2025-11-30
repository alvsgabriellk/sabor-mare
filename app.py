from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

@app.route("/css/<path:css>")
def custom_css(css):
    return send_from_directory('css', css)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


if __name__ == "__main__":
    app.run(debug=True)