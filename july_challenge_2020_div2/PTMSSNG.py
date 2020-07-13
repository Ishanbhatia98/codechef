#70pts
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    x, y = [], []
    for _ in range((4*n)-1):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)


    xn = Counter(x).most_common()[-1][0]
    yn = Counter(y).most_common()[-1][0]
    print(xn, yn)
