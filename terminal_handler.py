from typing import List
from RPA.Windows import Windows
from RPA.Windows.keywords.locators import WindowsElement

win = Windows()


def open_terminal():
    """Opens a windows terminal"""
    win.windows_run("cmd")


def get_terminal_focus():
    """Gains control of the windows terminal and returns the control element

    Returns:
        WindowsElement: The Windows terminal control element
    """
    return win.control_window('subname:"cmd.exe"')


def close_terminal_pop_up():
    """Closes any terminals opened as admin that aren't currently executing any actions"""
    LOCATOR_NON_EXECUTING_TERMINAL = (
        'name:"Administrator: C:\Windows\system32\cmd.exe"'
    )
    win.close_window(LOCATOR_NON_EXECUTING_TERMINAL)


def enter_command_in_terminal(element: WindowsElement, command: str):
    """Enters a command into the terminal and runs it

    Args:
        element (WindowsElement): Windows terminal element
        command (str): terminal command to run
    """
    win.send_keys(element, command, send_enter=True)


def get_terminal_text_as_list(cmd_box_element: WindowsElement) -> List[str]:
    """Gets the current text from the terminal

    Args:
        element (WindowsElement): Windows terminal element
    Returns:
        List[str]: List of the current strings in the terminal
    """
    text_elm = win.get_element('name:"Text Area"', root_element=cmd_box_element)

    # These functions are part of RPA windows element
    text_pattern = text_elm.item.GetTextPattern()
    visible_text_range_list = text_pattern.GetVisibleRanges()

    text_list = []
    cleaned_text_list = []

    # Sometimes it pulls as only one text range object with linebreaks in in the strings
    if len(visible_text_range_list) == 1:
        text_list = visible_text_range_list[0].GetText().split('\r\n')
    else :
        text_list = [text_range.GetText() for text_range in visible_text_range_list]

    # Get any lines of characters that contain non white space
    cleaned_text_list = [text.strip() for text in text_list if text.strip()]

    return cleaned_text_list
