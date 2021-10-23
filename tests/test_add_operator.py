import pytest

from calculator import DefaultStack, Number, OperatorError, add


def test_should_requires_two_numbers() -> None:
    stack = DefaultStack()

    with pytest.raises(OperatorError):
        add(stack)

    assert stack.size() == 0

    stack.push(Number(1))

    with pytest.raises(OperatorError):
        add(stack)

    assert stack.size() == 1
    assert stack.top() == Number(1)


def test_should_add_two_numbers() -> None:
    stack = DefaultStack()

    stack.push(Number(1))
    stack.push(Number(1))

    add(stack)

    assert stack.size() == 1
    assert stack.top() == Number(2)


def test_should_pop_two_numbers_and_push_the_result() -> None:
    stack = DefaultStack()

    stack.push(Number(1))
    stack.push(Number(2))
    stack.push(Number(3))

    add(stack)

    assert stack.size() == 2
    assert list(stack) == list(map(Number, [1, 5]))
