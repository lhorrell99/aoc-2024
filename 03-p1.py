import re
from utils import *

# Filepath
filepath = "./data/12-03.txt"


# Problem-specific functions
def trim_string(string: str, start_cut: int, end_cut: int) -> str:
    return string[start_cut:-end_cut]


# Load data
data = load_str(filepath)

# Compose a solver
solve = compose(
    lambda x: re.findall(r"mul\([0-9]*,[0-9]*\)", x),
    lambda x: [trim_string(i, 4, 1) for i in x],
    lambda x: split_strings(x, ","),
    parse_to_int,
    lambda x: [multiply_elements(i) for i in x],
    sum,
)

# Print result
print(solve(data))
