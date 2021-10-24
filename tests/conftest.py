import pytest

from calculator import Calculator, DefaultStack, Stack


@pytest.fixture
def stack() -> Stack:
    return DefaultStack()


@pytest.fixture
def calculator(stack: Stack) -> Calculator:
    return Calculator(stack)
