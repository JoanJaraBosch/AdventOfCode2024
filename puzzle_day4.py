def get_data():
    matrix = []
    with open("input/day4.txt", 'r') as file:
        for line in file:
            lining = []
            for letter in line.replace("\n", ""):
                lining.append(letter)
            matrix.append(lining)
    return matrix


def count_xmas():
    xmas = get_data()
    cont, i = 0, 0
    while i < len(xmas):
        j = 0
        while j < len(xmas[i]):
            if xmas[i][j] == 'X':
                # Look right
                if i + 1 < len(xmas) and xmas[i + 1][j] == 'M':
                    if i + 2 < len(xmas) and xmas[i + 2][j] == 'A':
                        if i + 3 < len(xmas) and xmas[i + 3][j] == 'S':
                            cont = cont + 1
                # Look left
                if i - 1 > -1 and xmas[i - 1][j] == 'M':
                    if i - 2 > -1 and xmas[i - 2][j] == 'A':
                        if i - 3 > -1 and xmas[i - 3][j] == 'S':
                            cont = cont + 1
                # Look Up
                if j + 1 < len(xmas[i]) and xmas[i][j + 1] == 'M':
                    if j + 2 < len(xmas[i]) and xmas[i][j + 2] == 'A':
                        if j + 3 < len(xmas[i]) and xmas[i][j + 3] == 'S':
                            cont = cont + 1
                # Look down
                if j - 1 > -1 and xmas[i][j - 1] == 'M':
                    if j - 2 > -1 and xmas[i][j - 2] == 'A':
                        if j - 3 > -1 and xmas[i][j - 3] == 'S':
                            cont = cont + 1
                # Look left-up
                if i - 1 > -1 and j - 1 > -1 and xmas[i - 1][j - 1] == 'M':
                    if i - 2 > -1 and j - 2 > -1 and xmas[i - 2][j - 2] == 'A':
                        if i - 3 > -1 and j - 3 > -1 and xmas[i - 3][j - 3] == 'S':
                            cont = cont + 1
                # Look right-down
                if i + 1 < len(xmas) and j + 1 < len(xmas[i]) and xmas[i + 1][j + 1] == 'M':
                    if i + 2 < len(xmas) and j + 2 < len(xmas[i]) and xmas[i + 2][j + 2] == 'A':
                        if i + 3 < len(xmas) and j + 3 < len(xmas[i]) and xmas[i + 3][j + 3] == 'S':
                            cont = cont + 1
                # Look left down
                if i - 1 > -1 and j + 1 < len(xmas[i]) and xmas[i - 1][j + 1] == 'M':
                    if i - 2 > -1 and j + 2 < len(xmas[i]) and xmas[i - 2][j + 2] == 'A':
                        if i - 3 > -1 and j + 3 < len(xmas[i]) and xmas[i - 3][j + 3] == 'S':
                            cont = cont + 1
                # Look right-up
                if i + 1 < len(xmas) and j - 1 > -1 and xmas[i + 1][j - 1] == 'M':
                    if i + 2 < len(xmas) and j - 2 > -1 and xmas[i + 2][j - 2] == 'A':
                        if i + 3 < len(xmas) and j - 3 > -1 and xmas[i + 3][j - 3] == 'S':
                            cont = cont + 1

            j = j + 1
        i = i + 1
    return cont


def count_mas():
    xmas = get_data()
    cont, i = 0, 0
    while i < len(xmas):
        j = 0
        while j < len(xmas[i]):
            if xmas[i][j] == 'A':
                if i - 1 > -1 and j - 1 > -1 and xmas[i - 1][j - 1] == 'M':
                    if i + 1 < len(xmas) and j + 1 < len(xmas[i]) and xmas[i + 1][j + 1] == 'S':
                        if i - 1 > -1 and j + 1 < len(xmas[i]) and xmas[i - 1][j + 1] == 'M':
                            if i + 1 < len(xmas) and j - 1 > -1 and xmas[i + 1][j - 1] == 'S':
                                cont = cont + 1
                        elif i - 1 > -1 and j + 1 < len(xmas[i]) and xmas[i - 1][j + 1] == 'S':
                            if i + 1 < len(xmas) and j - 1 > -1 and xmas[i + 1][j - 1] == 'M':
                                cont = cont + 1
                elif i - 1 > -1 and j - 1 > -1 and xmas[i - 1][j - 1] == 'S':
                    if i + 1 < len(xmas) and j + 1 < len(xmas[i]) and xmas[i + 1][j + 1] == 'M':
                        if i - 1 > -1 and j + 1 < len(xmas[i]) and xmas[i - 1][j + 1] == 'M':
                            if i + 1 < len(xmas) and j - 1 > -1 and xmas[i + 1][j - 1] == 'S':
                                cont = cont + 1
                        elif i - 1 > -1 and j + 1 < len(xmas[i]) and xmas[i - 1][j + 1] == 'S':
                            if i + 1 < len(xmas) and j - 1 > -1 and xmas[i + 1][j - 1] == 'M':
                                cont = cont + 1
            j = j + 1
        i = i + 1
    return cont
