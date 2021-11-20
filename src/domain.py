from dataclasses import dataclass
from typing import Callable, Iterator


class Error(Exception):
    pass


Number = float


class EmptyStackError(Error):
    pass


class Stack:
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
class Result:
    operator: str
    operands: list[float]
    value: float


Operator = Callable[[Stack], Result]


class OperatorError(Error):
    def __init__(self, operator: Operator, stack: list[Number]) -> None:
        self.operator = operator
        self.stack = stack


def add(stack: Stack) -> Result:
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    result_value = Number(a + b)
    stack.push(result_value)

    return Result(
        operator="add",
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
        operator="subtract",
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
        operator="multiply",
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
        operator="divide",
        operands=[a, b],
        value=result_value,
    )
