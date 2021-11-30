from math_series import __version__
from math_series.series import fibonacci
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_fib1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected