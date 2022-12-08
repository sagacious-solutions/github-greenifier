from RPA.Windows import Windows

win = Windows()


def open_terminal():
    """Opens a windows terminal"""
    win.windows_run("cmd")

def get_terminal_focus():
    """Gains control of the windows terminal and returns the control element

    Returns:
        WindowsLocator: The Windows terminal control element
    """
    return win.control_window('subname:"cmd.exe"')


def enter_command_in_terminal(element, command: str):
    """Enters a command into the terminal and runs it

    Args:
        element (WindowsLocator): Windows terminal element
        command (str): terminal command to run
    """
    win.send_keys(element, command, send_enter=True)