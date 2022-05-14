import pytest

from py_calc_rpn.entities import Stack


@pytest.fixture
def stack() -> Stack:
    return Stack()
