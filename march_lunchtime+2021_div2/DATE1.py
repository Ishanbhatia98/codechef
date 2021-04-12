for _ in range(int(input())):
    a, y, x = map(int, input().split())
    if a >= y:
        print(x*y)
    else:
        print(1+a*x)
