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

    for index, first in enumerate(nums):
        for second in nums[index+1:]:
            target = 2020 - (first + second)
            if target in map_:
                return first * second * target
            else:
                map_[first] = True

    return None


if __name__ == "__main__":
    answer = main()
    print(answer)
