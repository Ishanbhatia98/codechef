for _ in range(int(input())):
    n, k = map(int, input().split())
    neg = []
    i = 0
    for _ in range(n-k):
        if i>n-1:
            r = (n-1)-(i%n)
            neg.append(r)
        else:
            neg.append(i)
        i+=2
    
    for i in range(1, n+1):
        if i-1 in neg:
            print(-i, end=' ')
        else:
            print(i, end=' ')
    print()
