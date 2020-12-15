import re
from dataclasses import dataclass
from typing import Callable, Dict, List


@dataclass
class Requirement:
    key: str
    validation_func: Callable[[str], bool]


def read_input(name: str) -> List[Dict[str, str]]:
    passports: List[Dict[str, str]] = []
    with open(name) as f:
        current: Dict[str, str] = {}
        for line in f:
            # start of a new passport
            if line == "\n":
                passports.append(current)
                current = {}
            else:
                parts = line.split(" ")
                for part in parts:
                    key, value = part.split(":")
                    current[key] = value.strip()

    # add the last passport that was read
    passports.append(current)
    return passports


def validate_height(height: str) -> bool:
    units = height[-2:]
    value = height[:-2]

    if units == "cm":
        return int(value) >= 150 and int(value) <= 193
    elif units == "in":
        return int(value) >= 59 and int(value) <= 76
    else:
        return False


def check_passports(passports: List[Dict[str, str]]) -> int:
    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    requirements: List[Requirement] = [
        Requirement("byr", lambda x: int(x) >= 1920 and int(x) <= 2002),
        Requirement("iyr", lambda x: int(x) >= 2010 and int(x) <= 2020),
        Requirement("eyr", lambda x: int(x) >= 2020 and int(x) <= 2030),
        Requirement("hgt", validate_height),
        Requirement("hcl", lambda x: bool(re.match("^#[0-9a-f]{6}$", x))),
        Requirement("ecl", lambda x: x in valid_eye_colors),
        Requirement("pid", lambda x: bool(re.match("^[0-9]{9}$", x))),
    ]
    valid = 0

    for passport in passports:
        if (
            all(r.key in passport for r in requirements)
            # ignored because of https://github.com/python/mypy/issues/5485
            and all(
                r.validation_func(passport[r.key])  # type: ignore
                for r in requirements
            )
        ):
            valid += 1

    return valid


def main() -> int:
    passports = read_input("input.txt")
    valid = check_passports(passports)
    return valid


if __name__ == "__main__":
    answer = main()
    print(answer)
