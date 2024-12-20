from typing import List
from utils import *

# Filepath
filepath = "./data/12-02-test.txt"


# Problem-specific functions
sum_differences = compose(
    zip_adjacent,
    get_differences,
    sum,
)


def bias_ascending(data: List[int]) -> List[int]:
    return data if sum_differences(data) >= 0 else list(reversed(data))


def is_strictly_ascending(data: List[int]) -> bool:
    # Return if list passes outright
    s_data = sorted(data)

    if data == s_data:
        return data

    divergent_index = None

    for i, value in enumerate(data):
        if value != s_data[i]:
            divergent_index = i
            break

    candidate_a = data[0 : divergent_index - 1] + data[divergent_index:]
    candidate_b = data[0:divergent_index] + data[divergent_index + 1 :]

    if candidate_a == sorted(candidate_a):
        return candidate_a

    if candidate_b == sorted(candidate_b):
        return candidate_b

    # No candidates found
    return None


# TODO: final error is that a weakly ascending list is not properly addressed in strictly ascending func - go back to original implementation probably...

def apply_lower_gradient_limit(data: List[int], limit: int = 1) -> bool:
    return all(b - a >= limit for a, b in zip_adjacent(data))


def apply_upper_gradient_limit(data: List[int], limit: int = 3) -> bool:
    return all(b - a <= limit for a, b in zip_adjacent(data))


# Load data
data = load_data(filepath, "\n")


# Compose a solver
solve = compose(
    split_strings,
    parse_to_int,
    lambda x: list(map(bias_ascending, x)),
    lambda x: list(map(is_strictly_ascending, x)),
    lambda x: list(filter(is_strictly_ascending, x)),
    lambda x: list(filter(apply_lower_gradient_limit, x)),
    lambda x: list(filter(apply_upper_gradient_limit, x)),
    len,
)

# Print result
print(solve(data))
