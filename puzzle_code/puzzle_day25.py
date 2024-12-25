def solver():
    file = open('../input/day25.txt', 'r')
    lines = file.read().splitlines()

    d = []
    g = set()
    y0 = 0
    for y,line in enumerate(lines):
        if not line:
            d.append(g)
            g = set()
            y0 = y+1
        else:
            for x,c in enumerate(line):
                if c=="#":
                    g.add((x,y-y0))
    d.append(g)

    count = 0
    for i,x in enumerate(d[:-1]):
        for j,y in enumerate(d[i+1:]):
            if not x.intersection(y):
                count+=1
    return  count