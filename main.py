from pathlib import Path

commit_tracker = Path.cwd() / "commit_tracker.txt"


def retrieve_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_file(filename):
    with open(filename, "a", encoding="utf-8") as file:
        file.write("Haha, im so smart. ha ha ha.... i need a job\n")


if __name__ == "__main__":
    current_tracker = retrieve_file(commit_tracker)

    print(current_tracker)

    write_file(commit_tracker)
