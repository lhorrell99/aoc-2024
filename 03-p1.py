import re
from utils import *

# Filepath
filepath = "./data/12-03.txt"


# Load data
data = load_str(filepath)

# Compose a solver
solve = compose(
    lambda x: re.findall("mul\([0-9]*,[0-9]*\)", x),
    lambda x: [i[4:-1].split(",") for i in x],
    parse_to_int,
    lambda x: [multiply_elements(i) for i in x],
    sum,
)

# Print result
print(solve(data))
