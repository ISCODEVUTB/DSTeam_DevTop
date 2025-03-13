from controllers import PackageManager
from views import Menu, MainMenu


class PackageMenu(Menu):
    def __init__(self):
        """
        Inicializa el menú de gestión de paquetes.
        """
        super().__init__("Menú de Paquetes")
        self.add_option("1", "Ver paquetes", self.show_packages)
        self.add_option("2", "Agregar paquete", self.add_package)
        self.add_option("3", "Modificar paquete", self.modify_package)
        self.add_option("4", "Eliminar paquete", self.delete_package)
        self.add_option("e", "Volver", self.back)

    def show_packages(self):
        """
        Muestra los paquetes.
        """
        print("Mostrando paquetes...")
        pm = PackageManager()
        pm.show()

    def add_package(self):
        """
        Permite agregar un nuevo paquete.
        """
        print("Agregando paquete...")
        pm = PackageManager()

        package_description = input("Ingrese la descripción del paquete: ")
        package_sizes = input("Ingrese las dimensiones del paquete: ")
        package_type = input("Ingrese el tipo del paquete: ")
        package_weight = input("Ingrese el peso del paquete: ")
        pm.add_package(package_description, package_sizes, package_weight, package_type)

    def modify_package(self):
        """
        Permite modificar un paquete existente.
        """
        print("Modificando paquete...")
        pm = PackageManager()
        package_id = input("Ingrese el ID del paquete a modificar: ")
        package_description = input("Ingrese la nueva descripción del paquete: ")
        package_sizes = input("Ingrese las nuevas dimensiones del paquete: ")
        package_weight = input("Ingrese el nuevo peso del paquete: ")
        package_type = input("Ingrese el nuevo tipo del paquete: ")
        pm.update_package(package_id,
                          package_description,
                          package_sizes, package_weight,
                          package_type)

    def delete_package(self):
        """
        Permite eliminar un paquete.
        """
        print("Eliminando paquete...")
        pm = PackageManager()
        package_id = input("Ingrese el ID del paquete a eliminar: ")
        pm.delete_package(package_id)

    def back(self):
        """
        Vuelve al menú principal.
        """
        print("MESSAGGE_MAIN_MENU")
        MainMenu().run()
