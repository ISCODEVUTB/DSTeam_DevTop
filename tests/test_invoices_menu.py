import pytest
from views.invoices_menu import InvoicesMenu


@pytest.fixture
def invoices_menu():
    return InvoicesMenu()


def test_invoices_menu_init(invoices_menu):
    assert invoices_menu.name == "Menú de Facturas"
    assert "1" in invoices_menu.options  # ver facturas
    assert "2" in invoices_menu.options  # generar factura
    assert "3" in invoices_menu.options  # eliminar factura
    assert "e" in invoices_menu.options  # volver


def test_generate_invoice_execution(invoices_menu, mocker):
    inputs = ['I001', 'Cliente Test', '100.0', '2024-01-01']
    mocker.patch('builtins.input', side_effect=inputs)
    mock_create = mocker.patch(
        'controllers.PaymentsManager.PaymentsManager.create_invoice')
    invoices_menu.generate_invoice()
    mock_create.assert_called_once()


def test_show_invoices(invoices_menu, mocker):
    mock_show = mocker.patch(
        'controllers.PaymentsManager.PaymentsManager.show')
    invoices_menu.show_invoices()
    mock_show.assert_called_once()
