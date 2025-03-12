from controllers.controllers import LoginManager
from views.views import Menu
from utils.constants import LOGIN_OPTION, REGISTER_OPTION, EXIT_OPTION


class LoginMenu(Menu):
    def __init__(self):
        """
        Inicializa el menú de logueo.
        """
        super().__init__("Menú de Logueo")
        self.add_option(LOGIN_OPTION, "Loguearse", self.login)
        self.add_option(REGISTER_OPTION, "Registrarse", self.register)
        self.add_option(EXIT_OPTION, "Salir", self.leave)

    def login(self):
        """
        Permite al usuario loguearse.
        """
        print("Logueando...")
        lm = LoginManager()
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        lm.login(username, password)

    def register(self):
        """
        Permite al usuario registrarse.
        """
        print("Registrando...")
        lm = LoginManager()
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        name = input("Ingrese su nombre: ")
        email = input("Ingrese su correo electrónico: ")
        address = input("Ingrese su dirección: ")
        permission = input("Ingrese su permiso (admin/user): ")
        lm.sign_in(username, password, name, email, address, permission)

    def leave(self):
        """
        Sale del sistema.
        """
        print("Saliendo del sistema...")
