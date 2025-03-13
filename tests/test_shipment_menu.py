import pytest
from views.shipment_menu import ShipmentMenu


@pytest.fixture
def shipment_menu():
    return ShipmentMenu()


def test_shipment_menu_init(shipment_menu):
    assert shipment_menu.name == "Menú de Envíos"
    assert "1" in shipment_menu.options  # ver envíos
    assert "2" in shipment_menu.options  # agregar envío
    assert "3" in shipment_menu.options  # modificar envío
    assert "4" in shipment_menu.options  # eliminar envío
    assert "e" in shipment_menu.options  # volver


def test_add_shipment_execution(shipment_menu, mocker):
    inputs = ['U001', 'P001', '100.0', '2024-01-01', 'En proceso']
    mocker.patch('builtins.input', side_effect=inputs)
    mock_create = mocker.patch(
        'controllers.ShipmentManager.ShipmentManager.create_shipment')
    shipment_menu.add_shipment()
    mock_create.assert_called_once_with(*inputs)


def test_show_shipments(shipment_menu, mocker):
    mock_show = mocker.patch('controllers.ShipmentManager.ShipmentManager.show')
    shipment_menu.show_shipments()
    mock_show.assert_called_once()
