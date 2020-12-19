from typing import List


def read_input(name: str) -> List[str]:
    passes: List[str] = []
    with open(name) as f:
        for line in f:
            passes.append(line.strip())

    return passes


def calculate_seat_id(boarding_pass: str) -> int:
    row_movements = boarding_pass[:7]
    col_movements = boarding_pass[7:]
    rows = [x for x in range(128)]
    cols = [x for x in range(8)]

    for m in row_movements:
        if m == "F":
            rows = rows[:len(rows) // 2]
        else:
            rows = rows[len(rows) // 2:]

    for m in col_movements:
        if m == "L":
            cols = cols[:len(cols) // 2]
        else:
            cols = cols[len(cols) // 2:]

    return rows[0] * 8 + cols[0]


def main() -> int:
    passes = read_input("input.txt")
    seat_ids: List[int] = []

    for p in passes:
        seat_ids.append(calculate_seat_id(p))

    for s in seat_ids:
        if s + 1 not in seat_ids and s + 2 in seat_ids:
            return s + 1

    return -1


if __name__ == "__main__":
    answer = main()
    print(answer)
