for _ in range(int(input())):
    n, m = map(int, input().split())
    # 1-f, 0-c
    f = list(map(int, input().split()))
    c = list(map(int, input().split()))
    f = list(zip(f, [1]*len(f)))
    c = list(zip(c, [0]*len(c)))
    r = f+c
    r = sorted(r, key=lambda x: x[0])
    t = 0
    if r[0][1] == 0:
        t += 1
    for i in range(1, len(r)):
        t += r[i][1] != r[i-1][1]
    print(t)
