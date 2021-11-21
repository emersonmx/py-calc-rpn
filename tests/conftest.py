import pytest

from entities import Stack


@pytest.fixture
def stack() -> Stack:
    return Stack()
