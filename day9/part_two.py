from typing import Dict, List, Optional


def read_input(name: str) -> List[int]:
    values: List[int] = []
    with open(name) as f:
        for line in f:
            values.append(int(line.strip()))

    return values


def two_sum(target: int, values: List[int]) -> bool:
    compliments: Dict[int, bool] = {}
    for val in values:
        if val in compliments:
            return True

        compliments[target-val] = True

    return False


def get_invalid_value(values: List[int]) -> Optional[int]:
    sliding_window = values[:25]  # initial window
    for val in values[25:]:
        if not two_sum(val, sliding_window):
            return val

        sliding_window = sliding_window[1:]
        sliding_window.append(val)

    return None


def get_contiguous_list(target: int, values: List[int]) -> Optional[List[int]]:
    window: List[int] = []
    total = 0
    for val in values:
        window.append(val)
        total += val

        if total == target:
            return window

        while total > target:
            removed_val = window[0]
            window = window[1:]
            total -= removed_val
            if total == target:
                return window

    return None


def main() -> Optional[int]:
    values = read_input("input.txt")
    invalid_val = get_invalid_value(values)

    if invalid_val is None:
        return None

    contiguous_list = get_contiguous_list(invalid_val, values)

    if contiguous_list is None:
        return None

    return min(contiguous_list) + max(contiguous_list)


if __name__ == "__main__":
    answer = main()
    print(answer)
