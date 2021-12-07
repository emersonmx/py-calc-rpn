from dataclasses import dataclass, field

from usecases import (
    ClearMemory,
    EnterNumber,
    ExecuteOperation,
    MemoryOutput,
    ResultOuput,
    ShowMemory,
)


class EnterNumberController:
    def __init__(self, enter_number: EnterNumber) -> None:
        self._enter_number = enter_number

    def __call__(self, number: float) -> None:
        self._enter_number(number)


class ExecuteOperationController:
    def __init__(self, execute_operation: ExecuteOperation) -> None:
        self._execute_operation = execute_operation

    def __call__(self, operation: str) -> None:
        self._execute_operation(operation)


class ShowMemoryController:
    def __init__(self, show_memory: ShowMemory) -> None:
        self._show_memory = show_memory

    def __call__(self) -> None:
        self._show_memory()


class ClearMemoryController:
    def __init__(self, clear_memory: ClearMemory) -> None:
        self._clear_memory = clear_memory

    def __call__(self) -> None:
        self._clear_memory()


@dataclass
class Result:
    operation: str
    operands: list[float]
    value: float


Memory = list[float]


@dataclass
class ResultOuputPresenter(ResultOuput):
    result: Result | None = None

    def __call__(
        self,
        operation: str,
        operands: list[float],
        result: float,
    ) -> None:
        self.result = Result(
            operation=operation,
            operands=operands,
            value=result,
        )


@dataclass
class MemoryOutputPresenter(MemoryOutput):
    memory: Memory = field(default_factory=list)

    def __call__(self, memory: list[float]) -> None:
        self.memory = memory
