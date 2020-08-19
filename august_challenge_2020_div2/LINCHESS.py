for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = sorted(l)
    l = [i for i in l if i<k]
    l = l[::-1]
    f = 1
    for i in l:
        if k%i==0:
            f= 0
            print(i)
            break
    if f:
        print(-1)
