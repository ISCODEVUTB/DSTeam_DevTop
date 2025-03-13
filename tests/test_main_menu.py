import pytest
from views.main_menu import MainMenu


@pytest.fixture
def main_menu():
    return MainMenu()


def test_main_menu_init(main_menu):
    assert main_menu.name == "Menú Principal"
    assert "1" in main_menu.options  # menú de paquetes
    assert "2" in main_menu.options  # menú de envíos
    assert "3" in main_menu.options  # menú de facturas
    assert "q" in main_menu.options  # opción de salir


def test_menu_package_navigation(main_menu, mocker):
    mock_package_menu = mocker.patch('views.package_menu.PackageMenu.run')
    main_menu.menu_package()
    mock_package_menu.assert_called_once()


def test_menu_shipment_navigation(main_menu, mocker):
    mock_shipment_menu = mocker.patch('views.shipment_menu.ShipmentMenu.run')
    main_menu.menu_shipment()
    mock_shipment_menu.assert_called_once()


def test_menu_invoices_navigation(main_menu, mocker):
    mock_invoices_menu = mocker.patch('views.invoices_menu.InvoicesMenu.run')
    main_menu.menu_invoices()
    mock_invoices_menu.assert_called_once()
