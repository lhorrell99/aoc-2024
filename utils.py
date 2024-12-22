from functools import reduce
from typing import List, Tuple, Callable


def array_apply(*funcs: Callable) -> Callable:
    return lambda x: [f(x) for f in funcs]


def build_boolean_intersection(*funcs: Callable) -> Callable:
    return lambda x: all([f(x) for f in funcs])


def compose(*funcs: Callable) -> Callable:
    return lambda x: reduce(lambda acc, f: f(acc), funcs, x)


def duplicate_elements(data: list) -> List[list]:
    return [[i, i] for i in data]


def filter_falsy(data: list) -> list:
    return [i for i in data if i]


def get_abs_differences(data: List[Tuple[int, int]]) -> List[int]:
    return [abs(b - a) for a, b in data]


def get_differences(data: List[Tuple[int, int]]) -> List[int]:
    return [b - a for a, b in data]


def invert(data: List[bool]) -> List[bool]:
    return [not i for i in data]


def load_data(filepath: str, split_delimiter: str) -> list:
    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def load_str(filepath: str) -> str:
    with open(filepath) as file:
        data = file.read()

    return data


def multiply_elements(data: List[int]) -> int:
    return reduce(lambda acc, i: acc * i, data, 1)


def partition(p_func: Callable, l: list) -> Tuple[list, list]:
    return reduce(lambda x, y: x[not p_func(y)].append(y) or x, l, ([], []))


def parse_to_int(data: List[List[str]]) -> List[List[int]]:
    return [[int(j) for j in i] for i in data]


def row_all(data: List[List[bool]]) -> List[bool]:
    return [all(i) for i in data]


def split_strings(data: List[str], split_delimiter: str | None = None) -> list:
    return [i.split(split_delimiter) for i in data]


def sort_sublists(data: List[list]) -> List[list]:
    return [sorted(i) for i in data]


def transpose(data: List[list]) -> List[list]:
    return [list(i) for i in zip(*data)]


def zip_sublists(data: List[list]) -> List[list]:
    return list(zip(*data))


def zip_adjacent(data: list) -> List[Tuple]:
    return list(zip(data, data[1:]))
