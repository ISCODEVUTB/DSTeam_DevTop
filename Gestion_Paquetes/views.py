class Menu:
    def _init_(self, nombre):
        self.nombre = nombre
        self.opciones = {}

    def agregar_opcion(self, clave, descripcion, funcion):
        self.opciones[clave] = (descripcion, funcion)

    def mostrar(self):
        print(f"\n--- {self.nombre} ---")
        for clave, (descripcion, _) in self.opciones.items():
            print(f"{clave}. {descripcion}")
            
    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = input("Seleccione una opción (o 'q' para salir): ")
            if opcion == 'q':
                print("Saliendo del menú...")
                break
            if opcion in self.opciones:
                descripcion, funcion = self.opciones[opcion]
                funcion()
            else:
                print("Opción no válida. Intente de nuevo.")