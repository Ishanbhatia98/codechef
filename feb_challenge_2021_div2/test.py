from collections import defaultdict as dd


def mex(arr):
    if diff == 1:
        for i in range(min(arr), max(arr)+1):
            if i not in arr:
                return i+1
    return min(arr)+1


for _ in range(int(input())):
    n, q, m = map(int, input().split())
    l = list(map(int, input().split()))
    diff = l[0]
    Q = []
    G = 0
    d = dd(lambda: 0)
    for _ in range(q):
        le, ri = map(int, input().split())
        c = 0
        for g in range(1, m+1):
            d[g] += (g % mex(l[le-1:ri])) != 0

    print(max(d[g] for g in range(1, m+1)))
