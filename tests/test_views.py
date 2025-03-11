from views import Menu, MainMenu


# Test para verificar la creación del menú
def test_menu_creation():
    menu = Menu("Menú de Prueba")
    assert menu.name == "Menú de Prueba"


# Test para agregar opciones al menú
def test_add_option():
    menu = Menu("Menú de Prueba")

    def dummy_function():
        return "Ejecutado"

    menu.add_option("1", "Opción de prueba", dummy_function)
    assert "1" in menu.options
    assert menu.options["1"][0] == "Opción de prueba"


# Test para verificar el nombre del menú principal
def test_main_menu():
    main_menu = MainMenu()
    assert main_menu.name == "Menú Principal"
