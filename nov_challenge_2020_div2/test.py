from collections import defaultdict
def ins(si, it):
    if it in si:
        return ins(si, it)
    return it
def check(it):
    if it in new:
        return check(it**2)
    return it

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    it = 2
    s = set()
    si = set()
    new = [0 for _ in range(n)]
    d = defaultdict(list)
    for i in range(n):
        d[l[i]].append(i)
    for k in d.keys():
        for i in d[k]:
            new[i] = check(it)
        it+=1
    print(*new)
