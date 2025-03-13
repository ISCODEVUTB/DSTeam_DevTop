import pytest
from controllers.InvoicesManager import InvoiceManager


@pytest.fixture
def invoice_manager():
    """Fixture para crear una instancia de InvoiceManager."""
    return InvoiceManager()


def test_generate_invoice(invoice_manager, mocker):
    """Prueba la generación de una factura."""
    mock_add = mocker.patch(
        'controllers.InvoicesManager.InvoiceManager.add_record'
    )
    invoice_manager.generate_invoice(
        user_id="U001",
        shipment_id="S001",
        cost=100.0,
        date="2024-01-01"
    )
    mock_add.assert_called_once()


def test_update_invoice(invoice_manager, mocker):
    """Prueba la actualización de una factura."""
    mock_search = mocker.patch(
        'controllers.InvoicesManager.InvoiceManager.search_record'
    )
    mock_search.return_value.empty = False
    invoice_manager.update_invoice(invoice_id="I001", cost=150.0)
    mock_search.assert_called_with({"ID": "I001"})


def test_delete_invoice(invoice_manager, mocker):
    """Prueba la eliminación de una factura."""
    mock_search = mocker.patch(
        'controllers.InvoicesManager.InvoiceManager.search_record'
    )
    mock_search.return_value.empty = False
    invoice_manager.delete_invoice(invoice_id="I001")
    mock_search.assert_called_with({"ID": "I001"})
