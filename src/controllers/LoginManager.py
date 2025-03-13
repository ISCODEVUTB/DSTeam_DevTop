from controllers import Manager
from models import User
from utils import validate_input


class LoginManager(Manager):
    def __init__(self):
        super().__init__("Users")
        self.prefix = "U"  # Prefijo para generar IDs de usuarios

    def login(self, username, password):
        """
        Autentica a un usuario en el sistema.
        """
        if not validate_input(username, password):
            print("Error: El nombre de usuario y la contraseña no pueden estar vacíos.")
            return False

        # Buscar el usuario en los registros
        user = self.search_record({"Username": username, "Password": password})
        if not user.empty:
            print(f"Bienvenido, {username}!")
            return True
        else:
            print("Error: Usuario o contraseña incorrectos.")
            return False

    def sign_in(self, username, password, name, email, address, permissions):
        """
        Registra un nuevo usuario en el sistema.
        """
        if not validate_input(username, password, name, email):
            print("Error: Todos los campos obligatorios deben ser completados.")
            return

        # Verificar si el usuario ya existe
        if not self.search_record({"Username": username}).empty:
            print("Error: El nombre de usuario ya está en uso.")
            return

        # Generar un ID único para el nuevo usuario
        user_id = self.id_generator()

        # Crear el nuevo usuario y agregarlo al sistema
        new_user = User(user_id, username, password, name, email, address, permissions)
        self.add_record(new_user.__dict__)
        print(f"Usuario {username} registrado con éxito.")
