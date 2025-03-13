# Test para la clase Menu y MainMenu
from views import Menu, MainMenu


def test_menu_creation():
    """
    Verifica que al crear un objeto Menu se asigne correctamente el nombre
    y se inicialice el diccionario de opciones de forma adecuada.
    """
    menu = Menu("Menú de Prueba")
    # Verifica el nombre
    assert menu.name == "Menú de Prueba", "El nombre debe ser 'Menú de Prueba'."
    # Comprueba que el atributo 'options' exista y sea un diccionario vacío
    assert hasattr(menu, "options"), "El menú debe tener un atributo 'options'."
    assert isinstance(menu.options, dict), "'options' debe ser un diccionario."
    assert len(menu.options) == 0, "'options' debe estar vacío al crear el menú."


def test_add_option():
    """
    Verifica que se pueda agregar una opción al menú y que se almacene
    con la estructura esperada (descripción y función asociada).
    """
    menu = Menu("Menú de Prueba")

    def dummy_function():
        return "Ejecutado"
    menu.add_option("1", "Opción de prueba", dummy_function)
    # Verifica que la opción se haya agregado al diccionario
    assert "1" in menu.options, "La clave '1' debe existir en 'options'."
    # Se asume que cada opción se almacena como una tupla o lista (descripción, función)
    option = menu.options["1"]
    assert isinstance(option, (tuple, list)), "debe almacenarse como tuple o list."
    assert option[0] == "Opción de prueba", "La descripción de la opción no coincide."
    assert callable(option[1]), "El segundo elemento debe ser una función callable."
    # Verifica que la función asociada retorne el valor esperado
    result = option[1]()
    assert result == "Ejecutado", "no retorna 'Ejecutado'."


def test_main_menu():
    """
    Verifica que al crear un objeto MainMenu se asigne correctamente el nombre,
    y opcionalmente que se inicialicen otros atributos como 'options'.
    """
    main_menu = MainMenu()
    # Verifica el nombre del menú principal
    assert main_menu.name == "Menú Principal", "El nombre debe ser 'Menú Principal'."
    # Verifica que 'options' exista y sea un diccionario
    assert hasattr(main_menu, "options"), "El menú debe tener un atributo 'options'."
    assert isinstance(main_menu.options, dict), "'options' debe ser un diccionario."
