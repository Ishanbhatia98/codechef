for _ in range(int(input())):
    d, c = map(int, input().split())
    a = sum(list(map(int, input().split())))
    b = sum(list(map(int, input().split())))
    t = a+b+d+d
    tp = t+c
    if a>=150:
        tp-=d
    if b>=150:
        tp-=d
    if tp<t:
        print('YES')
    else:
        print('NO')
