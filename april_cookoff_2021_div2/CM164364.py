from collections import Counter
for _ in range(int(input())):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    c = Counter(l)
    cn = len(c.keys())
    if n-cn >= x:
        print(cn)
    else:
        print(n-x)
