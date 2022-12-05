from typing import Dict, List


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


def check_passports(passports: List[Dict[str, str]]) -> int:
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0

    for passport in passports:
        if all(key in passport for key in required):
            valid += 1

    return valid


def main() -> int:
    passports = read_input("input.txt")
    valid = check_passports(passports)
    return valid


if __name__ == "__main__":
    answer = main()
    print(answer)
