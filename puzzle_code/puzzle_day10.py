mapa: [[int]] = []

with open('../input/day10.txt', 'r') as file:
    for line in file:
        map_row = []
        for char in line.strip():
            map_row.append(int(char))
        mapa.append(map_row)


def solve_part1():
    def walk_trail(cord_x: int, cord_y: int, end_position: set[tuple[int, int]]):
        height = mapa[cord_y][cord_x]
        if height == 9:
            end_position.add((cord_x, cord_y))
            return

        # left
        if cord_x > 0 and mapa[cord_y][cord_x - 1] == height + 1:
            walk_trail(cord_x - 1, cord_y, end_position)
        # up
        if cord_y > 0 and mapa[cord_y - 1][cord_x] == height + 1:
            walk_trail(cord_x, cord_y - 1, end_position)
        # right
        if cord_x < len(mapa[cord_y]) - 1 and mapa[cord_y][cord_x + 1] == height + 1:
            walk_trail(cord_x + 1, cord_y, end_position)
        # down
        if cord_y < len(mapa) - 1 and mapa[cord_y + 1][cord_x] == height + 1:
            walk_trail(cord_x, cord_y + 1, end_position)

    total_score = 0
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            if mapa[y][x] == 0:
                end_positions = set()
                walk_trail(x, y, end_positions)
                total_score += len(end_positions)

    print('Sum of scores for all trailheads (part 1):', total_score)


def solve_part2():
    def walk_trail(cord_x, cord_y) -> int:
        height = mapa[cord_y][cord_x]
        if height == 9:
            return 1

        score = 0
        # left
        if cord_x > 0 and mapa[cord_y][cord_x - 1] == height + 1:
            score += walk_trail(cord_x - 1, cord_y)
        # up
        if cord_y > 0 and mapa[cord_y - 1][cord_x] == height + 1:
            score += walk_trail(cord_x, cord_y - 1)
        # right
        if cord_x < len(mapa[cord_y]) - 1 and mapa[cord_y][cord_x + 1] == height + 1:
            score += walk_trail(cord_x + 1, cord_y)
        # down
        if cord_y < len(mapa) - 1 and mapa[cord_y + 1][cord_x] == height + 1:
            score += walk_trail(cord_x, cord_y + 1)
        return score

    total_score = 0
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            if mapa[y][x] == 0:
                total_score += walk_trail(x, y)

    print('Sum of ratings for all trailheads (part 2):', total_score)
