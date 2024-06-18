import unittest


def some_func(value):
    return value * 100


class FuncTestCase(unittest.TestCase):
    def test_sum(self):
        self.assertLess(2 + 2, 5, "Message from test")

    def test_multiply(self):
        self.assertFalse(2 * 3 != 6)

    def test_some_func(self):
        value = 100
        self.assertEqual(some_func(value), value * 100)

    def test_some_func_wrong(self):
        value = 100
        self.assertNotEqual(some_func(value), value * 110)