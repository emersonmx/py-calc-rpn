import pytest

from calculator import Calculator, Number, Operation, OperatorError, Result


def test_should_execute_operator(calculator: Calculator) -> None:
    calculator.enter(2)
    calculator.enter(2)
    result = calculator.execute(Operation.ADD)

    assert result == Result(
        operation=Operation.ADD,
        operands=[Number(2), Number(2)],
        value=Number(4),
    )


def test_should_raises_exception_when_have_invalid_operands(
    calculator: Calculator,
) -> None:
    calculator.enter(2)

    with pytest.raises(OperatorError):
        calculator.execute(Operation.ADD)
    assert calculator.stack.size() == 1
