for _ in range(int(input())):
    n = int(input())
    if n==1:
        a = int(input())
        print(a)
    elif n==2:
        a, b = map(int, input().split())
        print(max(a, b))
    elif n==3:
        a, b, c = map(int,input().split())
        print(min(max(a+b, c), max(a, b+c), max(b, a+c)))
    else:
        a, b, c, d = map(int, input().split())
        print(min(max(a, b+c+d),max(a+d+c, b), max(a+b, c+d), max(a+b+d,c),  max(a+b+c, d), max(a+c, b+d), max(a+d, b+c)))
