from models import Invoice
from controllers import Manager


class InvoiceManager(Manager):
    def __init__(self):
        super().__init__("Invoices")
        self.prefix = "I"  # Prefijo para generar IDs de facturas

    def generate_invoice(self, user_id, shipment_id, cost, date):
        """
        Genera una nueva factura en el sistema.
        """
        invoice_id = self.id_generator()
        new_invoice = Invoice(invoice_id, user_id, shipment_id, cost, date)
        self.add_record(new_invoice.__dict__)
        print(f"Factura {invoice_id} generada con éxito.")

    def update_invoice(self, invoice_id, cost=None, date=None):
        """
        Actualiza los datos de una factura existente.
        """
        invoice = self.search_record({"ID": invoice_id})
        if not invoice.empty:
            if cost is not None:
                invoice["Cost"] = cost
            if date is not None:
                invoice["Date"] = date
            self.edit_record(invoice.iloc[0].to_dict())
            print(f"Factura {invoice_id} actualizada con éxito.")
        else:
            print(f"Error: No se encontró la factura con ID {invoice_id}.")

    def delete_invoice(self, invoice_id):
        """
        Elimina una factura del sistema.
        """
        invoice = self.search_record({"ID": invoice_id})
        if not invoice.empty:
            self.delete_record(invoice.iloc[0].to_dict())
            print(f"Factura {invoice_id} eliminada con éxito.")
        else:
            print(f"Error: No se encontró la factura con ID {invoice_id}.")

    def search_invoice(self, search_criteria):
        """
        Busca facturas basadas en criterios específicos.
        """
        result = self.search_record(search_criteria)
        if not result.empty:
            print(result)
        else:
            print("NO_FOUND")
