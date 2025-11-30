import json
import os
from models.user import User

CAMINHO_ARQUIVO = "data/usuarios.json"

class UserService:

    @staticmethod
    def carregar_usuarios():
        if not os.path.exists(CAMINHO_ARQUIVO):
            return []

        with open(CAMINHO_ARQUIVO, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    @staticmethod
    def salvar_usuario(user: User):
        usuarios = UserService.carregar_usuarios()

        usuarios.append({
            "nome": user.nome,
            "email": user.email,
            "senha": user.senha
        })

        with open(CAMINHO_ARQUIVO, "w") as f:
            json.dump(usuarios, f, indent=4)

    @staticmethod
    def email_existe(email):
        usuarios = UserService.carregar_usuarios()

        for u in usuarios:
            if u["email"] == email:
                return True
        return False

    @staticmethod
    def validar_login(email, senha):
        usuarios = UserService.carregar_usuarios()

        for u in usuarios:
            if u["email"] == email and u["senha"] == senha:
                return True
        return False
