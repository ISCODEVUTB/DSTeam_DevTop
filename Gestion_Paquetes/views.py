class Menu:
    def _init_(self, name):
        self.name = name
        self.options = {}

    def add_option(self, clave, description, funct):
        self.options[clave] = (description, funct)

    def show(self):
        print(f"\n--- {self.name} ---")
        for clave, (description, _) in self.options.items():
            print(f"{clave}. {description}")

    def ejecutar(self):
        while True:
            self.show()
            option = input("Seleccione una opción (o 'q' para salir): ")
            if option == 'q':
                print("Saliendo del menú...")
                break
            if option in self.options:
                description, funct = self.options[option]
                funct()
            else:
                print("Opción no válida. Intente de nuevo.")

def MainMenu(Menu):
    def __init__(self):
        super()._init_("Menú Principal")
        self.add_option("1", "Loguearse", self.login)
        self.add_option("2", "Registrarse", self.register)
        self.add_option("q", "Salir", self.leave)

    def login(self):
        print("Logueando...")
        LoginMenu().ejecutar()

    def register(self):
        print("Registrando...")
        RegisterMenu().ejecutar()

def LoginMenu(Menu):
    def __init__(self):
        super()._init_("Menú de Logueo")
        self.add_option("1", "Ingresar usuario", self.username)
        self.add_option("2", "Ingresar contraseña", self.password)

def RegisterMenu(Menu):
    def __init__(self):
        super()._init_("Menú de Registro")
        self.add_option("1", "Ingresar usuario", self.username)
        self.add_option("2", "Ingresar contraseña", self.password)
