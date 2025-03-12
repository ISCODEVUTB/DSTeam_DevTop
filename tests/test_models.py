import math
from models.models import Package, User, Shipment, Invoice
from datetime import date


# Pruebas para la clase Package
def test_package_creation():
    package = Package("P0001", "Laptop", 2.5, "Bogota", "Calle 123", "Fragil")
    assert package.package_id == "P0001"
    assert package.name == "Laptop"
    assert math.isclose(package.weight, 2.5, rel_tol=1e-09, abs_tol=1e-09)
    assert package.destination == "Bogota"
    assert package.delivery_address == "Calle 123"
    assert package.special_instructions == "Fragil"
    assert str(package) == "Package P0001: Laptop, 2.5 kg, Bogota, Calle 123"


# Pruebas para la clase User
def test_user_creation():
    user = User(
        "U0001", "omar_hernandez", "omar123", "Omar Hernandez",
        "Omarhernandez@gmail.com", "123 Bayunca", "admin"
    )
    assert user.user_id == "U0001"
    assert user.username == "omar_hernandez"
    assert user.password == "omar123"
    assert user.name == "Omar Hernandez"
    assert user.email == "Omarhernandez@gmail.com"
    assert user.address == "123 Bayunca"
    assert user.permissions == "admin"
    assert str(user) == (
        "User U0001: Omar Hernandez (omar_hernandez), "
        "Omarhernandez@gmail.com, 123 Bayunca, Permissions: admin"
    )


# Pruebas para la clase Shipment
def test_shipment_creation():
    package = Package("P0002", "Phone", 0.5,
                      "Los Angeles", "Street 456", "Handle with care")
    shipment = Shipment(
        "S0001", "U0001", package, 50, date(2025, 3, 6), "In Transit",
        "Express", "48h"
    )
    assert shipment.shipment_id == "S0001"
    assert shipment.user_id == "U0001"
    assert shipment.package == package
    assert shipment.cost == 50
    assert shipment.date == date(2025, 3, 6)
    assert shipment.state == "In Transit"
    assert shipment.shipping_type == "Express"
    assert shipment.estimated_time == "48h"
    assert str(shipment) == (
        "Shipment S0001: User U0001, Package P0002, Cost: 50, "
        "Date: 2025-03-06, State: In Transit, Type: Express"
    )


# Pruebas para la clase Invoice
def test_invoice_creation():
    package = Package("P0003", "Tablet", 1.0, "Chicago")
    shipment = Shipment(
        "S0002", "U0002", package, 100, date(2025, 3, 7), "Delivered"
    )
    invoice = Invoice("I0001", "U0002", shipment, 100, date(2025, 3, 8))
    assert invoice.invoice_id == "I0001"
    assert invoice.user_id == "U0002"
    assert invoice.shipment == shipment
    assert invoice.cost == 100
    assert invoice.date == date(2025, 3, 8)
    assert str(invoice) == (
        "Invoice I0001: User U0002, Shipment S0002, Cost: 100, Date: 2025-03-08"
    )
