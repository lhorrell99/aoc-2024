from typing import List
from utils import *

# Filepath
filepath = "./data/12-02.txt"


# Problem-specific functions
sum_differences = compose(
    zip_adjacent,
    get_differences,
    sum,
)


def bias_ascending(data: List[int]) -> List[int]:
    return data if sum_differences(data) >= 0 else list(reversed(data))


def apply_strictly_ascending(data: List[int]) -> List[bool]:
    return [a < b for a, b in zip_adjacent(data)]


# TODO second chance function with generic tester function
def is_strictly_ascending(data: List[int]):
    strictly_ascending = apply_strictly_ascending(data)

    # Return list if it passes
    if all(strictly_ascending):
        return data

    # Find first failing element
    fail_idx = strictly_ascending.index(False)

    # Remove it
    data.pop(fail_idx)

    # Retry
    strictly_ascending = apply_strictly_ascending(data)

    # Return list if it passes
    if all(strictly_ascending):
        return data

    # Return an empty list if still failing
    return []


def apply_lower_gradient(data: List[int], limit: int = 1) -> bool:
    return [b - a >= limit for a, b in zip_adjacent(data)]


def is_lower_gradient_safe(data):
    lower_gradient_safe = apply_lower_gradient(data)

    # Return list if it passes
    if all(lower_gradient_safe):
        return data

    # Find first failing element
    fail_idx = lower_gradient_safe.index(False)

    # Remove it
    data.pop(fail_idx)

    # Retry
    lower_gradient_safe = apply_lower_gradient(data)

    # Return list if it passes
    if all(lower_gradient_safe):
        return data

    # Return an empty list if still failing
    return []


def apply_upper_gradient(data: List[int], limit: int = 3) -> bool:
    return [b - a <= limit for a, b in zip_adjacent(data)]


def is_upper_gradient_safe(data):
    upper_gradient_safe = apply_upper_gradient(data)

    # Return list if it passes
    if all(upper_gradient_safe):
        return data

    # # Find first failing element
    # fail_idx = upper_gradient_safe.index(False)

    # # Remove it
    # data.pop(fail_idx)

    # # Retry
    # upper_gradient_safe = apply_upper_gradient(data)

    # # Return list if it passes
    # if all(upper_gradient_safe):
    #     return data

    # # Return an empty list if still failing
    return []


def filter_multi_edits(a_data: List[list], b_data: List[list]) -> List[list]:
    if len(a_data) != len(b_data):
        raise ValueError("a_data and b_data must be of the same length")

    pairwise = zip(a_data, b_data)

    return [b for a, b in pairwise if len(b) >= len(a) - 1]


# Load data
data = load_data(filepath, "\n")


# Compose a solver
preprocess = compose(
    split_strings,
    parse_to_int,
)

test_safety = compose(
    lambda x: list(map(bias_ascending, x)),
    lambda x: list(map(is_strictly_ascending, x)),
    # filter_falsy,
    lambda x: list(map(is_lower_gradient_safe, x)),
    # filter_falsy,
    lambda x: list(map(is_upper_gradient_safe, x)),
    # filter_falsy,
)


def solve(data):
    # Preprocess
    puzzle = preprocess(data)

    # Find safe candidates
    safe_candidates = test_safety(puzzle)

    # filter any multi-edited lists
    single_edited_safe_candidates = filter_multi_edits(puzzle, safe_candidates)

    return len(single_edited_safe_candidates)


# Print result
print(solve(data))
