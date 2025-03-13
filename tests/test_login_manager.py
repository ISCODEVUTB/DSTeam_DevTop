import pytest
import re
from controllers.LoginManager import LoginManager


@pytest.fixture
def login_manager():
    return LoginManager()


def test_sign_in_with_validation(login_manager):
    # Validar formato de email con regex
    email = "test@email.com"
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    assert re.match(email_pattern, email)

    # Registrar usuario
    result = login_manager.sign_in(
        username="testuser",
        password="password123",
        name="Test User",
        email=email,
        address="Test Address",
        permissions="user"
    )
    assert result is True

    # Verificar en DataFrame
    user_data = login_manager.search_record({"username": "testuser"})
    assert not user_data.empty
    assert user_data.iloc[0]["email"] == email


def test_login_validation(login_manager):
    # Validar formato de username
    username = "testuser"
    username_pattern = r'^\w{3,20}$'
    assert re.match(username_pattern, username)
    result = login_manager.login(username, "password123")
    assert isinstance(result, bool)


def test_sign_in_and_login(login_manager):
    # Registrar usuario
    result = login_manager.sign_in(
        username="testuser",
        password="password123",
        name="Test User",
        email="test@email.com",
        address="Test Address",
        permissions="user"
    )
    assert result is True

    # Probar login
    login_success = login_manager.login("testuser", "password123")
    assert login_success is True


def test_login_wrong_credentials(login_manager):
    result = login_manager.login("wronguser", "wrongpass")
    assert result is False
