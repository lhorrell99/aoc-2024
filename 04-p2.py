from utils import *
import re

# Filepath
filepath = "./data/12-04-test.txt"


# Problem-specific functions
get_row_len = compose(transpose, len)


def test_pair(str_char: str, search_char: str, skip_char: str = ".") -> bool:
    return True if str_char == search_char or search_char == skip_char else False


def find_all_in_string(string: str, s_pattern: str, skip_char: str = ".") -> int:
    pairwise = [
        list(zip(string[i:], s_pattern))
        for i in range(len(string) - (len(s_pattern) - 1))
    ]
    matches = [all(test_pair(*i) for i in j) for j in pairwise]
    return sum(matches)


def count_in_matrix(data: List[str], s_pattern: List[str], skip_char: str = ".") -> int:
    # Pad input
    padded_data = pad_rows(data)

    # Get row lengths
    row_len = get_row_len(padded_data)
    search_row_len = get_row_len(s_pattern)

    # Flatten
    flattened_data = flatten(padded_data)

    # Build flattened search pattern
    s_pattern = f"{skip_char * (row_len - search_row_len)}".join(s_pattern)

    return find_all_in_string(flattened_data, s_pattern, ".")


# Load data
data = load_data(filepath, "\n")


# Compose a solver
solve = compose(
    array_apply(
        lambda x: x,
        transpose,
        flip_cols,
        compose(transpose, flip_cols),
    ),
    lambda x: [count_in_matrix(i, ["M.S", ".A.", "M.S"]) for i in x],
    sum,
)

print(solve(data))
