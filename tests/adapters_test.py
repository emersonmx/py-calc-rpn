from unittest import mock

from hypothesis import given

from py_calc_rpn.adapters import (
    ClearMemoryController,
    EnterNumberController,
    ExecuteOperationController,
    MemoryOutputPresenter,
    ResultOuputPresenter,
    ShowMemoryController,
)


@given(...)
def test_should_call_enter_number_usecase(value: float) -> None:
    mocked_usecase = mock.Mock()
    controller = EnterNumberController(mocked_usecase)

    controller(value)

    mocked_usecase.assert_called_with(value)


def test_should_call_execute_operation_usecase() -> None:
    mocked_usecase = mock.Mock()
    controller = ExecuteOperationController(mocked_usecase)

    controller("add")

    mocked_usecase.assert_called_with("add")


def test_should_call_show_memory_usecase() -> None:
    mocked_usecase = mock.Mock()
    controller = ShowMemoryController(mocked_usecase)

    controller()

    mocked_usecase.assert_called_once()


def test_should_call_clear_memory_usecase() -> None:
    mocked_usecase = mock.Mock()
    controller = ClearMemoryController(mocked_usecase)

    controller()

    mocked_usecase.assert_called_once()


def test_should_fill_result_on_call() -> None:
    presenter = ResultOuputPresenter()

    assert presenter.result is None

    presenter(operation="add", operands=[1.0, 1.0], result=2.0)

    assert presenter.result is not None
    assert presenter.result.operation == "add"
    assert presenter.result.operands == [1.0, 1.0]
    assert presenter.result.value == 2.0


def test_should_fill_memory_on_call() -> None:
    presenter = MemoryOutputPresenter()

    assert presenter.memory == []

    presenter(memory=[1.0, 2.0, 3.0])

    assert presenter.memory == [1.0, 2.0, 3.0]
