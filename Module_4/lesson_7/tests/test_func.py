import pytest

from Module_4.lesson_7.tests.some_functionality import concat, sum_elem


def test_concat():
    test_data = ('hello', 'world')
    result = concat(*test_data)
    expect = 'hello world'
    assert result == expect


def test_sum_elem():
    result = sum_elem(2, 2, 2)
    expect = 6
    assert result == expect
