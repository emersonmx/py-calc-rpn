import pytest

from calculator import (
    Calculator,
    DefaultStack,
    Enter,
    Number,
    OperatorError,
    add,
)


def make_calculator() -> Calculator:
    stack = DefaultStack()
    return Calculator(stack)


def test_should_execute_operator() -> None:
    calc = make_calculator()

    calc.execute(Enter(Number(2)))
    calc.execute(Enter(Number(2)))
    calc.execute(add)

    assert calc.stack.top() == Number(4)
    assert calc.stack.size() == 1


def test_should_raises_exception_when_have_invalid_operands() -> None:
    calc = make_calculator()

    calc.execute(Enter(Number(2)))

    with pytest.raises(OperatorError):
        calc.execute(add)
    assert calc.stack.size() == 1
