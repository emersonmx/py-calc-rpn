from typing import Any
from unittest import mock

from py_calc_rpn.entities import Stack
from py_calc_rpn.usecases import (
    ClearMemoryInteractor,
    EnterNumberInteractor,
    ExecuteOperationInteractor,
    ShowMemoryInteractor,
)


def test_should_enter_a_number(stack: Stack) -> None:
    interactor = make_enter_number_interactor(stack)
    mocked_memory_output: Any = interactor._output_memory

    assert stack.size() == 0

    interactor(2)

    assert stack.size() == 1
    assert stack.top() == 2
    mocked_memory_output.assert_called_with([2])


def test_should_execute_operation(stack: Stack) -> None:
    enter_number_interactor = make_enter_number_interactor(stack)
    interactor = make_execute_operation_interactor(stack)
    mocked_result_output: Any = interactor._output_result
    mocked_memory_output: Any = interactor._output_memory

    assert stack.size() == 0

    enter_number_interactor(2)
    enter_number_interactor(2)
    interactor("add")

    assert stack.size() == 1
    assert stack.top() == 4
    mocked_result_output.assert_called_with("add", [2, 2], 4)
    mocked_memory_output.assert_called_with([4])


def test_should_show_memory(stack: Stack) -> None:
    enter_number_interactor = make_enter_number_interactor(stack)
    interactor = make_show_memory_interactor(stack)
    mocked_memory_output: Any = interactor._output_memory

    assert stack.size() == 0

    enter_number_interactor(2)
    enter_number_interactor(2)
    interactor()

    assert stack.size() == 2
    assert stack.top() == 2
    mocked_memory_output.assert_called_with([2, 2])


def test_should_clear_memory(stack: Stack) -> None:
    enter_number_interactor = make_enter_number_interactor(stack)
    interactor = make_clear_memory_interactor(stack)
    mocked_memory_output: Any = interactor._output_memory

    assert stack.size() == 0

    enter_number_interactor(2)
    enter_number_interactor(2)
    interactor()

    assert stack.size() == 0
    mocked_memory_output.assert_called_with([])


def make_enter_number_interactor(stack: Stack) -> EnterNumberInteractor:
    mocked_memory_output = mock.MagicMock()
    return EnterNumberInteractor(
        stack,
        mocked_memory_output,
    )


def make_execute_operation_interactor(
    stack: Stack,
) -> ExecuteOperationInteractor:
    mocked_result_output = mock.MagicMock()
    mocked_memory_output = mock.MagicMock()
    return ExecuteOperationInteractor(
        stack,
        mocked_result_output,
        mocked_memory_output,
    )


def make_show_memory_interactor(stack: Stack) -> ShowMemoryInteractor:
    mocked_memory_output = mock.MagicMock()
    return ShowMemoryInteractor(
        stack,
        mocked_memory_output,
    )


def make_clear_memory_interactor(stack: Stack) -> ClearMemoryInteractor:
    mocked_memory_output = mock.MagicMock()
    return ClearMemoryInteractor(
        stack,
        mocked_memory_output,
    )
