from math_series import __version__
from math_series.series import fibonacci
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