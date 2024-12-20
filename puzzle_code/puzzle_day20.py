from collections import Counter


def get_data(input_file):
    return [line.strip() for line in input_file]


def get_times(grid):
    end = next((row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == "E")

    times: list[list[int | None]] = [[None for cell in line] for line in grid]
    times[end[0]][end[1]] = 0
    time, to_visit = 0, [end]
    while to_visit:
        time += 1
        to_visit_ = []
        for row, col in to_visit:
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row_, col_ = row + dr, col + dc
                if times[row_][col_] is None and grid[row_][col_] != "#":
                    times[row_][col_] = time
                    to_visit_.append((row_, col_))
        to_visit = to_visit_

    # print()
    # print('\n'.join(''.join('#' if cell is None else str(cell % 10) for cell in line) for line in times))

    return times


def count_cheats(grid, max_cheat_time):
    m, n = len(grid), len(grid[0])
    times = get_times(grid)

    cheats_directions = {(dr, dc): dr + dc for dr in range(max_cheat_time + 1) for dc in range(max_cheat_time + 1 - dr)}
    cheats_directions |= {(dr, -dc): time for (dr, dc), time in cheats_directions.items()}
    cheats_directions |= {(-dr, dc): time for (dr, dc), time in cheats_directions.items()}

    start = next((row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == "S")
    cheats = Counter()
    visited = [[cell == "#" for cell in line] for line in grid]
    visited[start[0]][start[1]] = True
    time, to_visit = 0, [start]
    total_time = times[start[0]][start[1]]
    while to_visit:
        to_visit_ = []
        for row, col in to_visit:
            # Check for cheats
            for (dr, dc), cheat_time in cheats_directions.items():
                row_, col_ = row + dr, col + dc
                if (
                        0 <= row_ < m
                        and 0 <= col_ < n
                        and (time_ := times[row_][col_]) is not None
                        and (new_time := time + cheat_time + time_) < total_time
                ):
                    cheats[total_time - new_time] += 1
            # Continue on path
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row_, col_ = row + dr, col + dc
                if not visited[row_][col_] and grid[row_][col_] != "#":
                    visited[row_][col_] = True
                    to_visit_.append((row_, col_))

        time += 1
        to_visit = to_visit_

    # for time, count in sorted(cheats.items()):
    #    print(time, count)

    return cheats


def part1():
    with open("../input/day20.txt") as input_file:
        grid = get_data(input_file)
    max_cheat_time=2
    minimal_cheat=100
    cheats = count_cheats(grid, max_cheat_time)
    return sum(count for time, count in cheats.items() if time >= minimal_cheat)


def part2():
    with open("../input/day20.txt") as input_file:
        grid = get_data(input_file)
    max_cheat_time=20
    minimal_cheat=100
    cheats = count_cheats(grid, max_cheat_time)
    return sum(count for time, count in cheats.items() if time >= minimal_cheat)
