

class Shipment:
    def __init__(self, shipment_id, user_id, package_id, cost, date, state):
        """
        Representa un envío con un ID, ID de usuario, paquete, costo,
        fecha y estado.
        """
        self.shipment_id = shipment_id
        self.user_id = user_id
        self.package_id = package_id
        self.cost = cost
        self.date = date
        self.state = state

    def __str__(self):
        """
        Devuelve una representación en cadena del envío.
        """
        return (f"Shipment {self.shipment_id}: User {self.user_id}, "
                f"Package {self.package_id}, Cost: {self.cost}, "
                f"Date: {self.date}, State: {self.state}")
