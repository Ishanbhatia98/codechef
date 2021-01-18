'''
a very naive brute force approach
Variables changing at every recursive call
n->size of string
s->sum of string left to be computed
last->value of the last element included
'''
from collections import defaultdict

def f(n, s, last = 0):
    if n==0 and s==0:
        return 1
    elif n==0 and s!=0:
        return 0
    elif n!=0 and s==0:
        return 0
    if d[(n, s, last)]!=-1:
        return d[(n, s, last)]
    t = 0
    for i in range(1, 53):
        if i<=s and i>last:
            t+=f(n-1, s-i, last = i)
    d[(n, s, last)] = t
    return t

d = defaultdict(lambda :-1)


for c in range(int(input())):
    n, s = map(int, input().split())
    if n>52:
        print(f'case {c+1}: 0')
    elif s>1378:
        print(f'case {c+1}: 0')
    else:
        print(f'case {c+1}: {f(n, s)}')
