from typing import List


def read_input(name: str) -> List[List[str]]:
    grid = []
    with open(name) as f:
        for line in f:
            row = list(line.strip())
            grid.append(row)

    return grid


def main() -> int:
    grid = read_input("input.txt")
    width = len(grid[0])

    # (right, down)
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    product = 1
    for slope in slopes:
        row = 0
        col = 0
        trees_encountered = 0

        while row < len(grid):
            if col > (width - 1):
                col = col % width

            if grid[row][col] == "#":
                trees_encountered += 1

            col += slope[0]
            row += slope[1]

        if trees_encountered > 0:
            product *= trees_encountered

    return product


if __name__ == "__main__":
    answer = main()
    print(answer)
