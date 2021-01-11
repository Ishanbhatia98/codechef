for _ in range(int(input())):
    n, k  = map(int, input().split())
    l = list(map(int, input().split()))
    for i in range(n):
        x = l[i]
        while x>0:
            x//=2
            l.append(x)
    l = sorted(l, reverse=True)
    c = 0
    for i in l:
        if k<=0:
            break
        else:
            k-=i
            c+=1
    if k>0:
        print('Evacuate')
    else:
        print(c)
