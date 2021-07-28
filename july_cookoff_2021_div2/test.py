from collections import Counter


def check(m):
    for i in l:
        if i != m:
            if i % m == 0:
                return False
    return True


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = Counter(l)
    m = min(l)
    if m == 0:
        print(n-c[0])
    elif m == 1:
        if all(i % 2 != 0 for i in l):
            print(n-c[1])
        else:
            print(n)
    elif check(m):
        print(n-c[m])
    else:
        print(n)
