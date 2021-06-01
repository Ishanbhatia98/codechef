from collections import Counter
for _ in range(int(input())):
    n, w, c = map(int, input().split())
    l = list(map(int, input().split()))
    w -= c
    t = 0
    c = Counter(l)
    for k, v in c.items():
        if v > 1:
            r = v//2
            t += (r*2*k)
        if t >= w:
            print('YES')
            break
    else:
        print('NO')
