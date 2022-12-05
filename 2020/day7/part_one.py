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


def can_hold_gold_bag(rule: Rule, rules: Dict[str, Rule]) -> bool:
    for hold in rule.holds:
        if hold[0] == "shiny gold" and hold[1] > 0:
            return True
        elif hold[1] > 0:
            parent_rule = rules[hold[0]]
            if parent_rule is not None:
                if can_hold_gold_bag(parent_rule, rules) is True:
                    return True

    return False


def main() -> int:
    rules = read_input("input.txt")
    count = 0
    for key, value in rules.items():
        if can_hold_gold_bag(value, rules):
            count += 1

    return count


if __name__ == "__main__":
    answer = main()
    print(answer)
