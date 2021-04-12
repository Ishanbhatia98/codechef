for _ in range(int(input())):
    a, b, c, v = map(float, input().split())
    if round(100/(a*b*c*v), 2) < 9.58:
        print('YES')
    else:
        print('NO')
