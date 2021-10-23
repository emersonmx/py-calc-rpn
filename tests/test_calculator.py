import pytest

from calculator import Calculator, Enter, InvalidOperandsError, Number, add


def test_should_add_two_numbers() -> None:
    calc = Calculator()

    calc.execute(Enter(Number(2)))
    calc.execute(Enter(Number(2)))
    calc.execute(add)

    assert calc.stack.top() == Number(4)
    assert calc.stack.size() == 1


def test_should_requires_two_numbers_when_add() -> None:
    calc = Calculator()

    calc.execute(Enter(Number(2)))

    with pytest.raises(InvalidOperandsError):
        calc.execute(add)
    assert calc.stack.size() == 1


def test_should_pop_two_numbers_and_push_the_result_when_execute() -> None:
    calc = Calculator()

    calc.execute(Enter(Number(1)))
    calc.execute(Enter(Number(2)))
    calc.execute(Enter(Number(3)))
    calc.execute(add)

    assert calc.stack.size() == 2
    assert list(calc.stack) == list(map(Number, [1, 5]))
