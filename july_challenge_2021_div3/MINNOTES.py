from math import gcd
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if n == 1:
        print(1)
    else:
        gl = [0 for _ in range(n)]
        gr = [0 for _ in range(n)]
        for i in range(1, n):
            gl[i] = gcd(l[i-1], gl[i-1])
        for i in range(n-2, -1, -1):
            gr[i] = gcd(l[i+1], gr[i+1])

        m = [gcd(gl[i], gr[i]) for i in range(n)]
        mx = max(m)
        r = []
        for i in range(n):
            if m[i] == mx:
                r.append((i, l[i]))

        r = sorted(r, reverse=True, key=lambda x: x[1])
        k = r[0][0]
        v = m[k]
        t = 1
        for i in range(n):
            if i != k:
                t += l[i]//v
        print(t)
