from collections import Counter
from collections import defaultdict as dd


for _ in range(int(input())):
    n = int(input())

    l = list(map(int, input().split()))
    c = Counter(l)
    t = 0
    for k, v in c.items():
        t += min(v, k-1)
    print(t)
