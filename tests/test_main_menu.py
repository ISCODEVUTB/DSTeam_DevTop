
import pytest
from unittest import mock
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


def test_menu_package_navigation(main_menu):
    with mock.patch('views.package_menu.PackageMenu.run') as mock_run:
        main_menu.menu_package()
        assert mock_run.called_once()


def test_menu_shipment_navigation(main_menu):
    with mock.patch('views.shipment_menu.ShipmentMenu.run') as mock_run:
        main_menu.menu_shipment()
        assert mock_run.called_once()


def test_menu_invoices_navigation(main_menu):
    with mock.patch('views.invoices_menu.InvoicesMenu.run') as mock_run:
        main_menu.menu_invoices()
        assert mock_run.called_once()


def test_leave(main_menu):
    with mock.patch('builtins.print') as mock_print:
        main_menu.leave()
        mock_print.assert_called_with("Saliendo del sistema...")
