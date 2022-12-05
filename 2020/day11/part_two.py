import copy
from typing import List


OCCUPIED = "#"
EMPTY = "L"
FLOOR = "."


def read_input(name: str) -> List[List[str]]:
    layout: List[List[str]] = []
    with open(name) as f:
        for line in f:
            row = line.strip()
            layout.append(list(row))

    return layout


def set_all_to_occupied(layout: List[List[str]]) -> List[List[str]]:
    for row in layout:
        for index, seat in enumerate(row):
            if seat == EMPTY:
                row[index] = OCCUPIED

    return layout


def is_in_bounds(layout: List[List[str]], row: int, column: int) -> bool:
    return (
        row >= 0
        and row < len(layout)
        and column >= 0
        and column < len(layout[0])
    )


def get_neighbors(layout: List[List[str]], row: int, column: int) -> List[str]:
    neighbors: List[str] = []
    neighbor_movements = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, 1),  # right
        (0, -1),  # left
        (-1, 1),  # up and right
        (-1, -1),  # up and left
        (1, 1),  # down and right
        (1, -1),  # down and left
    ]

    for n in neighbor_movements:
        new_row = row + n[0]
        new_column = column + n[1]
        while is_in_bounds(layout, new_row, new_column):
            seat = layout[new_row][new_column]
            if seat != FLOOR:
                neighbors.append(seat)
                break
            else:
                new_row += n[0]
                new_column += n[1]

    return neighbors


def count_occupied_seats(layout: List[List[str]]) -> int:
    occupied_count = 0
    for row in layout:
        for seat in row:
            if seat == OCCUPIED:
                occupied_count += 1

    return occupied_count


def apply_rules(layout: List[List[str]]) -> int:
    while True:
        prev_layout = copy.deepcopy(layout)
        has_changed = False

        for row_index, row in enumerate(prev_layout):
            for column_index, seat in enumerate(row):
                if seat == FLOOR:
                    continue

                neighbors = get_neighbors(prev_layout, row_index, column_index)

                adjacent_count = 0
                for n in neighbors:
                    if n == OCCUPIED:
                        adjacent_count += 1

                if adjacent_count == 0 and seat == EMPTY:
                    layout[row_index][column_index] = OCCUPIED
                    has_changed = True
                elif adjacent_count >= 5 and seat == OCCUPIED:
                    layout[row_index][column_index] = EMPTY
                    has_changed = True

        if not has_changed:
            break

    return count_occupied_seats(layout)


def main() -> int:
    layout = read_input("input.txt")
    layout = set_all_to_occupied(layout)
    answer = apply_rules(layout)

    return answer


if __name__ == "__main__":
    answer = main()
    print(answer)
