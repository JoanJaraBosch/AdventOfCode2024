from collections import defaultdict


def get_antennas(grid):
    antennas = defaultdict(list)

    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char != ".":
                antennas[char].append((row, col))

    return antennas


def on_grid(node, n_rows, n_cols):
    return 0 <= node[0] < n_rows and 0 <= node[1] < n_cols


def main():
    with open("input/day8.txt", "rt") as f:
        grid = [line.strip() for line in f]
        n_rows, n_cols = len(grid), len(grid[0])

    antennas = get_antennas(grid)
    antinodes_part1 = set()
    antinodes_part2 = set()

    for locations in antennas.values():
        if len(locations) == 1:
            continue

        for i1 in range(len(locations) - 1):
            loc1 = locations[i1]

            for i2 in range(i1 + 1, len(locations)):
                loc2 = locations[i2]
                row_diff, coll_diff = loc2[0] - loc1[0], loc2[1] - loc1[1]

                antinodes_part2.add(loc1)
                antinodes_part2.add(loc2)

                # move from loc1 until out of bounds
                antinode = (loc1[0] - row_diff, loc1[1] - coll_diff)
                if on_grid(antinode, n_rows, n_cols):
                    antinodes_part1.add(antinode)
                    while on_grid(
                            antinode := (antinode[0] - row_diff, antinode[1] - coll_diff),
                            n_rows,
                            n_cols,
                    ):
                        antinodes_part2.add(antinode)

                # move from loc2 until out of bounds
                antinode = (loc2[0] + row_diff, loc2[1] + coll_diff)
                if on_grid(antinode, n_rows, n_cols):
                    antinodes_part1.add(antinode)
                    while on_grid(
                            antinode := (antinode[0] + row_diff, antinode[1] + coll_diff),
                            n_rows,
                            n_cols,
                    ):
                        antinodes_part2.add(antinode)

    print("DAY 8 FIRST PART")
    print(len(antinodes_part1))
    print("DAY 8 SECOND PART")
    print(len(antinodes_part1 | antinodes_part2))
