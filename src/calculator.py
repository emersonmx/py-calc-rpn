from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Iterator

Operator = Callable[["Stack"], "Result"]
Operation = str


class Number(float):
    pass


@dataclass(frozen=True)
class Result:
    operation: Operation
    operands: list["Number"]
    value: "Number"


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
    def __init__(self, operator: "Operator", stack: "list[Number]") -> None:
        self.operator = operator
        self.stack = stack


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


@dataclass(frozen=True)
class Enter:
    value: Number

    def __call__(self, stack: Stack) -> Result:
        stack.push(self.value)

        return Result(
            operation="enter",
            operands=[self.value],
            value=self.value,
        )


def add(stack: Stack) -> Result:
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    result_value = Number(a + b)
    stack.push(result_value)

    return Result(
        operation="add",
        operands=[a, b],
        value=result_value,
    )


def subtract(stack: Stack) -> Result:
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    result_value = Number(a - b)
    stack.push(result_value)

    return Result(
        operation="subtract",
        operands=[a, b],
        value=result_value,
    )


def multiply(stack: Stack) -> Result:
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    result_value = Number(a * b)
    stack.push(result_value)

    return Result(
        operation="multiply",
        operands=[a, b],
        value=result_value,
    )


def divide(stack: Stack) -> Result:
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    result_value = Number(a / b)
    stack.push(result_value)

    return Result(
        operation="divide",
        operands=[a, b],
        value=result_value,
    )


class Calculator:
    def __init__(self, stack: Stack) -> None:
        self.stack = stack

    def execute(self, operator: Operator) -> Result:
        return operator(self.stack)
