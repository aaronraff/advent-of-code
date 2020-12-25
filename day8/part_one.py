from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict, List


class Operation(Enum):
    NOP = auto()
    ACC = auto()
    JMP = auto()


@dataclass
class Instruction:
    operation: Operation
    argument: int


def read_input(name: str) -> List[Instruction]:
    instructions: List[Instruction] = []
    with open(name) as f:
        for line in f:
            operation, argument = line.strip().split(" ")
            arg = int(argument)

            op = Operation.NOP
            if operation == "acc":
                op = Operation.ACC
            elif operation == "jmp":
                op = Operation.JMP

            instructions.append(
                Instruction(
                    operation=op,
                    argument=arg,
                )
            )

    return instructions


def evaluate_instructions(instructions: List[Instruction]) -> int:
    acc = 0
    eip = 0
    already_evaluated: Dict[int, int] = {}

    while eip not in already_evaluated:
        already_evaluated[eip] = 1
        instruction = instructions[eip]

        if instruction.operation == Operation.ACC:
            acc += instruction.argument
            eip += 1
        elif instruction.operation == Operation.JMP:
            eip += instruction.argument
        elif instruction.operation == Operation.NOP:
            eip += 1

    return acc


def main() -> int:
    instructions = read_input("input.txt")
    acc = evaluate_instructions(instructions)

    return acc


if __name__ == "__main__":
    answer = main()
    print(answer)
