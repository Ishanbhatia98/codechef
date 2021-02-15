from collections import defaultdict
def f(n, a, b):
    if n==0:
        if abs(a-b)%2==0:
            return True
        return False
    if d[(n, a, b)]!=-1:
        return d[(n, a, b)]
    d[(n, a, b)] = f(n-1, a+l[n-1], b) or f(n-1, a, b+l[n-1])
    return d[(n, a, b)]
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d =defaultdict(lambda :-1)
    if f(n, 0, 0):
        print(1)
    else:
        print(2)

