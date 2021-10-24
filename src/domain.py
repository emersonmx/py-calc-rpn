from abc import ABC, abstractmethod
from typing import Iterator


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
