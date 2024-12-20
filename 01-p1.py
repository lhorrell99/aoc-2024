from utils import *

# Filepath
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
    get_abs_differences,
    sum,
)

# Print result
print(solve(data))
