import pytest
from operations import add, subtract, multiply, divide 

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_add_FAIL():
    assert add(2,3) == 6  # This test is expected to fail

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0

def test_subtract_FAIL():
    assert subtract(5, 3) == 3  # This test is expected to fail

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1

def test_multiply_FAIL():
    assert multiply(2, 3) == 5  # This test is expected to fail

def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(1, 0)

def test_divide_FAIL():
    assert divide(6, 3) == 3  # This test is expected to fail
    with pytest.raises(ValueError):
        divide(1, 1)  # This test is expected to fail
