for _ in range(int(input())):
    n = int(input())
    l = 0
    for i in range(n):
        if i%2==0:
            for j in range(n):
                l+=1
                print(l, end = ' ')
        else:
            k = l+n
            for j in range(n):
                print(k, end = ' ')
                k-=1
            l+=n
        print()
