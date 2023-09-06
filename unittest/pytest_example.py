# import pytest
# def sum(a,b):
#     if a is None or b is None:
#         raise ValueError("Please provide both the input")
#     return a + b

# def test_sum_equal():
#     assert sum(4,5) == 9
# def test_sum_none():
#     with pytest.raises(ValueError):
#         sum(None, 5)

#----------------
import pytest
class Fruit:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        # import pdb;pdb.set_trace()
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("banana")

@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]

def test_my_fruit_in_basket(my_fruit, fruit_basket):
    import pdb;pdb.set_trace()
    assert my_fruit in fruit_basket