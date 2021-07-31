def check(i, j):
    b1 = b[i:]+b[:i]
    b2 = b[j:]+b[:j]

    for i in range(n):
        z1 = (a[i]+b1[i]) % n
        z2 = (a[i]+b2[i]) % n
        if z1 > z2:
            return j
        elif z2 > z1:
            return i
    return i


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [(a[0]+b[i]) % n for i in range(n)]
    m = min(c)
    r = []
    for i in range(n):
        if c[i] == m:
            r.append(i)

    if len(r) == 1:
        b = b[r[0]:]+b[:r[0]]
        for i in range(n):
            print((a[i]+b[i]) % n, end=' ')
    else:
        ans = -1
        x, y = r[0], r[1]
        bx = b[x:]+b[:x]
        by = b[y:]+b[:y]
        for i in range(n):
            zx = (a[i]+bx[i]) % n
            zy = (a[i]+by[i]) % n
            if zx > zy:
                ans = y
                break
            elif zy > zx:
                ans = x
                break
        assert(ans != -1)
        b = b[ans:]+b[:ans]
        for i in range(n):
            print((a[i]+b[i]) % n, end=' ')
