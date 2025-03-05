from src.math_operations import add, mul


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_mul():
    assert mul(1, 3) == 3
    assert mul(2, 3) == 6
    assert mul(3, -2) == -6
 