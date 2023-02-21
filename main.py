from typing import List
from pathlib import Path
from RPA.Windows import Windows
import re
import time

win = Windows()

from file_handler import (
    retrieve_file_as_list,
    update_todays_commits,
    write_list_to_file,
)

from terminal_handler import (
    open_terminal,
    get_terminal_focus,
    enter_command_in_terminal,
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
        count = "".join(re.findall("[0-9]", line.split(":")[1]))
        total += int(count)

    return total


def make_commit(total_commits):
    """Opens the terminal, adds the commit_tracker to git tracking. Commits and pushes
        the newest changes. Closes the terminal.

    Args:
        total_commits (int): Total count of commits listed in the tracker file
    """
    open_terminal()
    terminal_element = get_terminal_focus()
    repo_path = Path.cwd().as_posix()
    enter_command_in_terminal(terminal_element, f"cd {repo_path}")
    enter_command_in_terminal(terminal_element, f"git pull")
    enter_command_in_terminal(terminal_element, f"git add commit_tracker.txt")
    enter_command_in_terminal(
        terminal_element, f'git commit -m "Heres commit #{total_commits}"'
    )
    enter_command_in_terminal(terminal_element, f"git push")
    win.close_window(terminal_element)


def main_loop():
    MINUTE_IN_SECS = 60
    HOUR_IN_MINUTES = 60
    WAIT_BETWEEN_COMMITS_SECS = HOUR_IN_MINUTES * MINUTE_IN_SECS
    print(
        "Now starting infinite commit bot. The bot will commit once an hour as"
        " long as this continues to run. Press ctrl-C to quit."
    )
    while True:
        total_commits = update_commits_count_tracker()
        make_commit(total_commits)
        print(
            f"Just made commit #{total_commits}. \nWill wait"
            f" {WAIT_BETWEEN_COMMITS_SECS} seconds and then make another.\n"
            " Ctrl-C to exit."
        )
        time.sleep(WAIT_BETWEEN_COMMITS_SECS)


if __name__ == "__main__":
    main_loop()
