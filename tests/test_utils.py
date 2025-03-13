# Test para las funciones de utilidad en src/utils.py
from src.utils import validate_input, generate_id


def test_validate_input():
    """
    Verifica la función validate_input para distintos escenarios:
    - Ambos parámetros no vacíos deben retornar True.
    - Un parámetro vacío o compuesto solo por espacios debe retornar False.
    """
    # Caso: usuario y contraseña válidos
    assert validate_input("username", "password") is True, ("Se espera True "
                                                            "para username y "
                                                            "password válidos.")
    # Caso: contraseña vacía
    assert validate_input("username", "") is False, ("Se espera False "
                                                     "cuando la contraseña "
                                                     " está vacía.")
    # Caso: usuario vacío
    assert validate_input("", "password") is False, ("Se espera False "
                                                     "cuando el username"
                                                     " está vacío.")
    # Caso: username compuesto solo por espacios
    assert validate_input(" ", "password") is False, ("Se espera False "
                                                      "cuando el username "
                                                      "contiene solo espacios.")


def test_generate_id():
    """
    Verifica la función generate_id para la generación correcta de nuevos IDs:
    - Cuando existen IDs previos, se debe generar el siguiente consecutivo.
    - Cuando no existen IDs previos, se debe generar el primer ID.
    """
    # Caso: lista con IDs existentes secuenciales
    existing_ids = ["U0001", "U0002", "U0003"]
    new_id = generate_id("U", existing_ids)
    assert new_id == "U0004", f"Se esperaba 'U0004', pero se obtuvo {new_id}."
    # Caso: lista vacía de IDs existentes
    existing_ids = []
    new_id = generate_id("U", existing_ids)
    assert new_id == "U0001", f"Se esperaba 'U0001', pero se obtuvo {new_id}."
