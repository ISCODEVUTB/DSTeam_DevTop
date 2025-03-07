import pandas as pd
import os
import re
from controllers import PackageManager, ShipmentManager, PaymentsManager, LoginManager
from models import User, Package, Shipment, Invoice

# Clase base para la creación de menús
class Menu:
    def __init__(self, name):
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
                _, funct = self.options[option]
                funct()
            else:
                print("Opción no válida. Intente de nuevo.")

# Menú de logueo
class LoginMenu(Menu):
    def __init__(self):
        super().__init__("Menú de Logueo")
        self.add_option("1", "Loguearse", self.login)
        self.add_option("2", "Registrarse", self.register)
        self.add_option("q", "Salir", self.leave)

    def login(self):
        print("Logueando...")
        lm = LoginManager()
        lm.login()

    def register(self):
        print("Registrando...")
        lm = LoginManager()
        lm.sign_in()

    def leave(self):
        print("Saliendo del sistema...")

# Menú principal del sistema
class MainMenu(Menu):
    def __init__(self):
        super().__init__("Menú Principal")
        self.add_option("1", "Menú de Paquetes", self.menu_package)
        self.add_option("2", "Menú de Envíos", self.menu_shipment)
        self.add_option("3", "Menú de Facturas", self.invoices_menu)
        self.add_option("q", "Salir", self.leave)

    def menu_package(self):
        print("Ingresando al menú de paquetes...")
        MenuPackage().run()

    def menu_shipment(self):
        print("Ingresando al menú de envíos...")
        MenuShipment().run()

    def invoices_menu(self):
        print("Ingresando al menú de facturas...")
        InvoicesMenu().run()

    def leave(self):
        print("Saliendo del sistema...")

# Menú para la gestión de paquetes
class MenuPackage(Menu):
    def __init__(self):
        super().__init__("Menú de Paquetes")
        self.add_option("1", "Ver paquetes", self.show_packages)
        self.add_option("2", "Agregar paquete", self.add_package)
        self.add_option("3", "Modificar paquete", self.modify_package)
        self.add_option("4", "Eliminar paquete", self.delete_package)
        self.add_option("e", "Volver", self.back)

    def show_packages(self):
        print("Mostrando paquetes...")
        pm = PackageManager()
        pm.Show()

    def add_package(self):
        print("Agregando paquete...")
        pm = PackageManager()
        pm.AddPackage()

    def modify_package(self):
        print("Modificando paquete...")
        pm = PackageManager()
        pm.EditPackage()

    def delete_package(self):
        print("Eliminando paquete...")
        pm = PackageManager()
        pm.DeletePackage()

    def back(self):
        print("Volviendo al menú principal...")
        MainMenu().run()

# Menú para la gestión de envíos
class MenuShipment(Menu):
    def __init__(self):
        super().__init__("Menú de Envíos")
        self.add_option("1", "Ver envíos", self.show_shipments)
        self.add_option("2", "Agregar envío", self.add_shipment)
        self.add_option("3", "Modificar envío", self.modify_shipment)
        self.add_option("4", "Eliminar envío", self.delete_shipment)
        self.add_option("e", "Volver", self.back)

    def show_shipments(self):
        print("Mostrando envíos...")
        sm = ShipmentManager()
        sm.Show()

    def add_shipment(self):
        print("Agregando envío...")
        sm = ShipmentManager()
        sm.CreateShipment()

    def modify_shipment(self):
        print("Modificando envío...")
        sm = ShipmentManager()
        sm.UpdateShipmentStatus()

    def delete_shipment(self):
        print("Eliminando envío...")
        sm = ShipmentManager()
        shipment_id = input("Ingrese el ID del envío a eliminar: ")
        sm.DeletedRecord({"ID": shipment_id})
        print("Envío eliminado (si el ID fue encontrado).")

    def back(self):
        print("Volviendo al menú principal...")
        MainMenu().run()

# Menú para la gestión de facturas
class InvoicesMenu(Menu):
    def __init__(self):
        super().__init__("Menú de Facturas")
        self.add_option("1", "Ver facturas", self.show_invoices)
        self.add_option("2", "Generar factura", self.generate_invoice)
        self.add_option("3", "Eliminar factura", self.delete_invoice)
        self.add_option("e", "Volver", self.back)

    def show_invoices(self):
        print("Mostrando facturas...")
        im = PaymentsManager()
        im.Show()

    def generate_invoice(self):
        print("Generando factura...")
        im = PaymentsManager()
        im.GenerateInvoice()

    def delete_invoice(self):
        print("Eliminando factura...")
        im = PaymentsManager()
        invoice_id = input("Ingrese el ID de la factura a eliminar: ")
        im.DeletedRecord({"ID": invoice_id})
        print("Factura eliminada (si el ID fue encontrado).")

    def back(self):
        print("Volviendo al menú principal...")
        MainMenu().run()


if __name__ == "__main__":
    main_menu = LoginMenu()
    main_menu.run()
