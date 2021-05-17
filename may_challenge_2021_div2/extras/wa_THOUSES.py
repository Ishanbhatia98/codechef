from collections import defaultdict as dd
import sys
sys.setrecursionlimit(10**9)
m = 10**9 + 7


def count(u):
    if len(d[u]) == 1:
        return 0
    t = 0
    for i in d[u]:
        t += 1+count(i)
    return t


def f(u, x):
    if len(d[u]) == 0:
        return 0

    r = sorted(d[u], key=lambda y: count(y), reverse=True)
    t, c = 0, 1
    for i in r:
        t += c*x+f(i, c*x) % m
        c += 1
    return t % m


for _ in range(int(input())):
    n, x = map(int, input().split())
    d = dd(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        d[u].append(v)

    print((f(1, x)+x) % m)
