from typing import List
from pathlib import Path
import datetime

from file_handler import (
    retrieve_file_as_list,
    update_todays_commits,
    write_list_to_file,
)

COMMIT_TRACKER_PATH = Path.cwd() / "commit_tracker.txt"


def update_commits_count_tracker():
    """Handles updating the count for today in the commits count tracker"""
    current_tracker = retrieve_file_as_list(COMMIT_TRACKER_PATH)

    updated_list = update_todays_commits(current_tracker)

    write_list_to_file(COMMIT_TRACKER_PATH, updated_list)


if __name__ == "__main__":
    update_commits_count_tracker()
