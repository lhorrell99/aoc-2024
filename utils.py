from functools import reduce
from typing import List


def compose(*funcs):
    return lambda x: reduce(lambda acc, f: f(acc), funcs, x)


def load_data(filepath: str, split_delimiter: str) -> list:
    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def parse_to_int(data: List[List[str]]) -> List[List[int]]:
    return [[int(j) for j in i] for i in data]


def transpose(data: List[list]) -> List[list]:
    return [list(i) for i in zip(*data)]


def split_strings(data: List[str], split_delimiter: str | None = None) -> list:
    return [i.split(split_delimiter) for i in data]


def sort_sublists(data: List[list]) -> List[list]:
    return [sorted(i) for i in data]


def zip_sublists(data: List[list]) -> List[list]:
    return list(zip(*data))
