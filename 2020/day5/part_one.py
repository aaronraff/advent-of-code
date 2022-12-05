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
    max_seat_id = 0

    for p in passes:
        seat_id = calculate_seat_id(p)
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id


if __name__ == "__main__":
    answer = main()
    print(answer)
