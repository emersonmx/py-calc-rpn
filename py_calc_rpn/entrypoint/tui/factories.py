from py_calc_rpn.adapters import EnterNumberController
from py_calc_rpn.entrypoint.tui.app import App


def make_app() -> App:
    return App()


def make_enter_number_command():
    enter_number_controller = make_enter_number_controller()
    return EnterNumberCommand(enter_number_controller)

def make_enter_number_controller():
    return EnterNumberController(

    )
