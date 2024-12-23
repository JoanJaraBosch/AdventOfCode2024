import numpy as np


def day22():
    nums = [int(x) for x in open('../input/day22.txt').read().split('\n')]
    m = 16777216
    repeats = 2000
    total = 0
    memos = {}
    for x in nums:
        seq = np.zeros(repeats + 1, dtype = int)
        seq[0] = x % 10
        for j in range(1, repeats + 1):
            x = (x ^ (x * 64)) % m
            x = (x ^ (x // 32)) % m
            x = (x ^ (x * 2048)) % m
            seq[j] =  x % 10
        total += x
        diffs = np.diff(seq)
        seen = set()
        for p in range(4,len(diffs)):
            h = tuple(diffs[p-3:p+1])
            if h not in memos and h not in seen:
                memos[h] = seq[p + 1]
            elif h not in seen:
                memos[h] += seq[p + 1]
            seen.add(h)
    print('Part 1:', total)
    print('Part 2: ', max(memos.values()))
