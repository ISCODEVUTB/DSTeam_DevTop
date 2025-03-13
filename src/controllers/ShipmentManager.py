from models import Shipment
from controllers.Manager import Manager
from utils import NO_FOUND


class ShipmentManager(Manager):
    def __init__(self):
        super().__init__("Shipments")
        self.prefix = "S"  # Prefijo para generar IDs de envíos

    def create_shipment(self, user_id, package_id, cost, date, state):
        """
        Crea un nuevo envío en el sistema.
        """
        shipment_id = self.id_generator()
        new_shipment = Shipment(shipment_id, user_id, package_id, cost, date, state)
        self.add_record(new_shipment.__dict__)
        print(f"Envío {shipment_id} creado con éxito.")

    def update_shipment_state(self, shipment_id, new_state):
        """
        Actualiza el estado de un envío existente.
        """
        shipment = self.search_record({"ID": shipment_id})
        if not shipment.empty:
            shipment["State"] = new_state
            self.edit_record(shipment.iloc[0].to_dict())
            print(f"Estado del envío {shipment_id} actualizado a {new_state}.")
        else:
            print(f"Error: No se encontró el envío con ID {shipment_id}.")

    def delete_shipment(self, shipment_id):
        """
        Elimina un envío del sistema.
        """
        shipment = self.search_record({"ID": shipment_id})
        if not shipment.empty:
            self.delete_record(shipment.iloc[0].to_dict())
            print(f"Envío {shipment_id} eliminado con éxito.")
        else:
            print(f"Error: No se encontró el envío con ID {shipment_id}.")

    def search_shipment(self, search_criteria):
        """
        Busca envíos basados en criterios específicos.
        """
        result = self.search_record(search_criteria)
        if not result.empty:
            print(result)
        else:
            print(NO_FOUND)
