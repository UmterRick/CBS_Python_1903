import datetime
import unittest
from unittest.mock import Mock, patch


class SomeClass:
    def get_data(self):
        # API HTTP Request
        # Request to DataBase
        return "real_data"


def process_data(service):
    data = service.get_data()
    return data.upper()


def get_current_time() -> float:
    print("Call get_current_time!!! ")
    return datetime.datetime.now().timestamp()


def check_diff_between_midnight():
    curr_time = datetime.datetime.fromtimestamp(get_current_time())
    date = curr_time.date()
    midnight = datetime.datetime.combine(date, datetime.time(0, 0, 0))
    diff = curr_time - midnight
    # get_current_time()
    print("Diff: ", int(diff.total_seconds()))
    return True if int(diff.total_seconds()) == 7200 else False


class User:
    def __init__(self, name):
        self.name = name


def save_to_db(user: User):
    ...
    ...
    print(f"User {user.name} saved to DB")


def create_user(name, save_func):
    user = User(name)
    save_func(user)
    return user


class TestDataCase(unittest.TestCase):
    def test_process_data(self):
        mock_service = Mock()
        mock_service.get_data.return_value = "mock_data"

        result = process_data(service=mock_service)
        self.assertEqual(result, "MOCK_DATA")

    def test_create_user(self):
        mock_save_user = Mock()
        mock_save_user.return_value = "hello"
        new_user = create_user("test_user", mock_save_user)
        self.assertIsInstance(new_user, User)
        self.assertEqual(new_user.name, "test_user")
        mock_save_user.assert_called_once_with(new_user)

    def test_current_time(self):
        mock_time = datetime.datetime(2024, 6, 18, 2, 0, 0).timestamp()
        with patch("Module_4.lesson_9.test_mock_patch.get_current_time", return_value=mock_time) as mocked_func:
            self.assertTrue(check_diff_between_midnight())
            mocked_func.assert_called_once()

        mock_time = datetime.datetime(2024, 6, 18, 2, 1, 0).timestamp()
        with patch("Module_4.lesson_9.test_mock_patch.get_current_time", return_value=mock_time):
            self.assertFalse(check_diff_between_midnight())



    @patch("Module_4.lesson_9.test_mock_patch.get_current_time", return_value=datetime.datetime(2024, 6, 18, 2, 0, 0).timestamp())
    def test_check_midnight(self, mocked_func):
        result = check_diff_between_midnight()
        self.assertTrue(result)
        mocked_func.assert_called_once()
