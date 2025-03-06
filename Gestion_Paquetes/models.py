class Package:
    def __init__(self, package_id, name, weight, destination):
        self.package_id = package_id
        self.name = name
        self.weight = weight
        self.destination = destination

    def Update(self, name=None, weight=None, destination=None):
        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight
        if destination is not None:
            self.destination = destination

    def __str__(self):
        return f"Package {self.package_id}: {self.name}, {self.weight} kg, {self.destination}"


class User:
    def __init__(self, user_id, name, email, password, address):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.address = address


class Shipment:
    def __init__(self, shipment_id, user, package, cost, date):
        self.shipment_id = shipment_id
        self.user = user
        self.package = package
        self.cost = cost
        self.date = date


class Invoice:
    def __init__(self, invoice_id, user, shipment, cost, date):
        self.invoice_id = invoice_id
        self.user = user
        self.shipment = shipment
        self.cost = cost
        self.date = date    