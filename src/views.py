import pandas as pd
import os
import re
from controllers import PackageManager, ShipmentManager, PaymentsManager, LoginManager
from models import User, Package, Shipment, Invoice

# Constantes para las opciones de menú
LOGIN_OPTION = "1"
REGISTER_OPTION = "2"
EXIT_OPTION = "q"

# Clase base para la creación de menús
class Menu:
    def __init__(self, name):
        """
        Inicializa un nuevo menú.

        :param name: Nombre del menú.
        """
        self.name = name
        self.options = {}

    def add_option(self, clave, description, funct):
        """
        Añade una opción al menú.

        :param clave: Clave de la opción.
        :param description: Descripción de la opción.
        :param funct: Función a ejecutar cuando se selecciona la opción.
        """
        self.options[clave] = (description, funct)

    def show(self):
        """
        Muestra las opciones del menú.
        """
        print(f"\n--- {self.name} ---")
        for clave, (description, _) in self.options.items():
            print(f"{clave}. {description}")

    def run(self):
        """
        Ejecuta el menú, permitiendo al usuario seleccionar opciones.
        """
        while True:
            self.show()
            option = input("Seleccione una opción (o 'q' para salir): ")
            if option == EXIT_OPTION:
                print("Saliendo del menú...")
                break
            if option in self.options:
                _, funct = self.options[option]
                try:
                    funct()
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Opción no válida. Intente de nuevo.")

# Menú de logueo
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

# Menú principal del sistema
class MainMenu(Menu):
    def __init__(self):
        """
        Inicializa el menú principal del sistema.
        """
        super().__init__("Menú Principal")
        self.add_option("1", "Menú de Paquetes", self.menu_package)
        self.add_option("2", "Menú de Envíos", self.menu_shipment)
        self.add_option("3", "Menú de Facturas", self.menu_invoices)
        self.add_option(EXIT_OPTION, "Salir", self.leave)

    def menu_package(self):
        """
        Muestra el menú de paquetes.
        """
        print("Ingresando al menú de paquetes...")
        PackageMenu().run()

    def menu_shipment(self):
        """
        Muestra el menú de envíos.
        """
        print("Ingresando al menú de envíos...")
        ShipmentMenu().run()

    def menu_invoices(self):
        """
        Muestra el menú de facturas.
        """
        print("Ingresando al menú de facturas...")
        InvoicesMenu().run()

    def leave(self):
        """
        Sale del sistema.
        """
        print("Saliendo del sistema...")

# Menú para la gestión de paquetes
class PackageMenu(Menu):
    def __init__(self):
        """
        Inicializa el menú de gestión de paquetes.
        """
        super().__init__("Menú de Paquetes")
        self.add_option("1", "Ver paquetes", self.show_packages)
        self.add_option("2", "Agregar paquete", self.add_package)
        self.add_option("3", "Modificar paquete", self.modify_package)
        self.add_option("4", "Eliminar paquete", self.delete_package)
        self.add_option("e", "Volver", self.back)

    def show_packages(self):
        """
        Muestra los paquetes.
        """
        print("Mostrando paquetes...")
        pm = PackageManager()
        pm.show()

    def add_package(self):
        """
        Permite agregar un nuevo paquete.
        """
        print("Agregando paquete...")
        pm = PackageManager()
        pm.add_package()

    def modify_package(self):
        """
        Permite modificar un paquete existente.
        """
        print("Modificando paquete...")
        pm = PackageManager()
        pm.edit_record()

    def delete_package(self):
        """
        Permite eliminar un paquete.
        """
        print("Eliminando paquete...")
        pm = PackageManager()
        pm.delete_package()

    def back(self):
        """
        Vuelve al menú principal.
        """
        print("Volviendo al menú principal...")
        MainMenu().run()

# Menú para la gestión de envíos
class ShipmentMenu(Menu):
    def __init__(self):
        """
        Inicializa el menú de gestión de envíos.
        """
        super().__init__("Menú de Envíos")
        self.add_option("1", "Ver envíos", self.show_shipments)
        self.add_option("2", "Agregar envío", self.add_shipment)
        self.add_option("3", "Modificar envío", self.modify_shipment)
        self.add_option("4", "Eliminar envío", self.delete_shipment)
        self.add_option("e", "Volver", self.back)

    def show_shipments(self):
        """
        Muestra los envíos.
        """
        print("Mostrando envíos...")
        sm = ShipmentManager()
        sm.show()

    def add_shipment(self):
        """
        Permite agregar un nuevo envío.
        """
        print("Agregando envío...")
        sm = ShipmentManager()
        sm.create_shipment()

    def modify_shipment(self):
        """
        Permite modificar un envío existente.
        """
        print("Modificando envío...")
        sm = ShipmentManager()
        sm.update_shipment_state()

    def delete_shipment(self):
        """
        Permite eliminar un envío.
        """
        print("Eliminando envío...")
        sm = ShipmentManager()
        shipment_id = input("Ingrese el ID del envío a eliminar: ")
        sm.delete_record({"ID": shipment_id})
        print("Envío eliminado (si el ID fue encontrado).")

    def back(self):
        """
        Vuelve al menú principal.
        """
        print("Volviendo al menú principal...")
        MainMenu().run()

# Menú para la gestión de facturas
class InvoicesMenu(Menu):
    def __init__(self):
        """
        Inicializa el menú de gestión de facturas.
        """
        super().__init__("Menú de Facturas")
        self.add_option("1", "Ver facturas", self.show_invoices)
        self.add_option("2", "Generar factura", self.generate_invoice)
        self.add_option("3", "Eliminar factura", self.delete_invoice)
        self.add_option("e", "Volver", self.back)

    def show_invoices(self):
        """
        Muestra las facturas.
        """
        print("Mostrando facturas...")
        im = PaymentsManager()
        im.show()

    def generate_invoice(self):
        """
        Permite generar una nueva factura.
        """
        print("Generando factura...")
        im = PaymentsManager()
        invoice_data = {
            "ID": input("Ingrese el ID de la factura: "),
            "Cliente": input("Ingrese el nombre del cliente: "),
            "Monto": input("Ingrese el monto de la factura: "),
            "Fecha": input("Ingrese la fecha de la factura: ")
        }
        im.create_invoice(invoice_data)
        print("Factura generada.")

    def delete_invoice(self):
        """
        Permite eliminar una factura.
        """
        print("Eliminando factura...")
        im = PaymentsManager()
        invoice_id = input("Ingrese el ID de la factura a eliminar: ")
        im.delete_record({"ID": invoice_id})
        print("Factura eliminada (si el ID fue encontrado).")

    def back(self):
        """
        Vuelve al menú principal.
        """
        print("Volviendo al menú principal...")
        MainMenu().run()


if __name__ == "__main__":
    main_menu = LoginMenu()
    main_menu.run()
