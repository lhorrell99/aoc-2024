from typing import List, Tuple
from utils import *

# Filepath
filepath = "./data/12-01.txt"


# Problem-specific functions
def get_frequency_counts(a: List[int], b: List[int]) -> List[Tuple[int, int]]:
    return [(i, b.count(i)) for i in a]


def get_multiples(data: List[Tuple[int, int]]) -> List[int]:
    return [a * b for a, b in data]


# Load data
data = load_data(filepath, "\n")

# Compose a solver
solve = compose(
    split_strings,
    transpose,
    sort_sublists,
    parse_to_int,
    lambda x: get_frequency_counts(*x),
    get_multiples,
    sum,
)

# Print result
print(solve(data))
