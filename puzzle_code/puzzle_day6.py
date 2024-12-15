import multiprocessing


def get_data():
    x, y = 0, 0
    index_i, index_j = 0, 0
    mapa = []
    with open("../input/day6.txt", 'r') as file_var:
        for line in file_var:
            mapa.append(list(line.replace("\n", "")))
            if '^' in line:
                x = index_i
                for letter in line:
                    if letter == '^':
                        y = index_j
                    index_j = index_j + 1
            index_i = index_i + 1

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


# check if position is in bounds
def in_bounds(x, y, width, height):
    return x in range(width) and y in range(height)


# get list of unique visited positions
def get_visited(g_x, g_y, width, height, obs, dirs):
    current_x = g_x
    current_y = g_y
    turn = 0
    visited_pos = [[g_y, g_x]]  # list of visited coordinates
    while in_bounds(current_x, current_y, width, height):
        # next position based on direction vector cycle
        next_x = current_x + dirs[turn % 4][1]
        next_y = current_y + dirs[turn % 4][0]

        if in_bounds(next_x, next_y, width, height):
            if [next_y, next_x] in obs:
                turn = turn + 1  # turn right
            else:
                current_x = next_x  # move to next
                current_y = next_y
                if [current_y, current_x] not in visited_pos:
                    visited_pos.append([current_y, current_x])  # record as visited
        else:
            break

    return visited_pos


# check if making pos an obstacle causes loop
def check_loop(pos):
    test_obstacles = obstacles[:]
    test_obstacles.append(pos)

    current_x = guard_x
    current_y = guard_y
    turn = 0
    test_visited = [[guard_y, guard_x, turn % 4]]
    while in_bounds(current_x, current_y, facility_width, facility_height):
        # next position based on direction vector cycle
        next_x = current_x + directions[turn % 4][1]
        next_y = current_y + directions[turn % 4][0]

        if in_bounds(next_x, next_y, facility_width, facility_height):
            if [next_y, next_x] in test_obstacles:
                turn = turn + 1  # turn right
            else:
                current_x = next_x  # move to next
                current_y = next_y
                if [current_y, current_x, turn % 4] not in test_visited:
                    test_visited.append([current_y, current_x, turn % 4])
                else:
                    return True  # seen this position from same direction before
        else:
            break

    return False


# read input_data from file
with open("../input/day6.txt", "r") as file:
    input_data = [list(line.strip()) for line in file.readlines()]

facility_map = input_data
facility_width = len(facility_map[0])
facility_height = len(facility_map)

# identify coordinates of obstacles and the guard
obstacles = []
guard_x = None
guard_y = None
for i in range(facility_height):
    for j in range(facility_width):
        if input_data[i][j] == "#":
            obstacles.append([i, j])
        if input_data[i][j] == "^":
            guard_x = j
            guard_y = i

# cycle of turn vectors
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# build list of unique visited positions
visited = get_visited(guard_x, guard_y, facility_width, facility_height, obstacles, directions)


# check loop for each visited position minus the starting position
def guard_movement_loop():
    with multiprocessing.Pool(10) as pool:
        results = pool.map(check_loop, visited[1:])

    print(results.count(True))
