from __future__ import annotations
import itertools
import pathlib
import re
from typing import Any, Callable, Sequence

_CWD = pathlib.Path(__file__).parent

def getcwd() -> pathlib.Path:
    return _CWD

"""
FILE I/O
"""
def load_as_table(fname: str | pathlib.Path, cast: Callable = int) -> list[list[Any]]:
    data = []
    with open(fname, 'r') as fp:
        data = fp.readlines()
    data = [[cast(v) for v in d.split()] for d in data]
    return data


def load_as_str(fname: str | pathlib.Path) -> str:
    with open(fname, 'r') as fp:
        data = fp.read()
    return data


def load_as_grid(fname: str | pathlib.Path, cast: Callable[[str], Any] = str) -> list[list[Any]]:
    data = []
    with open(fname, 'r') as fp:
        data = fp.readlines()
    return [[cast(c) for c in row.strip()] for row in data if len(row) != 0]


"""
REGEX
"""
def get_with_pattern(pattern: str, text: str, fn: Callable[[Sequence], Any]):
    results = []

    all_matches = re.findall(pattern, text) # returns matches as list or tuples

    for m in all_matches:
        results.append(fn(m))

    return results


def remove_with_pattern(pattern: str, text: str):
    """Remove everything inside a pattern"""

    while (match := re.search(pattern, text)) is not None:
        text = text[:match.start()] + text[match.end():]

    return text


"""" 
DATA MANIPULATION
"""

def transpose_data(data: list[list[int]]) -> list[list[int]]:
    # transpose from list of rows to list of columns
    return list(zip(*data))


def flatten(values: list[list[str]]) -> list[str]:
    return list(itertools.chain.from_iterable(values))


"""
Vectors
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        if type(other) is Vector:
            return Vector(self.x*other.x, self.y*other.y)

        return Vector(self.x*other, self.y*other)

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return (self.x, self.y).__hash__()
