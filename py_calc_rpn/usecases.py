from typing import Protocol

from . import entities


class EnterNumber(Protocol):
    def __call__(self, number: float) -> None:  # pragma: no cover
        ...


class ExecuteOperation(Protocol):
    def __call__(self, operation: str) -> None:  # pragma: no cover
        ...


class ShowMemory(Protocol):
    def __call__(self) -> None:  # pragma: no cover
        ...


class ClearMemory(Protocol):
    def __call__(self) -> None:  # pragma: no cover
        ...


class ResultOuput(Protocol):
    def __call__(
        self,
        operation: str,
        operands: list[float],
        result: float,
    ) -> None:  # pragma: no cover
        ...


class MemoryOutput(Protocol):
    def __call__(self, memory: list[float]) -> None:  # pragma: no cover
        ...


class EnterNumberInteractor:
    def __init__(
        self,
        stack: entities.Stack,
        memory_output: MemoryOutput,
    ) -> None:
        self._stack = stack
        self._output_memory = memory_output

    def __call__(self, number: float) -> None:
        self._stack.push(entities.Number(number))
        self._output_memory(list(self._stack))


class ExecuteOperationInteractor:
    def __init__(
        self,
        stack: entities.Stack,
        result_output: ResultOuput,
        memory_output: MemoryOutput,
    ) -> None:
        self._stack = stack
        self._output_result = result_output
        self._output_memory = memory_output

    def __call__(self, operation: str) -> None:
        operation_handler: entities.Operation = getattr(entities, operation)
        result = operation_handler(self._stack)
        self._output_result(result.operation, result.operands, result.value)
        self._output_memory(list(self._stack))


class ShowMemoryInteractor:
    def __init__(
        self,
        stack: entities.Stack,
        memory_output: MemoryOutput,
    ) -> None:
        self._stack = stack
        self._output_memory = memory_output

    def __call__(self) -> None:
        self._output_memory(list(self._stack))


class ClearMemoryInteractor:
    def __init__(
        self,
        stack: entities.Stack,
        memory_output: MemoryOutput,
    ) -> None:
        self._stack = stack
        self._output_memory = memory_output

    def __call__(self) -> None:
        self._stack.clear()
        self._output_memory(list(self._stack))
