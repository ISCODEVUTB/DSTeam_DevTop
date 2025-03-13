# Test de los modelos de la aplicación.
import math
from datetime import date
from models import Package, User, Shipment, Invoice


def test_package_creation():
    """Test de creación de un objeto Package y validación de sus atributos."""
    package = Package("P0001", "Laptop", "30x10x5", 2.5, "Bogota", "Normal")
    assert package.package_id == "P0001", "El ID del paquete no coincide."
    assert package.description == "Laptop", "El nombre del paquete no coincide."
    assert math.isclose(
        package.weight,
        2.5,
        rel_tol=1e-09,
        abs_tol=1e-09
    ), "El peso del paquete no es correcto."
    assert package.sizes == "30x10x5", "Las dimensiones del paquete no son correctas."
    assert package.destination == "Bogota", "El destino del paquete no coincide."
    assert package.type == "Normal", "El tipo de paquete no coincide."
    expected_str = (
        "Package P0001: Laptop, 30x10x5, 2.5 kg,"
        " Destination: Bogota, Type: Normal"
    )
    assert str(package) == expected_str


def test_user_creation():
    """Test de creación de un objeto User y validación de sus atributos."""
    user = User(
        "U0001",
        "omar_hernandez",
        "omar123",
        "Omar Hernandez",
        "Omarhernandez@gmail.com",
        "123 Bayunca",
        "admin"
    )
    assert user.user_id == "U0001", "El ID del usuario no coincide."
    assert user.username == "omar_hernandez", "El nombre de usuario no coincide."
    assert user.password == "omar123", "La contraseña no coincide."
    assert user.name == "Omar Hernandez", "El nombre completo no coincide."
    assert user.email == "Omarhernandez@gmail.com", "El email no coincide."
    assert user.address == "123 Bayunca", "La dirección no coincide."
    assert user.permissions == "admin", "Los permisos no coinciden."
    expected_str = (
        "User U0001: Omar Hernandez (omar_hernandez), "
        "Omarhernandez@gmail.com, 123 Bayunca, Permissions: admin"
    )
    assert str(user) == expected_str, f"__str__ del usuario debe ser '{expected_str}'."


def test_shipment_creation():
    """Test de creación de un objeto Shipment y validación de sus atributos."""
    package = Package("P0002", "Phone", "30x10x2", 0.5, "Los Angeles", "Normal")
    shipment_date = date(2025, 3, 6)
    shipment = Shipment(
        "S0001",
        "U0001",
        package.package_id,
        50,
        shipment_date,
        "In Transit"
    )
    assert shipment.shipment_id == "S0001", "El ID del envío no coincide."
    assert shipment.user_id == "U0001", "El ID del usuario en el envío no coincide."
    assert shipment.package_id == "P0002", "El paquete del envío no coincide."
    assert shipment.cost == 50, "El costo del envío no coincide."
    assert shipment.date == shipment_date, "La fecha del envío no coincide."
    assert shipment.state == "In Transit", "El estado del envío no coincide."
    expected_str = (
        "Shipment S0001: User U0001, Package P0002, Cost: 50,"
        " Date: 2025-03-06, State: In Transit"
    )
    assert str(shipment) == expected_str


def test_invoice_creation():
    """Test de creación de un objeto Invoice y validación de sus atributos."""
    shipment_date = date(2025, 3, 7)
    invoice_date = date(2025, 3, 8)
    shipment = Shipment(
        "S0002",
        "U0002",
        "P0003",
        100,
        shipment_date,
        "Delivered"
    )
    invoice = Invoice(
        "I0001",
        "U0002",
        shipment.shipment_id,
        100,
        invoice_date
    )
    assert invoice.invoice_id == "I0001", "El ID de la factura no coincide."
    assert invoice.user_id == "U0002", "El ID del usuario en la factura no coincide."
    assert invoice.shipment_id == "S0002", "El envío asociado a la factura no coincide."
    assert invoice.cost == 100, "El costo en la factura no coincide."
    assert invoice.date == invoice_date, "La fecha de la factura no coincide."
    expected_str = (
        "Invoice I0001: User U0002, Shipment S0002,"
        " Cost: 100, Date: 2025-03-08"
    )
    assert str(invoice) == expected_str
