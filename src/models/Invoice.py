

class Invoice:
    def __init__(self, invoice_id, user_id, shipment_id, cost, date):
        """
        Representa una factura con un ID, ID de usuario, envío, costo y fecha.
        """
        self.invoice_id = invoice_id
        self.user_id = user_id
        self.shipment_id = shipment_id
        self.cost = cost
        self.date = date

    def __str__(self):
        """
        Devuelve una representación en cadena de la factura.
        """
        return (f"Invoice {self.invoice_id}: User {self.user_id}, "
                f"Shipment {self.shipment_id}, Cost: {self.cost}, "
                f"Date: {self.date}")
