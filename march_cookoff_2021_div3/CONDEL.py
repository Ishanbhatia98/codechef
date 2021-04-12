for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    t = sum(l[:k])
    m = min(t, k)
    for i in range(k, n):
        t-=l[i-k]
        t+=l[i]
        m = min(m, t)
    print(m*(m+1)//2+sum(l)-m)
