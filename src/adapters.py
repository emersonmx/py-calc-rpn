from typing import Iterator

from domain import Number
from errors import EmptyStackError


class DefaultStack:
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
