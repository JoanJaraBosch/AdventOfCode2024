def get_data():
    f = open("input/day1.txt", "r")
    first_list = []
    second_list = []
    for x in f:
        first_list.append(x.split("   ")[0])
        second_list.append(x.split("   ")[1].replace("\n", ""))

    first_list.sort()
    second_list.sort()

    return first_list, second_list


def distances():
    x, y = get_data()
    distance = 0
    i = 0
    while i < len(x):
        distance = distance + abs(int(x[i]) - int(y[i]))
        i = i + 1
    return distance


def similarity():
    x, y = get_data()
    similar = 0
    i = 0
    while i < len(x):
        similar = similar + int(x[i]) * y.count(x[i])
        i = i + 1
    return similar
