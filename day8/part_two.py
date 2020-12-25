from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


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


def evaluate_instructions(instructions: List[Instruction]) -> Tuple[int, bool]:
    """
    Returns a tuple with the accumulator value, and a bool indicating whether
    or not there was an infinite loop.
    """
    acc = 0
    eip = 0
    already_evaluated: Dict[int, int] = {}

    while eip < (len(instructions) - 1) and eip not in already_evaluated:
        already_evaluated[eip] = 1
        instruction = instructions[eip]

        if instruction.operation == Operation.ACC:
            acc += instruction.argument
            eip += 1
        elif instruction.operation == Operation.JMP:
            eip += instruction.argument
        elif instruction.operation == Operation.NOP:
            eip += 1

    return acc, eip < (len(instructions) - 1)


def main() -> Optional[int]:
    instructions = read_input("input.txt")

    for index, instruction in enumerate(instructions):
        initial_op = instruction.operation
        initial_arg = instruction.argument

        if instruction.operation == Operation.NOP:
            instruction.operation = Operation.JMP
        elif instruction.operation == Operation.JMP:
            instruction.operation = Operation.NOP

        acc, infinte_loop = evaluate_instructions(instructions)
        if not infinte_loop:
            return acc

        # reset to the old value before trying to flip another instruction
        instruction.operation = initial_op
        instruction.argument = initial_arg

    return None


if __name__ == "__main__":
    answer = main()
    print(answer)
