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


def validate_stream(values: List[int]) -> Optional[int]:
    sliding_window = values[:25]  # initial window
    for val in values[25:]:
        if not two_sum(val, sliding_window):
            return val

        sliding_window = sliding_window[1:]
        sliding_window.append(val)

    return None


def main() -> Optional[int]:
    values = read_input("input.txt")
    invalid_val = validate_stream(values)

    return invalid_val


if __name__ == "__main__":
    answer = main()
    print(answer)
