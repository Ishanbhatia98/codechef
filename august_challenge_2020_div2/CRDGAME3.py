from math import ceil

for _ in range(int(input())):
    c, r = map(int, input().split())
    cn = ceil(c/9)
    rn = ceil(r/9)
    if cn<rn:
        print(0, cn)
    else:
        print(1, rn)
