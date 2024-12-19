from typing import List, Tuple
from utils import *


def get_differences(data: List[Tuple[int, int]]) -> List[int]:
    return [abs(a - b) for a, b in data]


filepath = "./data/12-01.txt"

# Load data
data = load_data(filepath, "\n")

# Compose a solver
solve = compose(
    split_strings,
    transpose,
    sort_sublists,
    parse_to_int,
    zip_sublists,
    get_differences,
    sum,
)

# Print result
print(solve(data))
