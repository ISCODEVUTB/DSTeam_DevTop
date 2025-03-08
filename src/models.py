class Package:
    def __init__(self, package_id, description, sizes, weight, type):
        """
        Representa un paquete con un ID, nombre, peso y destino.
        """
        self.package_id = package_id
        self.description = description
        self.sizes = sizes
        self.weight = weight
        self.type = type

    def __str__(self):
        """
        Devuelve una representación en cadena del paquete.
        """
        return (f"Package {self.package_id}: {self.description}, "
                f"Sizes: {self.sizes}, Weight: {self.weight}, Type: {self.type}")


class User:
    def __init__(self, user_id, username, password, name, email, address, permissions):
        """
        Representa un usuario con un ID, nombre de usuario, contraseña,
        nombre, email, dirección y permisos.
        """
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.address = address
        self.permissions = permissions

    def __str__(self):
        """
        Devuelve una representación en cadena del usuario.
        """
        return (f"User {self.user_id}: {self.name} ({self.username}), "
                f"{self.email}, {self.address}, Permissions: {self.permissions}")


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