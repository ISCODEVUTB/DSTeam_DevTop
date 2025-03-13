import pytest

from models.Invoice import Invoice
from models.Package import Package
from models.Shipment import Shipment
from models.User import User


@pytest.fixture
def sample_user():
    return User(
        "U001",
        "testuser",
        "password123",
        "Test User",
        "test@email.com",
        "Test Address",
        "user"
    )


@pytest.fixture
def sample_package():
    return Package(
        "P001",
        "Test Package",
        "10x10x10",
        1.5,
        "Normal"
    )


@pytest.fixture
def sample_shipment():
    return Shipment(
        "S001",
        "U001",
        "P001",
        100.0,
        "2024-01-01",
        "En proceso"
    )


@pytest.fixture
def sample_invoice():
    return Invoice(
        "I001",
        "U001",
        "S001",
        100.0,
        "2024-01-01"
    )


def test_user_attributes(sample_user):
    assert sample_user.user_id == "U001"
    assert sample_user.username == "testuser"
    assert sample_user.password == "password123"
    assert sample_user.name == "Test User"
    assert sample_user.email == "test@email.com"
    assert sample_user.address == "Test Address"
    assert sample_user.permissions == "user"


def test_package_attributes(sample_package):
    assert sample_package.package_id == "P001"
    assert sample_package.description == "Test Package"
    assert sample_package.sizes == "10x10x10"
    assert abs(sample_package.weight - 1.5) < 1e-9
    assert sample_package.type == "Normal"


def test_shipment_attributes(sample_shipment):
    assert sample_shipment.shipment_id == "S001"
    assert sample_shipment.user_id == "U001"
    assert sample_shipment.package_id == "P001"
    assert abs(sample_shipment.cost - 100.0) < 1e-9
    assert sample_shipment.date == "2024-01-01"
    assert sample_shipment.state == "En proceso"


def test_invoice_attributes(sample_invoice):
    assert sample_invoice.invoice_id == "I001"
    assert sample_invoice.user_id == "U001"
    assert sample_invoice.shipment_id == "S001"
    assert abs(sample_invoice.cost - 100.0) < 1e-9
    assert sample_invoice.date == "2024-01-01"


def test_user_str_representation(sample_user):
    expected = (
        "User U001: Test User (testuser), test@email.com, "
        "Test Address, Permissions: user"
    )
    assert str(sample_user) == expected


def test_package_str_representation(sample_package):
    expected = "Package P001: Test Package, Sizes: 10x10x10, Weight: 1.5, Type: Normal"
    assert str(sample_package) == expected


def test_shipment_str_representation(sample_shipment):
    expected = (
        "Shipment S001: User U001, Package P001, Cost: 100.0, "
        "Date: 2024-01-01, State: En proceso"
    )
    assert str(sample_shipment) == expected


def test_invoice_str_representation(sample_invoice):
    expected = "Invoice I001: User U001, Shipment S001, Cost: 100.0, Date: 2024-01-01"
    assert str(sample_invoice) == expected
