import pytest
from step3 import shop


@pytest.mark.parametrize('result', [('58.29')])
def test_shop(result):
    res = shop()
    assert res == result
