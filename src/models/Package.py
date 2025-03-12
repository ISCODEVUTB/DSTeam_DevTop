

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
