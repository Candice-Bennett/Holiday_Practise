#pylint: skip-file
import pytest
from day_one import elevators, basement_position

def test_elevators():
    assert elevators("(())") == 0
    assert elevators("()()") == 0
    assert elevators("(((") == 3
    assert elevators("(()(()(") == 3
    assert elevators("))(((((") == 3
    assert elevators("))(((((") == 3
    assert elevators("())") == -1
    assert elevators("))(") == -1
    assert elevators(")))") == -3
    assert elevators(")())())") == -3

def test_basement_position_positive():
    assert basement_position(")") == 1
    assert basement_position("()())") == 5

def test_basement_position_negative():
    with pytest.raises(ValueError):
        basement_position("((((")
    with pytest.raises(ValueError):
        basement_position("()")