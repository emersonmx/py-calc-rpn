import pytest

from calculator import Calculator, Enter, Number, OperatorError, add


def test_should_execute_operator() -> None:
    calc = Calculator()

    calc.execute(Enter(Number(2)))
    calc.execute(Enter(Number(2)))
    calc.execute(add)

    assert calc.stack.top() == Number(4)
    assert calc.stack.size() == 1


def test_should_raises_exception_when_have_invalid_operands() -> None:
    calc = Calculator()

    calc.execute(Enter(Number(2)))

    with pytest.raises(OperatorError):
        calc.execute(add)
    assert calc.stack.size() == 1
