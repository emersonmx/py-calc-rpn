import pytest

from domain import Stack


@pytest.fixture
def stack() -> Stack:
    return Stack()
