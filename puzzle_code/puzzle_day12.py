data = open("../input/day12.txt").read().splitlines()

G = {i + j * 1j: e for i, row in enumerate(data)
     for j, e in enumerate(row)}

dirs, viz = (1, -1, 1j, -1j), set()


def dfs(p, e, region, fence, dr=None):
    if p in viz and G.get(p) == e: return
    if G.get(p) != e: return fence.add((p, dr))
    viz.add(p), region.add(p)
    for dr in dirs: dfs(p + dr, e, region, fence, dr)
    neighbors = {(p + dr * 1j, dr) for p, dr in fence}
    return len(region), len(fence), len(fence - neighbors)


def solution():
    regions = ([dfs(p, e, set(), set())
                for p, e in G.items() if p not in viz])

    return sum(area * perimeter for area, perimeter, _ in regions), sum(area * sides for area, _, sides in regions)
