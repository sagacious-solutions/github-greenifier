from typing import List
from pathlib import Path
from RPA.Windows import Windows
import re

win = Windows()



from file_handler import (
    retrieve_file_as_list,
    update_todays_commits,
    write_list_to_file,
)

COMMIT_TRACKER_PATH = Path.cwd() / "commit_tracker.txt"


def update_commits_count_tracker() -> int:
    """Handles updating the count for today in the commits count tracker

    Returns:
        int: The total amount of commits ever made by the bot
    """
    current_tracker = retrieve_file_as_list(COMMIT_TRACKER_PATH)

    updated_list = update_todays_commits(current_tracker)

    write_list_to_file(COMMIT_TRACKER_PATH, updated_list)

    return get_total_commit_count(updated_list)

def get_total_commit_count(updated_list: List[str]) -> int:
    total = 0
    for line in updated_list:
        count = ''.join(re.findall('[0-9]',line.split(':')[1]))
        total += int(count)

    return total

def open_terminal():
    win.windows_run("cmd")

def get_terminal_focus():
    return win.control_window('subname:"cmd.exe"')

def navigate_to_repo_directory(element):
    repo_path = Path.cwd().as_posix()
    enter_command_in_terminal(element, f"cd {repo_path}")


def enter_command_in_terminal(element, command):
    win.send_keys(element, command, send_enter=True)


def make_commit(total_commits):
    open_terminal()
    terminal_element = get_terminal_focus()
    navigate_to_repo_directory(terminal_element)
    enter_command_in_terminal(terminal_element, f"git add commit_tracker.txt")
    enter_command_in_terminal(terminal_element, f'git commit -m "Heres commit #{total_commits}"')
    enter_command_in_terminal(terminal_element, f"git push")
    win.close_window(terminal_element)


if __name__ == "__main__":
    total_commits = update_commits_count_tracker()
    make_commit(total_commits)

    print("Completed")