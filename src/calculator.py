from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Iterator

Operator = Callable[["Stack"], "Result"]


class Number(float):
    pass


class Stack(ABC):
    @abstractmethod
    def top(self) -> Number:
        ...

    @abstractmethod
    def size(self) -> int:
        ...

    @abstractmethod
    def push(self, number: Number) -> None:
        ...

    @abstractmethod
    def pop(self) -> Number:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...

    @abstractmethod
    def __iter__(self) -> Iterator[Number]:
        ...


class Error(Exception):
    pass


class EmptyStackError(Error):
    pass


class OperatorError(Error):
    def __init__(self, operator: "Operator", stack: list[Number]) -> None:
        self.operator = operator
        self.stack = stack


class InvalidCommandError(Error):
    def __init__(self, operation: "Operation", stack: list[Number]) -> None:
        self.operation = operation


class DefaultStack(Stack):
    def __init__(self) -> None:
        self.stack: list[Number] = []

    def top(self) -> Number:
        if self.size() == 0:
            raise EmptyStackError()
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)

    def push(self, number: Number) -> None:
        self.stack.append(number)

    def pop(self) -> Number:
        if self.size() == 0:
            raise EmptyStackError()
        return self.stack.pop()

    def clear(self) -> None:
        self.stack = []

    def __iter__(self) -> Iterator[Number]:
        return iter(self.stack)


class Operation(str, Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

    def __str__(self) -> str:
        return self.value


def add(stack: Stack) -> "Result":
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    result_value = Number(a + b)
    stack.push(result_value)

    return Result(
        operation=Operation.ADD,
        operands=[a, b],
        value=result_value,
    )


def subtract(stack: Stack) -> "Result":
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    result_value = Number(a - b)
    stack.push(result_value)

    return Result(
        operation=Operation.SUBTRACT,
        operands=[a, b],
        value=result_value,
    )


def multiply(stack: Stack) -> "Result":
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    result_value = Number(a * b)
    stack.push(result_value)

    return Result(
        operation=Operation.MULTIPLY,
        operands=[a, b],
        value=result_value,
    )


def divide(stack: Stack) -> "Result":
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    result_value = Number(a / b)
    stack.push(result_value)

    return Result(
        operation=Operation.DIVIDE,
        operands=[a, b],
        value=result_value,
    )


@dataclass(frozen=True)
class Result:
    operation: Operation
    operands: list[float]
    value: float


class Calculator:
    def __init__(self, stack: Stack) -> None:
        self.stack = stack

    def enter(self, number: float) -> None:
        self.stack.push(Number(number))

    def execute(self, operation: Operation) -> Result:
        try:
            operator: Operator = globals()[operation]
            return operator(self.stack)
        except KeyError:
            raise InvalidCommandError(operation, list(self.stack))
