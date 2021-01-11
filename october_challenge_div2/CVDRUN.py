for _ in range(int(input())):
    n, k, x, y = map(int, input().split())
    s = set()
    while True:
        if x in s:
            break
        s.add(x)
        x = (x+k)%n
    if y in s:
        print('YES')
    else:
        print('NO')
