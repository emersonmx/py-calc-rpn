import itertools

import pytest

from calculator import Number, OperatorError, Stack, divide

DEFAULT_NUMBERS = itertools.product([-5, -1, 1, 5], repeat=2)


def test_should_requires_two_numbers(stack: Stack) -> None:
    with pytest.raises(OperatorError):
        divide(stack)

    assert stack.size() == 0

    stack.push(Number(1))

    with pytest.raises(OperatorError):
        divide(stack)

    assert stack.size() == 1
    assert stack.top() == Number(1)


@pytest.mark.parametrize(
    "a, b, result",
    [
        *[(a, b, a / b) for a, b in DEFAULT_NUMBERS],
        (0, 1, 0),
    ],
)
def test_should_divide_two_numbers(
    a: int,
    b: int,
    result: int,
    stack: Stack,
) -> None:
    stack.push(Number(a))
    stack.push(Number(b))

    divide(stack)

    assert stack.size() == 1
    assert stack.top() == Number(result)


def test_should_raise_error_when_division_by_zero(stack: Stack) -> None:
    stack.push(Number(1))
    stack.push(Number(0))

    with pytest.raises(ZeroDivisionError):
        divide(stack)


def test_should_pop_two_numbers_and_push_the_result(stack: Stack) -> None:
    stack.push(Number(1))
    stack.push(Number(2))
    stack.push(Number(3))

    divide(stack)

    assert stack.size() == 2
    assert list(stack) == list(map(Number, [1, 2 / 3]))
