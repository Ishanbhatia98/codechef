from collections import Counter

def f(n, c):
    if n==0:
        return 1
    if t[n][c]!=-1:
        return t[n][c]
    if c<k:
        t[n][c] = cn[l[n-1]]+f(n-1, c+1)+f(n-1, c)
        return t[n][c]
    t[n][c] = f(n-1, c)
    return t[n][c]

n, k = map(int, input().split())

#1007->number of prime numbers between 2 and 8000(from constraint)
k = min(k, 1007)

l = list(map(int, input().split()))
cn = Counter(l)
l = list(cn.keys())
n = len(l)
t = [[-1 for _ in range(k+1)] for _ in range(n+1)]

ans = f(n, 0)-n

print(ans%(10**9 +7))
