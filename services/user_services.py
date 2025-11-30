import json
from models.user import User

class UserService:
    FILE = "users.json"

    @staticmethod
    def load_all():
        try:
            with open(UserService.FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        
    @staticmethod
    def save(user: User):
        users = UserService.load_all()
        users.append({
            "nome": user.nome,
            "email": user.email,
            "senha": user.senha
        })
        with open(UserService.FILE, "w") as f:
            json.dump(users, f, indent=4)