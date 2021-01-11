from math import ceil

for _ in range(int(input())):
    n, d = map(int, input().split())
    l = list(map(int, input().split()))
    r, nr = 0, 0
    for i in l:
        if i>=80 or i<=9:
            r+=1
        else:
            nr+=1
    print(ceil(r/d)+ceil(nr/d))
