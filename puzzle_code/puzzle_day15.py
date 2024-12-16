def get_data(part):
    mapa = []
    directions = ""

    if part == 1:
        with open("../input/test_day15.txt", "r") as file:
            for line in file:
                mapa.append(list(line.replace("\n", "").strip()))
    else:
        with open("../input/test_day15.txt", "r") as file:
            for line in file:
                aux = []
                for value in list(line.replace("\n", "").strip()):
                    if value == "#":
                        aux.append("#")
                        aux.append("#")
                    elif value == "O":
                        aux.append("[")
                        aux.append("]")
                    elif value == "@":
                        aux.append("@")
                        aux.append(".")
                    elif value == ".":
                        aux.append(".")
                        aux.append(".")
                mapa.append(aux)

    with open("../input/test_day15directions.txt", "r") as file:
        for line in file:
            directions = directions + line.replace("\n", "").strip()

    return mapa, list(directions)


def pos_initial_robot(mapa):
    i = 0
    while i < len(mapa):
        j=0
        while j < len(mapa[i]):
            if mapa[i][j] == "@":
                return i,j
            j = j + 1
        i = i + 1


def part1_movement(mapa, directions, cord_x, cord_y):
    for direction in directions:
        if direction == ">":
            if cord_y+1 < len(mapa[cord_x]) -1:
                if mapa[cord_x][cord_y+1] == ".":
                    mapa[cord_x][cord_y] = "."
                    mapa[cord_x][cord_y+1] = "@"
                    cord_y = cord_y + 1
                elif mapa[cord_x][cord_y+1] == "O":
                    k = 1
                    while cord_y+k < len(mapa[cord_x]) -1 and mapa[cord_x][cord_y+k] == "O":
                        k = k + 1

                    if mapa[cord_x][cord_y+k] == ".":
                        while k > 0:
                            mapa[cord_x][cord_y+k] = mapa[cord_x][cord_y+k-1]
                            k = k - 1
                        mapa[cord_x][cord_y] = "."
                        cord_y = cord_y + 1
        elif direction == "^":
            if cord_x-1 > 0:
                if mapa[cord_x-1][cord_y] == ".":
                    mapa[cord_x][cord_y] = "."
                    mapa[cord_x-1][cord_y] = "@"
                    cord_x = cord_x - 1
                elif mapa[cord_x-1][cord_y] == "O":
                    k = 1
                    while cord_x-k > 0 and mapa[cord_x-k][cord_y] == "O":
                        k = k + 1

                    if mapa[cord_x-k][cord_y] == ".":
                        while k > 0:
                            mapa[cord_x-k][cord_y] = mapa[cord_x-k+1][cord_y]
                            k = k - 1
                        mapa[cord_x][cord_y] = "."
                        cord_x = cord_x - 1
        elif direction == "v":
            if cord_x+1 < len(mapa)-1:
                k = 1
                while cord_x+k < len(mapa) -1 and mapa[cord_x+k][cord_y] == "O":
                    k = k + 1

                if mapa[cord_x+k][cord_y] == ".":
                    while k > 0:
                        mapa[cord_x+k][cord_y] = mapa[cord_x+k-1][cord_y]
                        k = k - 1
                    mapa[cord_x][cord_y] = "."
                    cord_x = cord_x + 1
        elif direction == "<":
            if cord_y-1 > 0:
                if mapa[cord_x][cord_y-1] == ".":
                    mapa[cord_x][cord_y] = "."
                    mapa[cord_x][cord_y-1] = "@"
                    cord_y = cord_y - 1
                elif mapa[cord_x][cord_y-1] == "O":
                    k = 1
                    while cord_y-k > 0 and mapa[cord_x][cord_y-k] == "O":
                        k = k + 1

                    if mapa[cord_x][cord_y-k] == ".":
                        while k > 0:
                            mapa[cord_x][cord_y-k] = mapa[cord_x][cord_y-k+1]
                            k = k - 1
                        mapa[cord_x][cord_y] = "."
                        cord_y = cord_y - 1
    return mapa


def part2_movement():
    warehouse, moves = open("../input/day15.txt").read().split('\n\n')
    warehouse, robot = [[('[' if i % 2 == 0 else ']') if line[i // 2] == 'O' else line[i // 2] for i in range(len(line) * 2)] for line in warehouse.split()], warehouse.index('@')
    x, y, directions = robot % (len(warehouse[0]) // 2), robot // (len(warehouse[0]) // 2), {'>': 1, '<': -1, '^': -1, 'v': 1}
    warehouse[y][x], warehouse[y][x + 1] = '.', '.'
    for move in ''.join(moves.split()):
        if move in ['>', '<']:
            x1 = x + (directions[move])
            while warehouse[y][x1] in ['[', ']']: x1 += directions[move]
            if warehouse[y][x1] == '.':
                for x2 in range(x1, x, -directions[move]): warehouse[y][x2] = warehouse[y][x2 - directions[move]]
                x += directions[move]
        else:
            boxes = [{(x, y)}]
            while boxes[-1]:
                boxes.append(set())
                for box in boxes[-2]:
                    if warehouse[box[1] + directions[move]][box[0]] == '#': break
                    if warehouse[box[1] + directions[move]][box[0]] == '[': boxes[-1] |= {(box[0], box[1] + directions[move]), (box[0] + 1, box[1] + directions[move])}
                    elif warehouse[box[1] + directions[move]][box[0]] == ']': boxes[-1] |= {(box[0], box[1] + directions[move]), (box[0] - 1, box[1] + directions[move])}
                else: continue
                break
            else:
                for row in list(reversed(boxes)):
                    for box in row: warehouse[box[1] + directions[move]][box[0]], warehouse[box[1]][box[0]] = warehouse[box[1]][box[0]], '.'
                y += directions[move]
    return sum([100 * i + j for i, line in enumerate(warehouse) for j, c in enumerate(line) if c == '['])


def robot_movement(part):
    mapa, directions = get_data(part)
    cord_x, cord_y = pos_initial_robot(mapa)
    if part == 1:
        mapa = part1_movement(mapa, directions, cord_x, cord_y)
    else:
        return part2_movement()
    return count_distances(mapa, part)


def print_mapa(mapa):
    cadena = ""
    for i in mapa:
        for j in i:
            cadena = cadena+j
        cadena = cadena+"\n"
    print(cadena)


def count_distances(mapa, part):
    distances = 0
    i = 0
    if part == 1:
        while i < len(mapa):
            j = 0
            while j < len(mapa[i]):
                if mapa[i][j] == "O":
                    distances = distances + (i*100 + j)
                j = j + 1
            i = i + 1
    else:
        while i < len(mapa):
            j = 0
            while j < len(mapa[i]):
                if mapa[i][j] == "[":
                    distances = distances + (i*100 + j)
                j = j + 1
            i = i + 1
    return distances
