from functools import lru_cache

FILENAME = "../input/day19.txt"


def parse_input(filename):
    with open(filename) as input_file:
        patterns, designs = input_file.read().split("\n\n")
    return frozenset(patterns.split(", ")), designs.split()


def remove_prefix(prefix, word):
    return word[len(prefix) :]


@lru_cache(maxsize=None)
def check_design(design, patterns):
    if not design:
        return True
    return sum(
        check_design(remove_prefix(pattern, design), patterns)
        for pattern in patterns
        if design.startswith(pattern)
    )


def part1():
    patterns, designs = parse_input(FILENAME)
    return sum(check_design(design, patterns) > 0 for design in designs)


def part2():
    patterns, designs = parse_input(FILENAME)
    return sum(check_design(design, patterns) for design in designs)
