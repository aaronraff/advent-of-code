from typing import List


def read_input(name: str) -> List[int]:
    values: List[int] = []
    with open(name) as f:
        for line in f:
            values.append(int(line.strip()))

    return values


def possible_ways_to_get_here(
    jolts: List[int],
    index: int,
    intermediate_possibilies: List[int],
) -> int:
    count = 0
    prev_indexes = [i for i in range(index - 3, index) if i >= 0]
    for prev_index in prev_indexes:
        diff = jolts[index] - jolts[prev_index]
        if diff <= 3:
            count += intermediate_possibilies[prev_index]

    return count


def possible_chains(jolts: List[int]) -> int:
    jolts.sort()
    jolts.insert(0, 0)  # outlet joltage
    jolts.append(jolts[-1] + 3)  # device's built in adapter
    intermediate_possibilities = [1]  # how many ways to get to each adapter

    for index in range(1, len(jolts)):
        possibilites = possible_ways_to_get_here(
            jolts,
            index,
            intermediate_possibilities,
        )

        intermediate_possibilities.append(possibilites)

    return intermediate_possibilities[-1]


def main() -> int:
    jolts = read_input("input.txt")
    answer = possible_chains(jolts)

    return answer


if __name__ == "__main__":
    answer = main()
    print(answer)
