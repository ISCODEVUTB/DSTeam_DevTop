import pytest
from unittest.mock import patch
from controllers.UsersManager import UserManager


@pytest.fixture
def user_manager():
    return UserManager()


def test_update_user(user_manager):
    with patch('controllers.UsersManager.UserManager.search_record') as mock_search:
        mock_search.return_value.empty = False
        user_manager.update_user("U001", username="newuser")
        mock_search.assert_called_with({"ID": "U001"})


def test_delete_user(user_manager):
    with patch('controllers.UsersManager.UserManager.search_record') as mock_search:
        mock_search.return_value.empty = False
        user_manager.delete_user("U001")
        mock_search.assert_called_with({"ID": "U001"})


def test_search_user(user_manager):
    with patch('controllers.UsersManager.UserManager.search_record') as mock_search:
        mock_search.return_value.empty = False
        user_manager.search_user({"Username": "test"})
        mock_search.assert_called_with({"Username": "test"})
