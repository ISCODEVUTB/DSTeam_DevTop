class Payment:
    def __init__(self, payment_id: str, amount: float):
        self.payment_id = payment_id
        self.amount = amount

    def to_dict(self):
        return {"payment_id": self.payment_id, "amount": self.amount}
