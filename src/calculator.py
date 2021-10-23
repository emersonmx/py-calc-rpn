from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Iterator


class Number(float):
    pass


class Stack(ABC):
    @abstractmethod
    def top(self) -> Number | None:
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


class DefaultStack(Stack):
    def __init__(self) -> None:
        self.stack: list[Number] = []

    def top(self) -> Number | None:
        return self.stack[-1] if self.size() > 0 else None

    def size(self) -> int:
        return len(self.stack)

    def push(self, number: Number) -> None:
        self.stack.append(number)

    def pop(self) -> Number:
        return self.stack.pop()

    def clear(self) -> None:
        self.stack = []

    def __iter__(self) -> Iterator[Number]:
        return iter(self.stack)


Operator = Callable[[Stack], None]


class InvalidOperandsError(Exception):
    def __init__(self, operator: Operator, operands: list[Number]) -> None:
        self.operator = operator
        self.operands = operands


@dataclass(frozen=True)
class Enter:
    value: Number

    def __call__(self, stack: Stack) -> None:
        stack.push(self.value)


def add(stack: Stack) -> None:
    if stack.size() < 2:
        raise InvalidOperandsError(add, list(stack))

    a = stack.pop()
    b = stack.pop()
    stack.push(Number(a + b))


class Calculator:
    def __init__(self) -> None:
        self.stack = DefaultStack()

    def execute(self, operator: Operator) -> None:
        operator(self.stack)
