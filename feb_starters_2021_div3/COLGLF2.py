for _ in range(int(input())):
    n = int(input())
    q = list(map(int, input().split()))
    t = []
    for _ in range(n):
        l = list(map(int, input().split()))
        t.append(l[1:])

    total = 0
    for i in range(n):
        total+=t[i][0]
        for j in range(1, len(t[i])):
            total+=t[i][j]-q[i]
    print(total)
