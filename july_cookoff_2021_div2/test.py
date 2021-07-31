
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = min(l)
    c = 0
    f = 1
    for i in l:
        if i != m and i-m-2 >= 0:
            c += 1
        else:
            f = 0
            break
    sol = c
    if not f:
        k = Counter(l)
        sol = n-k[0]
    print(sol)
