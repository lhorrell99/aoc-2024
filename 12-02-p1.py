from functools import reduce
from typing import List, Tuple
from utils import *


# Filepath
filepath = "./data/12-02.txt"


# Problem-specific functions
def is_monotonic(data: List[int]) -> bool:
    is_increasing = lambda i: all(x < y for x, y in zip(i, i[1:]))
    return is_increasing(data) or is_increasing(list(reversed(data)))


def is_gradual(data: List[int]):
    return all(abs(x - y) < 4 for x, y in zip(data, data[1:]))


def check_if_safe(data: List[List[int]]) -> List[bool]:
    return [is_gradual(i) and is_monotonic(i) for i in data]


# Load data
data = load_data(filepath, "\n")

# Compose a solver
solve = compose(split_strings, parse_to_int, check_if_safe, sum)

# Print result
print(solve(data))
