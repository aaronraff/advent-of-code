from typing import List, Optional


def read_input(name: str) -> List[int]:
    nums = []
    with open(name) as f:
        for line in f:
            nums.append(int(line))

    return nums


def main() -> Optional[int]:
    nums = read_input("input.txt")
    map_ = {}

    for num in nums:
        target = 2020 - num
        if target in map_:
            return num * target
        else:
            map_[num] = True

    return None


if __name__ == "__main__":
    answer = main()
    print(answer)
