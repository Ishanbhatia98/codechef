n, h, x = map(int, input().split())
ts = list(map(int, input().split()))
f = 1
for t in ts:
    if t+x>=h:
        print('YES')
        f = 0
        break
if f:
    print('NO')
