import itertools

import pytest

from calculator import DefaultStack, Number, OperatorError, subtract

DEFAULT_NUMBERS = itertools.product([-5, -1, 0, -1, 5], repeat=2)


def test_should_requires_two_numbers() -> None:
    stack = DefaultStack()

    with pytest.raises(OperatorError):
        subtract(stack)

    assert stack.size() == 0

    stack.push(Number(1))

    with pytest.raises(OperatorError):
        subtract(stack)

    assert stack.size() == 1
    assert stack.top() == Number(1)


@pytest.mark.parametrize(
    "a, b, result",
    [
        *[(a, b, a - b) for a, b in DEFAULT_NUMBERS],
    ],
)
def test_should_subtract_two_numbers(a: int, b: int, result: int) -> None:
    stack = DefaultStack()

    stack.push(Number(a))
    stack.push(Number(b))

    subtract(stack)

    assert stack.size() == 1
    assert stack.top() == Number(result)


def test_should_pop_two_numbers_and_push_the_result() -> None:
    stack = DefaultStack()

    stack.push(Number(1))
    stack.push(Number(2))
    stack.push(Number(3))

    subtract(stack)

    assert stack.size() == 2
    assert list(stack) == list(map(Number, [1, -1]))
