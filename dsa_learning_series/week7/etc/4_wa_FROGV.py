def find(i):
    for j in range(on):
        if l[j][0]==i:
            return j
    return -1

def f(n, m):
    if t[n][m]!=-1:
        return t[n][m]

    ni, mi = find(n), find(m)
    assert(ni!=-1 and mi!=-1)
    
    mxi, mni = mi, ni
    mx, mn = l[mxi][1], l[mni][1]
    
    if mx-mn<=k:
        t[n][m] = t[m][n] = True
        return t[n][m]
    elif l[mni+1][1]-l[mni][1]<=k:
            t[n][m] = t[m][n] = f(l[mni+1][0], l[mxi][0])
            return t[n][m]
    else:
        t[n][m] = t[m][n] = False
        return False

on, k, p = map(int, input().split())
l = list(enumerate(list(map(int, input().split())) , 1))
l = sorted(l, key=lambda x:x[1])
t = [[-1 for _ in range(on+2)] for _ in range(on+2)]

for _ in range(p):
    a, b = map(int, input().split())
    print('Yes' if f(a, b) else 'No')
