from collections import defaultdict as dd
import sys
sys.setrecursionlimit(10000)

'''
def f(x, y):
    if x < x1 or y < y1:
        return 0
    if d[x, y] != -1:
        return d[x, y]
    d[x, y] = dp[x][y]+max(f(x-1, y), f(x, y-1))
    return d[x, y]

'''


def f(x, y):
    if x == x1 and y == y1:
        return 0
    if y == y1:
        return dp[x][y]+f(x-1, y)
    return dp[x][y]+f(x, y-1)


dp = [[0 for _ in range(1001)] for _ in range(1001)]
t, d = 1, 1
for r in range(1001):
    dp[r][0] = t
    d += 1
    t += d

for r in range(1001):
    for c in range(1, 1001):
        dp[r][c] += dp[r][c-1]+r+c


for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    d = dd(lambda: -1)
    print(f(x2, y2)+dp[x1][y1])
