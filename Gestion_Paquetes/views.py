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

    def run(self):
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

def LoginMenu(Menu):
    def __init__(self):
        super()._init_("Menú de Logueo")
        self.add_option("1", "Loguearse", self.login)
        self.add_option("2", "Registrarse", self.register)
        self.add_option("q", "Salir", self.leave)

    def login(self):
        print("Logueando...")
        LoginMenu().run()

    def register(self):
        print("Registrando...")
        RegisterMenu().run()

def MainMenu(Menu):
    def __init__(self):
        super()._init_("Menú Principal")
        self.add_option("1", "Menú de Paquetes", self.MenuPackage)
        self.add_option("2", "Menú de Envíos", self.MenuShipment)
        self.add_option("3", "Menú de Facturas", self.InvoicesMenu)
        self.add_option("q", "Salir", self.leave)

    def MenuPackage(self):
        print("Ingresando al menú de paquetes...")
        MenuPackage().run()

    def MenuShipment(self):
        print("Ingresando al menú de envíos...")
        MenuShipment().run()

    def InvoicesMenu(self):
        print("Ingresando al menú de facturas...")
        InvoicesMenu().run()

    def leave(self):
        print("Saliendo del sistema...")
        

def MenuPackage(Menu):
    def __init__(self):
        super()._init_("Menú de Paquetes")
        self.add_option("1", "Ver paquetes", self.show_packages)
        self.add_option("2", "Agregar paquete", self.add_package)
        self.add_option("3", "Modificar paquete", self.modify_package)
        self.add_option("4", "Eliminar paquete", self.delete_package)
        self.add_option("e", "Volver", self.back)

    def show_packages(self):
        print("Mostrando paquetes...")
        # Lógica para mostrar paquetes

    def add_package(self):
        print("Agregando paquete...")
        # Lógica para agregar paquete

    def modify_package(self):
        print("Modificando paquete...")
        # Lógica para modificar paquete

    def delete_package(self):
        print("Eliminando paquete...")
        # Lógica para eliminar paquete

    def back(self):
        print("Volviendo al menú principal...")
        MainMenu().run()

def MenuShipment(Menu):
    def __init__(self):
        super()._init_("Menú de Envíos")
        self.add_option("1", "Ver envíos", self.show_shipments)
        self.add_option("2", "Agregar envío", self.add_shipment)
        self.add_option("3", "Modificar envío", self.modify_shipment)
        self.add_option("4", "Eliminar envío", self.delete_shipment)
        self.add_option("e", "Volver", self.back)

    def show_shipments(self):
        print("Mostrando envíos...")
        # Lógica para mostrar envíos

    def add_shipment(self):
        print("Agregando envío...")
        # Lógica para agregar envío

    def modify_shipment(self):
        print("Modificando envío...")
        # Lógica para modificar envío

    def delete_shipment(self):
        print("Eliminando envío...")
        # Lógica para eliminar     
    
    def back(self):
        print("Volviendo al menú principal...")
        MainMenu().run()

def InvoicesMenu(Menu):
    def __init__(self):
        super()._init_("Menú de Facturas")
        self.add_option("1", "Ver facturas", self.show_invoices)
        self.add_option("2", "Eliminar factura", self.delete_invoice)
        self.add_option("e", "Volver", self.back)      

    def show_invoices(self):
        print("Mostrando facturas...")
        # Lógica para mostrar facturas

    def delete_invoice(self):
        print("Eliminando factura...")
        # Lógica para eliminar factura

    def back(self):
        print("Volviendo al menú principal...")
        MainMenu().run()

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
