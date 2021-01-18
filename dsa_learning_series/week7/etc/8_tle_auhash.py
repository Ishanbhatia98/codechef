'''
a very naive brute force approach
Variables changing at every recursive call
n->size of string
s->sum of string left to be computed
last->value of the last element included
'''
def f(n, s, last = 0):
    if n==0 and s==0:
        return 1
    elif n==0 and s!=0:
        return 0
    elif n!=0 and s==0:
        return 0
    t = 0
    for i in range(last+1, 53):
        if i<=s:
            t+=f(n-1, s-i, last = i)
    return t

for _ in range(int(input())):
    n, s = map(int, input().split())
    print(f(n, s))
