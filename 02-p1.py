from typing import List
from utils import *

# Filepath
filepath = "./data/12-02.txt"


# Problem-specific functions
sum_differences = compose(zip_adjacent, get_differences, sum)


def bias_ascending(data: List[int]) -> List[int]:
    return data if sum_differences(data) >= 0 else list(reversed(data))


def is_strictly_ascending(data: List[int]) -> bool:
    return data == sorted(data)


def test_lower_gradient_limit(data: List[int], limit: int = 1) -> bool:
    return all(b - a >= limit for a, b in zip_adjacent(data))


def test_upper_gradient_limit(data: List[int], limit: int = 3) -> bool:
    return all(b - a <= limit for a, b in zip_adjacent(data))


# Load data
data = load_data(filepath, "\n")


# Compose a solver
solve = compose(
    split_strings,
    parse_to_int,
    lambda x: list(map(bias_ascending, x)),
    lambda x: list(filter(is_strictly_ascending, x)),
    lambda x: list(filter(test_lower_gradient_limit, x)),
    lambda x: list(filter(test_upper_gradient_limit, x)),
    len,
)

# Print result
print(solve(data))
