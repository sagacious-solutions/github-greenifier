from pathlib import Path
import datetime
from typing import List

commit_tracker = Path.cwd() / "commit_tracker.txt"
TODAYS_DATE = datetime.datetime.now().date()


def retrieve_file_as_list(filename: Path) -> List[str]:
    """Gets the current contents of the file and returns it as a list of strs

    Args:
        filename (Path): Path to file containing list

    Returns:
        List[str]: A list of strings representing rows in the text file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


def write_list_to_file(filename: Path, commit_list: List[str]) -> None:
    """Writes a list of strings onto the file at the filename path

    Args:
        filename (Path): Path of file to write list to
        commit_list (List[str]): List of strings showing commit count for each day
    """
    final_str = "".join(commit_list)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(final_str)


def update_todays_commits(commit_list: List[str]) -> List[str]:
    """Updates the existing commit_list with todays commits, which if none starts with
        todays date, and 1 commit.

    Args:
        commit_list (List[str]): The list of commits to check

    Returns:
        List[str]: The updated list with todays current count.
    """
    todays_date_str = TODAYS_DATE.strftime("%m-%d-%Y")
    daily_count = 1

    if todays_date_str in commit_list[-1]:
        daily_count = get_commit_count_from_line(commit_list[-1])
        daily_count += 1
        commit_list.pop()

    commit_list.append(
        f"{todays_date_str} : I made {daily_count} commits on this day.\n"
    )

    return commit_list


def get_commit_count_from_line(entry: str) -> int:
    """Gets integer count from this txt string.

    12-01-2022 : I made 40 commits on this day.

    Args:
        entry (str): The line to pull from

    Returns:
        int: Integer in this line
    """
    return int(entry.split(" made ")[1].split(" commits")[0])


if __name__ == "__main__":
    current_tracker = retrieve_file_as_list(commit_tracker)

    updated_list = update_todays_commits(current_tracker)

    write_list_to_file(commit_tracker, updated_list)
