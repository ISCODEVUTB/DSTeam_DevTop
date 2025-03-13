from views import Menu, PackageMenu, ShipmentMenu, InvoicesMenu
from utils import EXIT_OPTION


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
