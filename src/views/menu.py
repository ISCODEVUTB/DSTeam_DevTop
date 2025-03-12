from utils.constants import EXIT_OPTION


class Menu:
    def __init__(self, name):
        """
        Inicializa un nuevo menú.

        :param name: Nombre del menú.
        """
        self.name = name
        self.options = {}

    def add_option(self, clave, description, funct):
        """
        Añade una opción al menú.

        :param clave: Clave de la opción.
        :param description: Descripción de la opción.
        :param funct: Función a ejecutar cuando se selecciona la opción.
        """
        self.options[clave] = (description, funct)

    def show(self):
        """
        Muestra las opciones del menú.
        """
        print(f"\n--- {self.name} ---")
        for clave, (description, _) in self.options.items():
            print(f"{clave}. {description}")

    def run(self):
        """
        Ejecuta el menú, permitiendo al usuario seleccionar opciones.
        """
        while True:
            self.show()
            option = input("Seleccione una opción (o 'q' para salir): ")
            if option == EXIT_OPTION:
                print("Saliendo del menú...")
                break
            if option in self.options:
                _, funct = self.options[option]
                try:
                    funct()
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Opción no válida. Intente de nuevo.")
