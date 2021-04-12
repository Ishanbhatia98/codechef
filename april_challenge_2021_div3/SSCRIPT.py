
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    cm, gm = 0, 0
    f = 1
    for i in range(n):
        if s[i] == '*':
            cm += 1
            gm = max(cm, gm)
        else:
            cm = 0
        if gm >= k:
            print('YES')
            f = 0
            break
    if f:
        print('NO')
