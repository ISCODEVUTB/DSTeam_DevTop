import pytest
from unittest.mock import patch
import main


@patch('src.views.LoginMenu.run')
def test_main(mock_run):
    """
    Verifica que la función main ejecute el menú de inicio de sesión correctamente,
    comprobando que LoginMenu.run se invoque exactamente una vez.
    """
    main.main()
    mock_run.assert_called_once()


if __name__ == "__main__":
    pytest.main()
