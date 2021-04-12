for _ in range(int(input())):
    w1, w2, x1, x2, m = map(int, input().split())
    r = (w2-w1)/m
    print(int(r>=x1 and r<=x2))
        
