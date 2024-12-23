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


test_all_conditions = build_boolean_intersection(
    is_strictly_ascending,
    test_lower_gradient_limit,
    test_upper_gradient_limit,
)


def is_valid(data: List[int]) -> bool:
    # Test if safe outright
    if test_all_conditions(data):
        return True

    # Brute force removing elements
    for i, _ in enumerate(data):
        test = data[0:i] + data[i + 1 :]
        if test_all_conditions(test):
            return True

    return False


# Load data
data = load_data(filepath, "\n")


# Compose a solver
preprocess = compose(
    split_strings,
    parse_to_int,
    lambda x: list(map(bias_ascending, x)),
)

get_valid_candidate_count = compose(
    lambda x: list(filter(is_valid, x)),
    len,
)


def solve(data):
    puzzle = preprocess(data)
    return get_valid_candidate_count(puzzle)


# Print result
print(solve(data))
