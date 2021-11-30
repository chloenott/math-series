from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_fib1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fib4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fib5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fib6():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_fibMany():
    n_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    for i in range(len(n_list)):
        actual = fibonacci(i)
        expected = n_list[i]
        assert actual == expected

def test_lucas1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas2():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucasMany():
    n_list = [2, 1, 3, 4, 7, 11, 18, 29]
    for i in range(len(n_list)):
        actual = lucas(i)
        expected = n_list[i]
        assert actual == expected

def test_sum_series_0_default_default():
    actual = sum_series(0)
    expected = fibonacci(0)
    assert actual == expected

def test_sum_series_1_default_default():
    actual = sum_series(1)
    expected = fibonacci(1)
    assert actual == expected

def test_sum_series_5_default_default():
    actual = sum_series(5)
    expected = fibonacci(5)
    assert actual == expected

def test_sum_series_5_0_1():
    actual = sum_series(5, 0, 1)
    expected = fibonacci(5)
    assert actual == expected