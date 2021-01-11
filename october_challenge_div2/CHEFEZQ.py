for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    f = 1
    s = 0
    for i in range(n):
        s+=l[i]
        s-=k
        if s<0:
            f=0
            print(i+1)
            break
    if f:
        r = s//k
        print(1+r+n)
