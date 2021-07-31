from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    t = n*(n-1)
    c = Counter(l)
    for k, v in c.items():
        if v > 1:
            t -= (v*(v-1))
    print(t)
