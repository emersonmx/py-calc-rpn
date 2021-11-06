from typing import Iterator, Protocol


class Number(float):
    pass


class Stack(Protocol):
    def top(self) -> Number:
        ...

    def size(self) -> int:
        ...

    def push(self, number: Number) -> None:
        ...

    def pop(self) -> Number:
        ...

    def clear(self) -> None:
        ...

    def __iter__(self) -> Iterator[Number]:
        ...
