import pytest
from src.utils import validate_input, generate_id

def test_validate_input():
    """
    Prueba la función validate_input para diferentes casos.
    """
    assert validate_input("username", "password") == True
    assert validate_input("username", "") == False
    assert validate_input("", "password") == False
    assert validate_input(" ", "password") == False

def test_generate_id():
    """
    Prueba la función generate_id para diferentes casos.
    """
    existing_ids = ["U0001", "U0002", "U0003"]
    assert generate_id("U", existing_ids) == "U0004"

    existing_ids = []
    assert generate_id("U", existing_ids) == "U0001"
