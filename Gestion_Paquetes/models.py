class Package:
    def __init__(self, ID, name, weight, destination):
        self.ID = ID
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
        return f"Package {self.ID}: {self.name}, {self.weight} kg, {self.destination}"


class User:
    def __init__(self, ID,username,password,name, email,address,permissions):
        self.ID = ID
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.address = address
        self.permissions = permissions


class Shipment:
    def __init__(self, ID, userID, package, cost, date, state):
        self.ID = ID
        self.userID = userID
        self.package = package
        self.cost = cost
        self.date = date
        self.state = state


class Invoice:
    def __init__(self, ID, userID, shipment, cost, date):
        self.ID = ID
        self.userID = userID
        self.shipment = shipment
        self.cost = cost
        self.date = date    