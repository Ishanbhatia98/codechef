from math import ceil
def count(n, m):
    mx = max(n, m)
    mn = min(n, m)
    a = ceil(mx/2)
    b = mx-a
    am = ceil(mn/2)
    bm = mn-am
    return a*am+b*bm

def convert(s):
    l = []
    for i in s:
        if i=='.':
            l.append(0)
        else:
            l.append(1)
    return l

def f(matrix, n,  m,  c, t):
    if n==0:
        return 0
    elif on>=n>0 and om>=m>0:
        if matrix[n-1][m-1]==1:
            matrix[n-1][m-1]=0
            left = 1+f(matrix, n, m-1, c, t-1)
            matrix[n-1][m-1]=1
            return min(left, f(matrix, n, m-1, c, t))
        else:
            matrix[n-1][m-1] = 1
            right = 1+f(matrix, n, m-1, c, t+1)
            matrix[n-1][m-1] = 0
            return min(f(matrix, n, m-1, c, t), right)
    elif on>=n>=0 and om<0:
        return f(matrix, n-1, om, c, t)
    else:
        return 0
        #return float('inf')



    
for _ in range(int(input())):
    on, om = map(int, input().split())
    c = count(on, om)
    matrix = []
    t = 0
    for _ in range(on):
        s = input()
        l = convert(s)
        matrix.append(l)
        t+=sum(l)
    print(f(matrix, on, om, c, t))
