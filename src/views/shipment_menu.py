from controllers import ShipmentManager
from views.menu import Menu


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

        user_id = input("Ingrese el ID del envío: ")
        package_id = input("Ingrese el ID del paquete: ")
        cost = input("Ingrese el destino del envío: ")
        shipment_date = input("Ingrese la fecha del envío: ")
        status = input("Ingrese el estado del envío: ")
        sm.create_shipment(user_id, package_id, cost, shipment_date, status)

    def modify_shipment(self):
        """
        Permite modificar un envío existente.
        """
        print("Modificando envío...")
        sm = ShipmentManager()
        shipment_id = input("Ingrese el ID del envío a modificar: ")
        new_state = input("Ingrese el nuevo estado del envío: ")
        sm.update_shipment_state(shipment_id, new_state)

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

        from views import MainMenu
        print("MESSAGGE_MAIN_MENU")
        MainMenu().run()
