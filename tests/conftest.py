import pytest

from adapters import DefaultStack
from domain import Stack
from service import Calculator


@pytest.fixture
def stack() -> Stack:
    return DefaultStack()


@pytest.fixture
def calculator(stack: Stack) -> Calculator:
    return Calculator(stack)
