from utils import *
import re

# Filepath
filepath = "./data/12-04.txt"


# Problem-specific functions
get_row_len = compose(transpose, len)


def find_all_in_string(string: str, s_pattern: str, skip_char: str = ".") -> int:
    
    
    pass


def count_in_matrix(data: List[str], s_pattern: List[str], skip_char: str = ".") -> int:
    # Pad input
    padded_data = pad_rows(data, ".")

    # Get row length
    row_len = get_row_len(padded_data)
    search_row_len = get_row_len(s_pattern)

    # Flatten
    flattened_data = flatten(padded_data)

    # Build 2D search pattern
    s_pattern = f"{skip_char * (row_len - search_row_len)}".join(s_pattern)

    print(s_pattern)
    # # Build search regex
    # search = re.compile("")


print(get_row_len(["xox", "xox"]))

print(count_in_matrix(["xox", "xox", "xox"], ["xox", "xox"]))
# def skew(data: List[str], s_char: str = "*") -> List[str]:
#     return [s_char * i + s + s_char * (len(data) - (i + 1)) for i, s in enumerate(data)]


# count_all_in_sublists = compose(pad_rows, flatten, lambda x: x.count("XMAS"))


# # Load data
# data = load_data(filepath, "\n")

# # Compose a solver
# solve = compose(
#     array_apply(
#         lambda x: x,
#         transpose,
#         flip_cols,
#         compose(transpose, flip_cols),
#     ),
#     lambda x: [count_all_in_sublists(i) for i in x],
#     sum,
# )

# print(solve(data))
