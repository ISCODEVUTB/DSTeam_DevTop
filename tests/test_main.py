import pytest
from unittest.mock import patch
import main


@patch('src.gui.login_menu.LoginMenu.run')
def test_main(mock_run):
    """
    Prueba la función principal para asegurarse
    de que el menú de inicio de sesión se ejecute.
    """
    main()
    mock_run.assert_called_once()


if __name__ == "__main__":
    pytest.main()
