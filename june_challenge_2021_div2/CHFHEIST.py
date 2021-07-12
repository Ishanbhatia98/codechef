for _ in range(int(input())):
    D, d, p, q = map(int, input().split())
    r = p
    t = 0
    for i in range(1, D+1):

        t += r
        if i % d == 0:
            r += q
    print(t)
