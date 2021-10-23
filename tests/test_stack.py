import pytest

from calculator import DefaultStack, EmptyStackError, Number


def test_should_raise_error_on_top_when_empty() -> None:
    stack = DefaultStack()

    with pytest.raises(EmptyStackError):
        stack.top()


def test_should_return_zero_on_size_when_empty() -> None:
    stack = DefaultStack()

    assert stack.size() == 0


def test_should_push_a_number() -> None:
    stack = DefaultStack()

    stack.push(Number(1))

    assert stack.size() == 1
    assert stack.top() == Number(1)


def test_should_push_two_numbers() -> None:
    stack = DefaultStack()

    stack.push(Number(2))
    stack.push(Number(3))

    assert stack.size() == 2
    assert stack.top() == Number(3)


def test_should_pop_a_number() -> None:
    stack = DefaultStack()

    stack.push(Number(2))
    stack.push(Number(3))

    assert stack.pop() == Number(3)
    assert stack.size() == 1
    assert stack.top() == Number(2)


def test_should_return_empty_when_pop() -> None:
    stack = DefaultStack()

    with pytest.raises(EmptyStackError):
        stack.pop()


def test_should_return_empty_when_clear() -> None:
    stack = DefaultStack()

    stack.push(Number(2))
    stack.push(Number(3))

    assert stack.pop() == Number(3)
    assert stack.size() == 1
    assert stack.top() == Number(2)

    stack.clear()

    assert stack.size() == 0


def test_should_be_iterable() -> None:
    stack = DefaultStack()

    stack.push(Number(1))
    stack.push(Number(2))
    stack.push(Number(3))

    assert list(stack) == list(map(Number, [1, 2, 3]))
