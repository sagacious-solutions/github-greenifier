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
    get_terminal_text_as_list,
    close_terminal_pop_up,
)

from failure_alert import email_alert_on_failure


COMMIT_TRACKER_PATH = Path.cwd() / "commit_tracker.txt"


def update_commits_count_tracker() -> None:
    """Handles updating the count for today in the commits count tracker

    Returns:
        int: The total amount of commits ever made by the bot
    """
    current_tracker = retrieve_file_as_list(COMMIT_TRACKER_PATH)

    updated_list = update_todays_commits(current_tracker)

    write_list_to_file(COMMIT_TRACKER_PATH, updated_list)


def get_commit_count_from_git():
    """Opens the terminal, navigates to the repo folder, checks the commit history,
        extracts commit count number from terminal and returns it.

    Args:
        total_commits (int): The total amount of commits in the commit history
    """
    SECOND_TO_LAST_ITEM_IN_TERMINAL = -2
    open_terminal()
    terminal_element = get_terminal_focus()
    repo_path = Path.cwd().as_posix()
    enter_command_in_terminal(terminal_element, f"cd {repo_path}")
    enter_command_in_terminal(terminal_element, "cls")
    enter_command_in_terminal(terminal_element, f"git rev-list --all --count")
    term_text_list = get_terminal_text_as_list(terminal_element)
    close_terminal_pop_up()
    return int(term_text_list[SECOND_TO_LAST_ITEM_IN_TERMINAL]) + 1


def make_commit(total_commits : int) -> None:
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
    close_terminal_pop_up()

def commit_and_update_tracker(wait_between_commits_secs : int) -> None:
    """Gets the current commit count, updates the commit tracker and then commits
        the changes

    Args:
        wait_between_commits_secs (int): Wait time to display in message
    """    
    total_commits = get_commit_count_from_git()
    update_commits_count_tracker()
    make_commit(total_commits)
    print(
        f"Just made commit #{total_commits}. \nWill wait"
        f" {wait_between_commits_secs} seconds and then make another.\n"
        " Ctrl-C to exit."
    )
    
    

def main_loop():
    MINUTE_IN_SECS = 60
    HOUR_IN_MINUTES = 60
    WAIT_BETWEEN_COMMITS_SECS = HOUR_IN_MINUTES * MINUTE_IN_SECS
    WAIT_FOR_RETRY_ON_ERROR_SECS = 60
    print(
        "Now starting infinite commit bot. The bot will commit once an hour as"
        " long as this continues to run. Press ctrl-C to quit."
    )
    while True:
        try :
            commit_and_update_tracker(WAIT_BETWEEN_COMMITS_SECS)            
        except IndexError as err:
            failure_str = (
                "The commit loop had a fault. Likely it didn't get the"
                f" element for console. Waiting {WAIT_FOR_RETRY_ON_ERROR_SECS}"
                f" seconds and then will try again. \n{err}"
            )
            print(failure_str)
            email_alert_on_failure(failure_str)
            time.sleep(WAIT_FOR_RETRY_ON_ERROR_SECS)
        except Exception as err :
            failure_str = (
                "The commit loop had an unknown fault."
                f" Waiting {WAIT_FOR_RETRY_ON_ERROR_SECS}"
                f" seconds and then will try again. \n{err}"
            )
            print(failure_str)
            email_alert_on_failure(failure_str)
            time.sleep(WAIT_FOR_RETRY_ON_ERROR_SECS)            
            
        time.sleep(WAIT_BETWEEN_COMMITS_SECS)
    

if __name__ == "__main__" :    
    main_loop()
