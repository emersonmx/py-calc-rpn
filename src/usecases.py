from typing import Protocol

import domain


class EnterNumber(Protocol):
    def __call__(self, number: float) -> None:
        ...


class ExecuteOperator(Protocol):
    def __call__(self, operator: str) -> None:
        ...


class ShowMemory(Protocol):
    def __call__(self) -> None:
        ...


class ClearMemory(Protocol):
    def __call__(self) -> None:
        ...


class ResultOuput(Protocol):
    def __call__(
        self,
        operator: str,
        operands: list[float],
        result: float,
    ) -> None:
        ...


class MemoryOutput(Protocol):
    def __call__(self, memory: list[float]) -> None:
        ...


class EnterNumberInteractor:
    def __init__(
        self,
        stack: domain.Stack,
        memory_output: MemoryOutput,
    ) -> None:
        self._stack = stack
        self._output_memory = memory_output

    def __call__(self, number: float) -> None:
        self._stack.push(domain.Number(number))
        self._output_memory(list(self._stack))


class ExecuteOperatorInteractor:
    def __init__(
        self,
        stack: domain.Stack,
        result_output: ResultOuput,
        memory_output: MemoryOutput,
    ) -> None:
        self._stack = stack
        self._output_result = result_output
        self._output_memory = memory_output

    def __call__(self, operator: str) -> None:
        operator_handler: domain.Operator = getattr(domain, operator)
        result = operator_handler(self._stack)
        self._output_result(result.operator, result.operands, result.value)
        self._output_memory(list(self._stack))


class ShowMemoryInteractor:
    def __init__(
        self,
        stack: domain.Stack,
        memory_output: MemoryOutput,
    ) -> None:
        self._stack = stack
        self._output_memory = memory_output

    def __call__(self) -> None:
        self._output_memory(list(self._stack))


class ClearMemoryInteractor:
    def __init__(
        self,
        stack: domain.Stack,
        memory_output: MemoryOutput,
    ) -> None:
        self._stack = stack
        self._output_memory = memory_output

    def __call__(self) -> None:
        self._stack.clear()
        self._output_memory(list(self._stack))
