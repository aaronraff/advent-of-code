from typing import List


def read_input(name: str) -> List[List[str]]:
    grouped_answers: List[List[str]] = []
    with open(name) as f:
        current: List[str] = []
        for line in f:
            # start of a new group
            if line == "\n":
                grouped_answers.append(current)
                current = []
            else:
                current.append(line.strip())

    # add the last group that was read
    grouped_answers.append(current)
    return grouped_answers


def count_agreed_answers(groups_answers: List[str]) -> int:
    agreed = list(groups_answers[0])
    for answers in groups_answers[1:]:
        agreed_copy = agreed.copy()
        for a in agreed_copy:
            if a not in answers:
                pos = agreed.index(a)
                del agreed[pos]

    return len(agreed)


def main() -> int:
    grouped_answers = read_input("input.txt")
    count = 0
    for groups_answers in grouped_answers:
        count += count_agreed_answers(groups_answers)

    return count


if __name__ == "__main__":
    answer = main()
    print(answer)
