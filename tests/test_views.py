from views.views import Menu, MainMenu, ShipmentMenu, PackageMenu


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


def test_shipment_menu():
    shipment_menu = ShipmentMenu()
    assert shipment_menu.name == "Menú de Envíos"
    assert len(shipment_menu.options) >= 4  # Verificar que tenga al menos 4 opciones


def test_package_menu():
    package_menu = PackageMenu()
    assert package_menu.name == "Menú de Paquetes"
    assert len(package_menu.options) >= 3  # Verificar que tenga al menos 3 opciones


def test_submenu_integration():
    main_menu = MainMenu()
    assert "1" in main_menu.options  # Opción para menú de envíos
    assert "2" in main_menu.options  # Opción para menú de paquetes
