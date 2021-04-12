
def bs(nl, nr, i):
    if nl > nr:
        return -1
    if l[i][0] >= k:
        return 0
    mid = nl + (nr-nl)//2
    mn = min(m, n-i)+1
    exp1 = pr[i][mid]-pr[mn][mid]-pr[i][mn]+pr[mn][mn]

    rhs = (mn-1)*(mn-1)*k
    if mid != 0:
        exp2 = pr[i][mid-1]-pr[mn][mid-1]-pr[i][mn]+pr[mn][mn]

    if exp1 >= rhs and mid == 0:
        return 0
    elif exp1 >= rhs and exp2 < rhs:
        return mid
    elif exp1 >= rhs and exp2 > rhs:
        return bs(0, mid-1, i)

    return bs(mid+1, m, i)


def check(i, j):
    for x in range(1, min(n-i, m-j)+1):
        if pr[i][j]-pr[i][j+x]-pr[i+x][j]+pr[i+x][j+x] >= x*x*k:
            return min(n-i, m-j)-x+1
    return 0


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    pr = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            pr[i][j] = l[i][j]
    for i in range(n):
        for j in range(m-2, -1, -1):
            pr[i][j] += pr[i][j+1]
    for i in range(n-2, -1, -1):
        for j in range(m):
            pr[i][j] += pr[i+1][j]
    # print(pr)
    t = 0
    for i in range(n):

        r = bs(0, m-1, i)
        print(r)

        if r != -1:

            for j in range(r, m):
                if i != n-1 and j != m-1:
                    print(i, j, check(i, j))
                    t += check(i, j)
                else:
                    t += (l[i][j] >= k)
                    print(i, j, (l[i][j] >= k))
    print(t)
