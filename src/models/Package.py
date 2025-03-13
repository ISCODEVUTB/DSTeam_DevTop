

class Package:
    def __init__(self, package_id, description, sizes, weight, destination, type):
        """
        Representa un paquete con un ID, nombre, peso y destino.
        """
        self.package_id = package_id
        self.description = description
        self.sizes = sizes
        self.weight = weight
        self.destination = destination
        self.type = type

    def __str__(self):
        """
        Devuelve una representación en cadena del paquete.
        """
        return (f"Package {self.package_id}: {self.description}, {self.sizes}, "
                f"{self.weight} kg, Destination: {self.destination}, Type: {self.type}")
