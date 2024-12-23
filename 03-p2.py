import re
from utils import *

# Filepath
filepath = "./data/12-03.txt"


# Problem-specific functions
def trim_string(string: str, start_cut: int, end_cut: int) -> str:
    return string[start_cut:-end_cut]


process_mul_command = compose(
    lambda x: trim_string(x, 4, 1),
    lambda x: x.split(","),
    lambda x: [int(i) for i in x],
    multiply_elements,
)


def parse_list_element_builder() -> Callable:
    active = True

    def parse_list_element(acc: int, i: str) -> int:
        nonlocal active

        match i:
            case "don't()":
                active = False
                return acc
            case "do()":
                active = True
                return acc
            case _:
                # Default case is a mul command
                if active:
                    return acc + process_mul_command(i)
                else:
                    return acc

    return parse_list_element


# Load data
data = load_str(filepath)

# Compose a solver
solve = compose(
    lambda x: re.findall(r"mul\([0-9]*,[0-9]*\)|don't\(\)|do\(\)", x),
    lambda x: reduce(parse_list_element_builder(), x, 0),
)

# Print result
print(solve(data))
