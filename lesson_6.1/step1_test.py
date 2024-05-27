import pytest
from step1 import check_bg

@pytest.mark.parametrize('result', [(True)])
def test_bg_zip(result):
    res = check_bg()[0]
    assert res == result

@pytest.mark.parametrize('result', [([True, True, True, True, True, True, True, True, True])])
def test_bg_other(result):
    res = check_bg()[1:]
    assert res == result
    