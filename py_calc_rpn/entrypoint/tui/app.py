from py_calc_rpn.entrypoint.tui.commands import Command
from py_calc_rpn.entrypoint.tui.exceptions import InvalidCommandError


class App:
    def __init__(self) -> None:
        self.running = True
        self.user_input = ""

    def run(self) -> None:
        self._show_init_help()
        while self.running:
            try:
                self._process()
            except Exception as e:
                print(e)

    def _show_init_help(self) -> None:
        print("Press Ctrl-c to quit.")

    def _process(self) -> None:
        self.user_input = self._get_user_input()
        command = self._get_command()
        command(self.user_input)

    def _get_user_input(self) -> str:
        return input("> ")

    def _get_command(self) -> Command:
        # A number
        # + or add
        # - or subtract
        # * or multiply
        # / or divide
        # stack
        # clear
        # quit
        # help
        raise InvalidCommandError(self.user_input)
