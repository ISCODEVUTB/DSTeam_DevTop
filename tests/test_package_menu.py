import pytest
from views.package_menu import PackageMenu


@pytest.fixture
def package_menu():
    return PackageMenu()


def test_package_menu_init(package_menu):
    assert package_menu.name == "Menú de Paquetes"
    assert "1" in package_menu.options  # ver paquetes
    assert "2" in package_menu.options  # agregar paquete
    assert "3" in package_menu.options  # modificar paquete
    assert "4" in package_menu.options  # eliminar paquete
    assert "e" in package_menu.options  # volver


def test_add_package_execution(package_menu, mocker):
    inputs = ['Test Package', '10x10x10', 'Normal', '1.5']
    mocker.patch('builtins.input', side_effect=inputs)
    mock_add = mocker.patch(
        'controllers.PackagesManager.PackageManager.add_package')
    package_menu.add_package()
    mock_add.assert_called_once_with(*inputs)


def test_show_packages(package_menu, mocker):
    mock_show = mocker.patch(
        'controllers.PackagesManager.PackageManager.show')
    package_menu.show_packages()
    mock_show.assert_called_once()
