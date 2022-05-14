import pytest

from py_calc_rpn.entities import EmptyStackError, Number, Stack


def test_should_raise_error_on_top_when_empty(stack: Stack) -> None:
    with pytest.raises(EmptyStackError):
        stack.top()


def test_should_return_zero_on_size_when_empty(stack: Stack) -> None:
    assert stack.size() == 0


def test_should_push_a_number(stack: Stack) -> None:
    stack.push(Number(1))

    assert stack.size() == 1
    assert stack.top() == Number(1)


def test_should_push_two_numbers(stack: Stack) -> None:
    stack.push(Number(2))
    stack.push(Number(3))

    assert stack.size() == 2
    assert stack.top() == Number(3)


def test_should_pop_a_number(stack: Stack) -> None:
    stack.push(Number(2))
    stack.push(Number(3))

    assert stack.pop() == Number(3)
    assert stack.size() == 1
    assert stack.top() == Number(2)


def test_should_return_empty_when_pop(stack: Stack) -> None:
    with pytest.raises(EmptyStackError):
        stack.pop()


def test_should_return_empty_when_clear(stack: Stack) -> None:
    stack.push(Number(2))
    stack.push(Number(3))

    assert stack.pop() == Number(3)
    assert stack.size() == 1
    assert stack.top() == Number(2)

    stack.clear()

    assert stack.size() == 0


def test_should_be_iterable(stack: Stack) -> None:
    stack.push(Number(1))
    stack.push(Number(2))
    stack.push(Number(3))

    assert list(stack) == list(map(Number, [1, 2, 3]))
