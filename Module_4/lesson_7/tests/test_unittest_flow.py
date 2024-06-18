import datetime
import unittest
from unittest.mock import patch

from Module_4.lesson_7.tests.settings import PROJECT_MODE


def cause_error_func():
    print("Hello from error")
    raise ValueError


def some_func(value):
    cause_error_func()
    return value * 100


class FuncTestCase(unittest.TestCase):

    def tearDown(self):
        print("Clean up after all tests...")

    def setUp(self):
        print("Set init values")
        self.name = "John"
        self.now = datetime.datetime.now()

    @patch('test_unittest_flow.cause_error_func')
    def test_mock_cause_error_func(self, mocked_func):
        print(mocked_func)
        print(mocked_func.called)
        self.assertFalse(mocked_func.called)

    @unittest.skipIf(PROJECT_MODE == "DEV", reason="Just for fun")
    def test_1(self):
        print("Test 1", self.now)
        self.assertLess(self.now, datetime.datetime.now())
        

    def test_2(self):
        print("Test 2", self.name)
        self.assertEqual(self.name, 'John')
        with self.assertRaises(ValueError):
            # cause_error_func()
            raise ValueError
