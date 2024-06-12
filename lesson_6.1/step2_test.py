import pytest
from step2 import calc

@pytest.mark.parametrize('num1, num2, result', [(7, 8, 15)])
def test_calc(num1, num2, result):
    res = calc(num1, num2)
    assert res == result
