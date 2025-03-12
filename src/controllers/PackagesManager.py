from src.controllers.Manager import Manager
from src.models.Package import Package


class PackageManager(Manager):
    def __init__(self):
        super().__init__("Packages")
        self.prefix = "P"  # Prefijo para generar IDs de paquetes

    def add_package(self, description, sizes, weight, type):
        """
        Registra un nuevo paquete en el sistema.
        """
        package_id = self.id_generator()
        new_package = Package(package_id, description, sizes, weight, type)
        self.add_record(new_package.__dict__)
        print(f"Paquete {package_id} registrado con éxito.")

    def update_package(self, package_id, description=None,
                       sizes=None, weight=None, type=None):
        """
        Actualiza los datos de un paquete existente.
        """
        package = self.search_record({"ID": package_id})
        if not package.empty:
            if description is not None:
                package["Description"] = description
            if sizes is not None:
                package["Sizes"] = sizes
            if weight is not None:
                package["Weight"] = weight
            if type is not None:
                package["Type"] = type
            self.edit_record(package.iloc[0].to_dict())
            print(f"Paquete {package_id} actualizado con éxito.")
        else:
            print(f"Error: No se encontró el paquete con ID {package_id}.")

    def delete_package(self, package_id):
        """
        Elimina un paquete del sistema.
        """
        package = self.search_record({"ID": package_id})
        if not package.empty:
            self.delete_record(package.iloc[0].to_dict())
            print(f"Paquete {package_id} eliminado con éxito.")
        else:
            print(f"Error: No se encontró el paquete con ID {package_id}.")

    def search_package(self, search_criteria):
        """
        Busca paquetes basados en criterios específicos.
        """
        result = self.search_record(search_criteria)
        if not result.empty:
            print(result)
        else:
            print("NO_FOUND")
