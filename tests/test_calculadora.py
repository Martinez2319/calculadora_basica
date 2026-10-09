
import pytest
from calculadora import add, sub, mul, div

def test_suma():
    assert add(2, 3) == 5

def test_resta():
    assert sub(5, 2) == 3

def test_multiplicacion():
    assert mul(4, 3) == 12

def test_division():
    assert div(10, 2) == 5

def test_division_cero():
    with pytest.raises(ValueError):
        div(10, 0)
