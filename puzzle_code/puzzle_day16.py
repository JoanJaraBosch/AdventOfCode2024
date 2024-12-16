import heapq
from collections import defaultdict

data = open("../input/day16.txt").read()

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]


def traverse():
    walls = set()
    for y, line in enumerate(data.split()):
        for x, c in enumerate(line):
            match c:
                case '#': walls.add((y,x))
                case 'S': source = (y, x)
                case 'E': target = (y,x)

    q = [(0, source, 0)]
    seen = set()
    while q:
        cost, pos, d = heapq.heappop(q)
        if (pos, d) in seen:  continue
        if pos == target: return cost

        seen.add((pos,d))
        # add possible next moves to the queue
        forwards = (pos[0]+DIRS[d][0], pos[1]+DIRS[d][1])
        if forwards not in walls: heapq.heappush(q,(cost+1, forwards, d))
        heapq.heappush(q,(cost+1000, pos, (d+1)%4))
        heapq.heappush(q,(cost+1000, pos, (d-1)%4))
    print("Queue exhausted - end not found.")


def find_all_paths():
    target_cost = traverse()
    walls = set()
    for y, line in enumerate(data.split()):
        for x, c in enumerate(line):
            match c:
                case '#': walls.add((y,x))
                case 'S': source = (y, x)
                case 'E': target = (y,x)
    best_costs = {}
    links = defaultdict(set)

    q = [(0, source, 0, None)]
    while q:
        cost, pos, d, prev = heapq.heappop(q)
        if cost > target_cost:      # we know we can't find any more routes now
            break
        if (pos, d) in best_costs:  # if we've found a new good route, record it
            if cost == best_costs[(pos,d)]:
                links[(pos, d)].add(prev)
            continue
        # now we know we've got a new best cost
        best_costs[(pos,d)] = cost
        links[(pos,d)].add(prev)

        # add possible next moves to the queue
        prev = (pos, d)
        forwards = (pos[0]+DIRS[d][0], pos[1]+DIRS[d][1])
        if forwards not in walls: heapq.heappush(q,(cost+1, forwards, d, prev))
        heapq.heappush(q,(cost+1000, pos, (d+1)%4, prev))
        heapq.heappush(q,(cost+1000, pos, (d-1)%4, prev))

    # now walk backwards from the target, recording every tile visited.
    routes, tiles = set(), set()
    def walk(cur):
        if cur and cur not in routes:
            routes.add(cur)
            tiles.add(cur[0])
            for npos in links[cur]: walk(npos)
    for d in range(4): walk((target, d))
    return len(tiles)
