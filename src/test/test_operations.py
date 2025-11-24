from src.math_operation import add,subtraction


def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    


def test_subract():
    assert subtraction(5,3)==2
    assert subtraction(-1,1)==-2
