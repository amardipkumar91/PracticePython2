import pytest
def sum(a,b):
    if a is None or b is None:
        raise ValueError("Please provide both the input")
    return a + b

def test_sum_equal():
    assert sum(4,5) == 9
def test_sum_none():
    with pytest.raises(ValueError):
        sum(None, 5)

