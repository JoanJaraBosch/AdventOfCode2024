from collections import defaultdict
from functools import reduce
from operator import mul
import re

import tqdm
from toolbox import load_as_str, getcwd, Vector


def parse_input(suffix: str) -> list[tuple[Vector, Vector]]:
    data = load_as_str(getcwd().joinpath(f"input/day14.txt"))
    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    initial_positions = re.findall(pattern, data)
    robots = []
    for x, y, vx, vy in initial_positions:
        robots.append((Vector(int(x), int(y)), Vector(int(vx), int(vy))))
    return robots


def update_positions(robots: list[tuple[Vector, Vector]],
                     iterations: int,
                     width: int,
                     height: int) -> list[tuple[Vector, Vector]]:
    new_positions = []
    for position, velocity in robots:
        end_position = position + velocity * iterations
        new_positions.append((Vector(end_position.x % width, end_position.y % height),
                              velocity))
    return new_positions


def positions_to_grid(positions: Vector,
                      width: int,
                      height: int) -> dict[tuple[int, int], int]:
    def getzero():
        return 0

    grid = defaultdict(getzero)
    for position in positions:
        grid[(position.y % height, position.x % width)] += 1

    return grid


def show_grid(grid: dict[tuple[int, int], int],
              width: int,
              height: int):
    for r in range(height):
        print(''.join(str(grid[(r, c)]) if grid[(r, c)] > 0 else '.' for c in range(width)))


def compute_score(positions: list[Vector],
                  width: int,
                  height: int):
    robots_per_quadrant = [0, 0, 0, 0]
    middle_x = width // 2
    middle_y = height // 2
    for position in positions:
        if position.x == middle_x or position.y == middle_y:
            continue
        if position.x < middle_x:
            if position.y < middle_y:
                robots_per_quadrant[0] += 1
            else:
                robots_per_quadrant[1] += 1
        else:
            if position.y < middle_y:
                robots_per_quadrant[2] += 1
            else:
                robots_per_quadrant[3] += 1
    print(robots_per_quadrant)
    return reduce(mul, robots_per_quadrant)


def main():
    width = 101
    height = 103
    # width = 11 # for test sample
    # height = 7
    robots = parse_input("")
    final_positions = update_positions(robots, 100, width, height)
    print(f"Part 1 answer: {compute_score([pos for pos, _ in final_positions], width, height)}")

    for i in tqdm.tqdm(range(100_000)):
        robots = update_positions(robots, 1, width, height)
        grid = positions_to_grid([pos for pos, _ in robots], width, height)

        if max(grid.values()) == 1:
            show_grid(grid, width, height)
            print(f"Part 2 answer: {i+1}")
            break
