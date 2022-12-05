from typing import List


def read_input(name: str) -> List[int]:
    values: List[int] = []
    with open(name) as f:
        for line in f:
            values.append(int(line.strip()))

    return values


def chain_adapters(jolts: List[int]) -> int:
    counts = {1: 0, 3: 0}
    jolts.sort()
    jolts.insert(0, 0)  # outlet joltage
    jolts.append(jolts[-1] + 3)  # device's built in adapter

    for index in range(1, len(jolts)):
        diff = jolts[index] - jolts[index-1]
        counts[diff] += 1

    return counts[1] * counts[3]


def main() -> int:
    jolts = read_input("input.txt")
    answer = chain_adapters(jolts)

    return answer


if __name__ == "__main__":
    answer = main()
    print(answer)
