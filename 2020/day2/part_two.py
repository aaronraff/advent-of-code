from typing import List
from dataclasses import dataclass


@dataclass
class Entry:
    positions: List[int]
    letter: str
    password: str


def read_input(name: str) -> List[Entry]:
    entries = []
    with open(name) as f:
        for line in f:
            parts = line.split(" ")
            positions_raw = parts[0].split("-")
            positions = list(map(int, positions_raw))

            entry = Entry(
                positions=positions,
                letter=parts[1][0],
                password=parts[2].strip(),
            )
            entries.append(entry)

    return entries


def count_occurrences(password: str, letter: str, positions: List[int]) -> int:
    count = 0
    for pos in positions:
        if password[pos-1] == letter:
            count += 1

    return count


def main() -> int:
    entries = read_input("input.txt")
    valid = 0

    for entry in entries:
        count = count_occurrences(entry.password, entry.letter, entry.positions)
        if count == 1:
            valid += 1

    return valid


if __name__ == "__main__":
    answer = main()
    print(answer)
