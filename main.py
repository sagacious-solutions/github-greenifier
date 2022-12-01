from pathlib import Path
import datetime
from typing import List

commit_tracker = Path.cwd() / "commit_tracker.txt"
TODAYS_DATE = datetime.datetime.now().date()


def retrieve_file_as_list(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


def write_file(filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Haha, im so smart. ha ha ha.... i need a job\n")


def update_todays_commits(commit_list: List[str]):
    todays_date_str = TODAYS_DATE.strftime("%m-%d-%Y")

    for str in commit_list:
        if todays_date_str in str:
            print("This is the line")
            daily_count = get_commit_count_from_line(str)
            print(f"This was {daily_count} commits on this day.")


def get_commit_count_from_line(entry: str):
    number_str = entry.split(" made ")[1].split(" commits")[0]
    return int(number_str)


if __name__ == "__main__":
    current_tracker = retrieve_file_as_list(commit_tracker)

    update_todays_commits(current_tracker)
