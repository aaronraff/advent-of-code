from typing import List
from dataclasses import dataclass


@dataclass
class Entry:
    lower_bound: int
    upper_bound: int
    letter: str
    password: str


def read_input(name: str) -> List[Entry]:
    entries = []
    with open(name) as f:
        for line in f:
            parts = line.split(" ")
            bounds = parts[0].split("-")
            entry = Entry(
                lower_bound=int(bounds[0]),
                upper_bound=int(bounds[1]),
                letter=parts[1][0],
                password=parts[2].strip(),
            )
            entries.append(entry)

    return entries


def count_occurrences(password: str, letter: str) -> int:
    count = 0
    for char in password:
        if char == letter:
            count += 1

    return count


def main() -> int:
    entries = read_input("input.txt")
    valid = 0

    for entry in entries:
        count = count_occurrences(entry.password, entry.letter)
        if count >= entry.lower_bound and count <= entry.upper_bound:
            valid += 1

    return valid


if __name__ == "__main__":
    answer = main()
    print(answer)
