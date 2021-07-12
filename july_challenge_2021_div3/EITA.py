for _ in range(int(input())):
    d, x, y, z = map(int, input().split())
    print(max(7*x, y*d+z*(7-d)))
