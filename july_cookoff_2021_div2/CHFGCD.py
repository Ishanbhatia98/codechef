from math import gcd
for _ in range(int(input())):
    x, y = map(int, input().split())
    if gcd(x, y) > 1:
        print(0)
    elif gcd(x+1, y) > 1 or gcd(x, y+1) > 1:
        print(1)
    else:
        print(2)
