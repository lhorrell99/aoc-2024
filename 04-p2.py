from utils import *
from itertools import islice

# Filepath
filepath = "./data/12-04.txt"


# Problem-specific functions
get_row_len = compose(transpose, len)


def get_row_slice(matrix: List[str], start: int, r_splice: int) -> List[str]:
    return list(islice(matrix, start, start + r_splice))


def get_all_submatrices(
    matrix: List[str], r_splice: int, c_splice: int
) -> List[List[str]]:
    process = compose(
        lambda x: [get_row_slice(x, i, r_splice) for i, _ in enumerate(x)],
        lambda x: [transpose(i) for i in x],
        lambda x: [get_row_slice(y, i, c_splice) for y in x for i, _ in enumerate(y)],
        lambda x: [transpose(i) for i in x],
        lambda x: list(filter(lambda y: len(flatten(y)) == r_splice * c_splice, x)),
    )

    return process(matrix)


def test_pair(str_char: str, search_char: str, skip_char: str = ".") -> bool:
    return True if str_char == search_char or search_char == skip_char else False


def test_match(search: List[str], match: List[str], skip_char: str = ".") -> bool:
    return all(test_pair(*i, skip_char) for i in zip(flatten(search), flatten(match)))


# Load data
data = load_data(filepath, "\n")

# Define search matrix
s_matrix = ["M.S", ".A.", "M.S"]

# Compose a solver
solve = compose(
    array_apply(
        lambda x: x,
        transpose,
        flip_cols,
        compose(transpose, flip_cols),
    ),
    lambda x: [get_all_submatrices(i, len(s_matrix), get_row_len(s_matrix)) for i in x],
    lambda x: [i for j in x for i in j],
    lambda x: [test_match(i, s_matrix) for i in x],
    sum,
)

print(solve(data))
