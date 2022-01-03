import pytest

# content of test_assert1.py
def f():
    return 4


def test_function():
    assert f() == 4
