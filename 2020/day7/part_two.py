from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Rule:
    bag: str
    holds: List[Tuple[str, int]]  # (bag color, amount)


def read_input(name: str) -> Dict[str, Rule]:
    rules: Dict[str, Rule] = {}
    with open(name) as f:
        for line in f:
            line = line.strip()[:-1]  # remove period
            parts = line.split("contain")

            bag = " ".join(parts[0].split(" ")[:2])
            contains_list = parts[1].split(",")

            holds: List[Tuple[str, int]] = []
            for contains in contains_list:
                stripped = contains.strip()
                contains_parts = stripped.split(" ")

                count = contains_parts[0]
                if count == "no":
                    amount = 0
                else:
                    amount = int(count)

                bag_color = " ".join(contains_parts[1:3])
                holds.append((bag_color, amount))

            rules[bag] = Rule(bag=bag, holds=holds)

    return rules


def gold_bag_contains(rule: Rule, rules: Dict[str, Rule]) -> int:
    count = 0
    for hold in rule.holds:
        if hold[1] == 0:
            continue

        child = rules[hold[0]]
        if child is not None:
            count += hold[1] + (hold[1] * gold_bag_contains(child, rules))
        else:
            count += hold[1]

    return count


def main() -> int:
    count = 0
    rules = read_input("input.txt")
    rule = rules["shiny gold"]

    if rule is not None:
        count = gold_bag_contains(rule, rules)

    return count


if __name__ == "__main__":
    answer = main()
    print(answer)
