import pytest
from Calculator import Calculator

@pytest.mark.test
def test_add_with_2number():
    calc = Calculator()
    total = calc.add(5,5)
    assert total, 55