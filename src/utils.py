import re

def validate_input(*args):
    """
    Valida que los campos de entrada no estén vacíos.
    """
    for arg in args:
        if not arg or str(arg).strip() == "":
            return False
    return True

def generate_id(prefix, existing_ids):
    """
    Genera un ID único basado en los IDs existentes.
    El formato del ID es: prefijo + número (ejemplo: U0001, P0001).
    """
    numbers = [int(re.search(r'\d+', id).group()) for id in existing_ids if re.search(r'\d+', id)]
    next_number = max(numbers) + 1 if numbers else 1
    return f"{prefix}{next_number:04d}"
