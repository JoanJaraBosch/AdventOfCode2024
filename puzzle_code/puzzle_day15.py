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


def part2_movement(mapa, directions, cord_x, cord_y):
    print_mapa(mapa)
    return mapa


def robot_movement(part):
    mapa, directions = get_data(part)
    cord_x, cord_y = pos_initial_robot(mapa)
    if part == 1:
        mapa = part1_movement(mapa, directions, cord_x, cord_y)
    else:
        mapa = part2_movement(mapa, directions, cord_x, cord_y)
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
