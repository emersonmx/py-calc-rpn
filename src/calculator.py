from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Iterator

Operator = Callable[["Stack"], None]


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

    def __call__(self, stack: Stack) -> None:
        stack.push(self.value)


def add(stack: Stack) -> None:
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    stack.push(Number(a + b))


def subtract(stack: Stack) -> None:
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    stack.push(Number(a - b))


def multiply(stack: Stack) -> None:
    if stack.size() < 2:
        raise OperatorError(add, list(stack))

    b = stack.pop()
    a = stack.pop()

    stack.push(Number(a * b))


class Calculator:
    def __init__(self) -> None:
        self.stack = DefaultStack()

    def execute(self, operator: Operator) -> None:
        operator(self.stack)
