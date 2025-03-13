from views import Menu, MainMenu, ShipmentMenu, PackageMenu
from views import LoginMenu, InvoicesMenu


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
def test_main_menu_creation():
    main_menu = MainMenu()
    assert main_menu.name == "Menú Principal"


def test_shipment_menu_creation():
    shipment_menu = ShipmentMenu()
    assert shipment_menu.name == "Menú de Envíos"
    assert len(shipment_menu.options) >= 4  # Verificar que tenga al menos 4 opciones


def test_package_menu_creation():
    package_menu = PackageMenu()
    assert package_menu.name == "Menú de Paquetes"
    assert len(package_menu.options) >= 3  # Verificar que tenga al menos 3 opciones


def test_submenu_integration():
    main_menu = MainMenu()
    assert "1" in main_menu.options  # Opción para menú de envíos
    assert "2" in main_menu.options  # Opción para menú de paquetes


# Test para verificar el nombre del menú de login
def test_login_menu_creation():
    login_menu = LoginMenu()
    assert login_menu.name == "Menú de Login"


# Test para verificar el nombre del menú de facturas
def test_invoices_menu_creation():
    invoices_menu = InvoicesMenu()
    assert invoices_menu.name == "Menú de Facturas"
    assert len(invoices_menu.options) >= 2  # Verificar que tenga al menos 2 opciones


# Test para verificar la ejecución de una opción del menú
def test_execute_option_menu():
    menu = Menu("Menú de Prueba")

    def dummy_function():
        return "Ejecutado"

    menu.add_option("1", "Opción de prueba", dummy_function)
    result = menu.execute_option("1")
    assert result == "Ejecutado"


# Test para verificar la eliminación de una opción del menú
def test_remove_option_menu():
    menu = Menu("Menú de Prueba")

    def dummy_function():
        return "Ejecutado"

    menu.add_option("1", "Opción de prueba", dummy_function)
    menu.remove_option("1")
    assert "1" not in menu.options


# Test para verificar la actualización de una opción del menú
def test_update_option_menu():
    menu = Menu("Menú de Prueba")

    def dummy_function():
        return "Ejecutado"

    def new_dummy_function():
        return "Ejecutado Nuevo"

    menu.add_option("1", "Opción de prueba", dummy_function)
    menu.update_option("1", "Opción de prueba actualizada", new_dummy_function)
    assert menu.options["1"][0] == "Opción de prueba actualizada"
    assert menu.execute_option("1") == "Ejecutado Nuevo"


def test_menu_invalid_option():
    menu = Menu("Menú de Prueba")
    assert menu.execute_option("999") is None


def test_menu_display_format():
    menu = Menu("Menú de Prueba")

    def dummy_function():
        # Esta función es un marcador de posición para las pruebas
        # y no realiza ninguna acción.
        pass
    menu.add_option("1", "Primera opción", dummy_function)
    menu.add_option("2", "Segunda opción", dummy_function)
    display = menu.display()
    assert isinstance(display, str)
    assert "Primera opción" in display
    assert "Segunda opción" in display


def test_nested_menus():
    main_menu = MainMenu()
    submenu = ShipmentMenu()
    main_menu.add_submenu("S", "Submenú", submenu)
    assert "S" in main_menu.options
    assert isinstance(main_menu.options["S"][1], ShipmentMenu)
