with open('input/day6.txt', 'r') as f:
    data = f.read()

grid_list = [[position for position in element] for element in data.split("\n")]

grid = {(x, y): grid_list[y][x] for y in range(len(grid_list)) for x in range(len(grid_list[0]))}

GRID_WIDTH, GRID_HEIGHT = (len(grid_list[0]), len(grid_list))

# directions
DIRECTIONS = {'^': (0, -1),
              '>': (1, 0),
              'v': (0, 1),
              '<': (-1, 0)}

NEXT_DIRECTIONS = {'^': '>',
                   '>': 'v',
                   'v': '<',
                   '<': '^'}

BLOCKAGE = '#'

# find START_POSITION
START_POSITION = None
START_DIRECTION = '^'

for y, row in enumerate(grid_list):
    if not START_POSITION:
        for x, position in enumerate(row):
            if position == '^':
                START_POSITION = (x, y)
                break


def get_data():
    x, y = 0, 0
    i, j = 0, 0
    mapa = []
    with open("input/day6.txt", 'r') as file:
        for line in file:
            mapa.append(list(line.replace("\n", "")))
            if '^' in line:
                x = i
                for letter in line:
                    if letter == '^':
                        y = j
                    j = j + 1
            i = i + 1

    return mapa, x, y


def guard_movement():
    mapa, x, y = get_data()
    direction = '^'
    count = 0
    mapa[x][y] = '.'
    while True:
        if direction == '^':
            x = x - 1
            if x == -1:
                return count
            elif mapa[x][y] == '.':
                count = count + 1
                mapa[x][y] = 'X'
            elif mapa[x][y] == '#':
                x = x + 1
                direction = '>'
        elif direction == '>':
            y = y + 1
            if y == len(mapa[x]):
                return count
            elif mapa[x][y] == '.':
                count = count + 1
                mapa[x][y] = 'X'
            elif mapa[x][y] == '#':
                y = y - 1
                direction = 'v'
        elif direction == 'v':
            x = x + 1
            if x == len(mapa[x]):
                return count
            elif mapa[x][y] == '.':
                count = count + 1
                mapa[x][y] = 'X'
            elif mapa[x][y] == '#':
                x = x - 1
                direction = '<'
        else:
            y = y - 1
            if y == -1:
                return count
            elif mapa[x][y] == '.':
                count = count + 1
                mapa[x][y] = 'X'
            elif mapa[x][y] == '#':
                y = y + 1
                direction = '^'


def loops_found(grid=grid, start_position=START_POSITION, start_direction=START_DIRECTION):
    num_of_possible_loops = 0
    for position in grid.keys():
        steps_taken = set()
        current_position = start_position
        current_direction = start_direction
        while True:
            x_current, y_current = current_position
            x_direction, y_direction = DIRECTIONS[current_direction]
            next_position = (x_current + x_direction, y_current + y_direction)
            x_next, y_next = next_position

            if x_next < 0 or x_next > GRID_WIDTH - 1 or y_next < 0 or y_next > GRID_HEIGHT - 1:  # break out of loop if out of grid bounds
                break

            if grid[(x_next, y_next)] == BLOCKAGE or next_position == position:  # change direction if real or theoretical blockage is hit
                current_direction = NEXT_DIRECTIONS[current_direction]
                continue

            current_position = next_position  # take a step
            step_key = (next_position, current_direction)

            if step_key in steps_taken:  # loop found
                num_of_possible_loops += 1
                break

            steps_taken.add(step_key)
    return num_of_possible_loops
