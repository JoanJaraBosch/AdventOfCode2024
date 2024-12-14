def get_data(test):
    if test == 0:
        with open("input/day9.txt", "r") as f:
            memoria = f.readline().replace("\n", "").strip()
    else:
        with open("input/test_day9.txt", "rt") as f:
            memoria = f.readline().replace("\n", "").strip()
    return memoria


def create_map():
    mapa = []
    memoria = get_data(0)
    cont = 0
    free_space = False
    for mem in memoria:
        if not free_space:
            free_space = True
            for i in range(0, int(mem)):
                mapa.append(str(cont))
            cont = cont + 1
        else:
            free_space = False
            if int(mem) != 0:
                for i in range(0, int(mem)):
                    mapa.append(".")
    return mapa


def order_map(part):
    mapa = create_map()
    if part == 1:
        i = 0
        j = len(mapa) - 1
        while i < j:
            while i < len(mapa) and mapa[i] != "." and i < j:
                i = i + 1

            while j > -1 and mapa[j] == "." and i < j:
                j = j - 1

            if i < len(mapa) and j > -1 and i < j:
                mapa[i] = mapa[j]
                mapa[j] = "."
                i = i + 1
                j = j - 1
    else:
        i = 0
        j = len(mapa) - 1

        while j > -1 and j > i:
            while j > - 1 and j > i and mapa[j] == ".":
                j = j - 1

            num_cont = 0
            while j-num_cont > - 1 and j-num_cont > i and mapa[j-num_cont] == mapa[j]:
                num_cont = num_cont + 1

            if num_cont != 0:
                movement = False

                while i < j and not movement:
                    while i < len(mapa) and j > i and mapa[i] != ".":
                        i = i + 1

                    point_cont = 0
                    while i + point_cont < len(mapa) and j > i + point_cont and mapa[i+point_cont] == ".":
                        point_cont = point_cont + 1

                    if point_cont >= num_cont:
                        movement = True
                        while num_cont > 0:
                            mapa[i] = mapa[j]
                            mapa[j] = "."
                            i = i + 1
                            j = j - 1
                            num_cont = num_cont - 1
                    else:
                        i = i + point_cont
            j = j - num_cont
            i = 0
    return calculate_checksum(mapa)


def calculate_checksum(mapa):
    checksum = 0
    for i, block in enumerate(mapa):
        if block != ".":
            checksum = checksum + (int(block) * i)
    return checksum
