for _ in range(int(input())):
    x, r, m = map(int, input().split())
    r, m = r*60, m*60
    if r <= x:
        print('YES')
    elif x+2*(r-x) <= m:
        print('YES')
    else:
        print('NO')
