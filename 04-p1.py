from utils import *

# Filepath
filepath = "./data/12-04.txt"


# Problem-specific functions
def skew(data: List[str], s_char: str = "*") -> List[str]:
    return [s_char * i + s + s_char * (len(data) - (i + 1)) for i, s in enumerate(data)]


count_all_in_sublists = compose(pad_rows, flatten, lambda x: x.count("XMAS"))


# Load data
data = load_data(filepath, "\n")

# Compose a solver
solve = compose(
    array_apply(
        lambda x: x,
        transpose,
        flip_cols,
        compose(transpose, flip_cols),
        compose(flip_cols, skew, transpose),
        compose(skew, transpose),
        compose(flip_rows, skew, transpose),
        compose(flip_rows, flip_cols, skew, transpose),
    ),
    lambda x: [count_all_in_sublists(i) for i in x],
    sum,
)

print(solve(data))
