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
    row = 0
    col = 0
    width = len(grid[0])
    trees_encountered = 0

    while row < len(grid):
        if col > (width - 1):
            col = col % width

        if grid[row][col] == "#":
            trees_encountered += 1

        col += 3
        row += 1

    return trees_encountered


if __name__ == "__main__":
    answer = main()
    print(answer)
