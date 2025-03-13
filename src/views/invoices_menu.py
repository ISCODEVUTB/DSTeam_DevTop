from views.menu import Menu
from controllers import PaymentsManager


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

        from views import MainMenu
        print("MESSAGGE_MAIN_MENU")
        MainMenu().run()
