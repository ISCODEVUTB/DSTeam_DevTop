from .Manager import Manager


class PaymentsManager(Manager):
    def __init__(self):
        super().__init__("Payments")
        self.data = None
        self.save_data()

    def AddPayment(self, payment):
        self.AddRecord(payment)

    def ShowPayments(self):
        self.Show()
