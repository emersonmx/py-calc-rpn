import pytest

from calculator import Calculator, Enter, Number, OperatorError, Result, add


def test_should_execute_operator(calculator: Calculator) -> None:
    na = Number(2)
    nb = Number(2)
    calculator.execute(Enter(na))
    calculator.execute(Enter(nb))
    result = calculator.execute(add)

    assert result == Result(
        operation="add",
        operands=[na, nb],
        value=Number(4),
    )


def test_should_raises_exception_when_have_invalid_operands(
    calculator: Calculator,
) -> None:
    calculator.execute(Enter(Number(2)))

    with pytest.raises(OperatorError):
        calculator.execute(add)
    assert calculator.stack.size() == 1
