import pytest
from views.login_menu import LoginMenu


@pytest.fixture
def login_menu():
    return LoginMenu()


def test_login_menu_init(login_menu):
    assert login_menu.name == "Menú de Logueo"
    assert "1" in login_menu.options  # opción de login
    assert "2" in login_menu.options  # opción de registro
    assert "q" in login_menu.options  # opción de salir


def test_login_execution(login_menu, mocker):
    mocker.patch('builtins.input', side_effect=['testuser', 'password'])
    mock_login = mocker.patch(
        'controllers.LoginManager.LoginManager.login')
    login_menu.login()
    mock_login.assert_called_once_with('testuser', 'password')


def test_register_execution(login_menu, mocker):
    inputs = ['testuser', 'password',
              'Test User', 'test@email.com',
              'Test Address', 'user']
    mocker.patch('builtins.input', side_effect=inputs)
    mock_signin = mocker.patch(
        'controllers.LoginManager.LoginManager.sign_in')
    login_menu.register()
    mock_signin.assert_called_once_with(*inputs)
