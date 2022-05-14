class Error(Exception):
    pass


class InvalidCommandError(Error):
    def __init__(self, command: str) -> None:
        self.command = command
