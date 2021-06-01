from collections import defaultdict as dd
import sys
sys.setrecursionlimit(100000)


def f(y, i):
    if y == 0:
        return 0
    if y-x < 0:
        return float('inf')
    if d[y, i] != -1:
        return d[y, i]
    if y-(x*(2**i)) < 0:
        d[y, i] = 2+f(y-x, 1)
        return d[y, i]
    d[y, i] = 1+min(1+f(y-x, 1), f(y-(x*(2**i)), i+1))

    return d[y, i]


for _ in range(int(input())):
    x, y = map(int, input().split())
    d = dd(lambda: -1)
    z = f(y, 0)
    print(z if z != float('inf') else -1)
