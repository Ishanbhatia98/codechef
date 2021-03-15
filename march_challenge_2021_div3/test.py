from collections import defaultdict as dd
import sys
sys.setrecursionlimit(10**8)


def f(n, e, h, a, b, c):
    if n < 0:
        return 0
    if d[(n, e, h)] != -1:
        return d[(n, e, h)]
    m = float('inf')

    # All omellettes
    if 2*n <= e:
        m = min(m, n*a)

    # All shakes
    if 3*n <= h:
        m = min(m, n*b)

    # All cakes
    if e >= n and h >= n:
        m = min(m, n*c)

    #Shakes and Cakes
    if (h-n)//2 >= 1 and (h-n)//2 >= n-e:
        if b < c:
            t = min(n-1, (h-n)//2)
            m = min(m, t*(b-c)+n*c)
        else:
            t = max(1, n-e)
            m = min(m, t*(b-c)+n*c)

    #Omelletes and shakes
    if e//2 >= 1 and 3//2 >= (3*n-h+2)//3:
        if a < b:
            t = min(n-1, e//2)
            m = min(m, t*(a-b)+n*b)
        else:
            t = max(1, (3*n-h+2)//3)
            m = min(m, t*(a-b)+n*b)

    #Omelletes and Cakes
    if e-n >= 1 and e+h >= 2*n:
        if a < c:
            t = min(n-1, e-n)
            m = min(m, t*(a-c)+n*c)
        else:
            t = max(1, n-h)
            m = min(m, t*(a-c)+n*c)

    # All
    if n >= 3 and e >= 3 and h >= 4:
        m = min(m, a+b+c+f(n-3, e-3, h-4, a, b, c))

    d[(n, e, h)] = m
    return m


for _ in range(int(input())):
    n, e, h, a, b, c = map(int, input().split())
    d = dd(lambda: -1)
    r = f(n, e, h, a, b, c)
    print(r if r != float('inf') else -1)
