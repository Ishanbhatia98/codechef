for _ in range(int(input())):
    n, k, x, y = map(int, input().split())
    if x==y:
        print(n, n)
    else:
        k%=4
        if x>y:
            if k==0:
                print(x-y, 0)
            elif k==1:
                print(n, n+y-x)
            elif k==2:
                print(n+y-x, n)
            else:
                print(0, x-y)
        else:
            if k==1:
                print(n+x-y, n)
            elif k==2:
                print(n, n+x-y)
            elif k==3:
                print(y-x, 0)
            else:
                print(0, y-x)

