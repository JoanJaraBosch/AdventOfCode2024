import re
import sys
import numpy as np
from heapq import heappop, heappush


def part1():
    with open('../input/day18.txt') as f:
        lines = f.readlines()

    coords = [[int(num) for num in re.findall(r'\d+', line)] for line in lines]

    gridsize = 71
    bytesfallen = 1024
    gridlines = []
    for i in range(gridsize):
        line = []
        for j in range(gridsize):
            line.append('.')
        gridlines.append(line)

    for coord in coords[:bytesfallen]:
        gridlines[coord[1]][coord[0]] = '#'

    grid = np.array(gridlines)
    start = [0,0]
    end = [gridsize-1,gridsize-1]

    q = [(0, start)]
    visited = {}
    min_cost = sys.maxsize

    while q:
        (cost, [y, x]) = heappop(q)

        if [y,x] == end:
            min_cost = min(min_cost, cost)
            break

        cost += 1

        if y <= gridsize-2 and grid[y+1, x] == '.' and ((y+1, x) not in visited or visited[(y+1, x)] > cost):
            visited[(y+1, x)] = cost
            heappush(q, (cost, [y+1, x]))
        if y >= 1 and grid[y-1, x] == '.' and ((y-1, x) not in visited or visited[(y-1, x)] > cost):
            visited[(y-1, x)] = cost
            heappush(q, (cost, [y-1, x]))
        if x <= gridsize-2 and grid[y, x+1] == '.' and ((y, x+1) not in visited or visited[(y, x+1)] > cost):
            visited[(y, x+1)] = cost
            heappush(q, (cost, [y, x+1]))
        if x >= 1 and grid[y, x-1] == '.' and ((y, x-1) not in visited or visited[(y, x-1)] > cost):
            visited[(y, x-1)] = cost
            heappush(q, (cost, [y, x-1]))

    return min_cost


def part2():
    with open('../input/day18.txt') as f:
        lines = f.readlines()

    coords = [[int(num) for num in re.findall(r'\d+', line)] for line in lines]

    gridsize = 71
    gridlines = []
    for i in range(gridsize):
        line = []
        for j in range(gridsize):
            line.append('.')
        gridlines.append(line)

    grid = np.array(gridlines)
    start = [0,0]
    end = [gridsize-1,gridsize-1]

    for coord in coords[:1024]:
        grid[coord[1],coord[0]] = '#'

    for coord in coords[1024:]:
        grid[coord[1],coord[0]] = '#'

        q = [(0, start)]
        visited = {}
        min_cost = sys.maxsize

        while q:
            (cost, [y, x]) = heappop(q)

            if [y,x] == end:
                min_cost = min(min_cost, cost)
                break

            cost += 1

            if y <= gridsize-2 and grid[y+1, x] == '.' and ((y+1, x) not in visited or visited[(y+1, x)] > cost):
                visited[(y+1, x)] = cost
                heappush(q, (cost, [y+1, x]))
            if y >= 1 and grid[y-1, x] == '.' and ((y-1, x) not in visited or visited[(y-1, x)] > cost):
                visited[(y-1, x)] = cost
                heappush(q, (cost, [y-1, x]))
            if x <= gridsize-2 and grid[y, x+1] == '.' and ((y, x+1) not in visited or visited[(y, x+1)] > cost):
                visited[(y, x+1)] = cost
                heappush(q, (cost, [y, x+1]))
            if x >= 1 and grid[y, x-1] == '.' and ((y, x-1) not in visited or visited[(y, x-1)] > cost):
                visited[(y, x-1)] = cost
                heappush(q, (cost, [y, x-1]))

        if min_cost == sys.maxsize:
            print(','.join(map(str,coord)))
            break

    return min_cost

