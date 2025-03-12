from models.models import User, Package, Shipment, Invoice


def test_user_creation():
    user = User("John Doe", "john@example.com", "password123")
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.verify_password("password123")


def test_package_creation():
    package = Package("Test Package", 2.5, "Small")
    assert package.description == "Test Package"
    assert package.weight == 2.5
    assert package.size == "Small"


def test_shipment_creation():
    shipment = Shipment("Origin", "Destination", "Express")
    assert shipment.origin == "Origin"
    assert shipment.destination == "Destination"
    assert shipment.shipping_type == "Express"


def test_invoice_creation():
    invoice = Invoice(100.0, "Pending")
    assert invoice.amount == 100.0
    assert invoice.status == "Pending"
