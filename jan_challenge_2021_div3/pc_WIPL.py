#partially correct 30/100 pts

from collections import defaultdict
def f(a, b, n):
    if n<0:
        return 10**9
    if a>=k and b>=k:
        return 0
    if d[(a, b, n)]!=-1:
        return d[(a, b, n)]

    if a>=k and b<k:
        d[(a, b, n)] = min(1+f(a, b+l[n-1], n-1), f(a, b, n-1))
        return d[(a, b, n)]
    if a<k and b>=k:
        d[(a, b, n)] = min(1+f(a+l[n-1], b, n-1), f(a, b, n-1))
        return d[(a, b, n)]
    if a<k and b<k:
        d[(a, b, n)] = min(1+f(a+l[n-1], b, n-1), 1+f(a, b+l[n-1], n-1), f(a, b, n-1))
        return d[(a, b, n)]
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    d = defaultdict(lambda :-1)
    ans = f(0, 0, n)
    if ans>n:
        print(-1)
    else:
        print(ans)

