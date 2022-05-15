from typing import Protocol


class Command(Protocol):
    def __call__(self, user_input: str) -> None:
        ...
