import pytest

from calculator import Calculator, Enter, Number, OperatorError, add


def test_should_execute_operator(calculator: Calculator) -> None:
    calculator.execute(Enter(Number(2)))
    calculator.execute(Enter(Number(2)))
    calculator.execute(add)

    assert calculator.stack.top() == Number(4)
    assert calculator.stack.size() == 1


def test_should_raises_exception_when_have_invalid_operands(
    calculator: Calculator,
) -> None:
    calculator.execute(Enter(Number(2)))

    with pytest.raises(OperatorError):
        calculator.execute(add)
    assert calculator.stack.size() == 1
